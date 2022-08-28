'''
《数字图像处理》大作业
董欣然
1900013018
'''
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
import torch
from model  import Network
# import model
def smooth_edge(gray_image):
    '''
    平滑车票边缘凸起
    '''
    # 全局最佳阈值分割
    _,binary_image = cv2.threshold(gray_image, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (70, 70))
    # 开操作
    mor_img = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel1) 
    # 闭操作
    mor_img = cv2.morphologyEx(mor_img, cv2.MORPH_CLOSE, kernel2)
    # 开操作
    mor_img = cv2.morphologyEx(mor_img, cv2.MORPH_OPEN, kernel2)
    return cv2.bitwise_and(gray_image,mor_img)

def rotate_convex(image):
    '''
    旋转车票
    '''  
    # 找到最大的连通块
    contours, hierarchy=cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rect=contours[0]
    for i in contours:
        if len(i)>len(rect):
            rect=i
    # 找到车票所在矩形
    rect = cv2.minAreaRect(rect.squeeze())
    box = cv2.boxPoints(rect)
    # print(box)
    edge_length = rect[1]
    if(edge_length[0]>edge_length[1]):
        angle = -(180 - rect[2])
    else:
        angle = -(90 - rect[2])
    center=rect[0]
    width=max(edge_length)
    height=min(edge_length)
    # 旋转矩形
    moving_matrix=np.float64([[1,0,width],[0,1,height]])
    rotate_martrix = cv2.getRotationMatrix2D(center, angle, 1)

    rotate_martrix[0][2] += width/2
    rotate_image = cv2.warpAffine(image, rotate_martrix, (2*int(width), 2*int(height)))
    return rotate_image

def cut_convex(image):
    '''
    裁剪车票
    '''
    contours, hierarchy=cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rect=contours[0]
    for i in contours:
        if len(i)>len(rect):
            rect=i

    rect = cv2.minAreaRect(rect.squeeze())
    box = np.int0(cv2.boxPoints(rect))
    # 得到矩形边缘坐标
    min_y=min(box[:,1])
    max_y=max(box[:,1])
    min_x=min(box[:,0])
    max_x=max(box[:,0])

    cut_image = image[min_y:max_y,min_x:max_x]
    return cut_image

def flip(image):
    '''
    翻转车票
    '''
    w,h=image.shape
    upper_image=image[0:int(image.shape[0]/2),:]
    botom_image=image[int(image.shape[0]/2):image.shape[0],:]
    # 比较车票上下部分灰度值
    if np.sum(upper_image)<np.sum(botom_image):
        rotate_martrix = cv2.getRotationMatrix2D((h/2,w/2), 180, 1)
        image = cv2.warpAffine(image, rotate_martrix, (h,w))
    return image

def find_mask7(gray_image):
    '''
    对7位码定位出所在矩形位置
    '''
#    提取七位码
    ret, _ = cv2.threshold(gray_image[30:100, 50:400], 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    _, binary_image2 = cv2.threshold(gray_image, ret, 255, cv2.THRESH_BINARY) 
    _, binary_image1 = cv2.threshold(gray_image, ret/3, 255,cv2.THRESH_BINARY) 

    binary_image=binary_image1-binary_image2
    mask_7 = np.zeros(binary_image.shape, dtype=np.uint8)
    mask_7[30:100, 50:400] = 1
# 粗定位
    binary_image = binary_image * mask_7

    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    kernel20 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
    mor_img = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel2)
    mor_img = cv2.morphologyEx(mor_img, cv2.MORPH_CLOSE, kernel20)

    retval, labels, stats, _ = cv2.connectedComponentsWithStats(mor_img, connectivity=8)
    for i in range(retval):
        if stats[i][4] < 150:
            mor_img[labels==i] = 0
# 精定位
    coords_7 = np.column_stack(np.where(mor_img > 0))
    rect_7 = cv2.minAreaRect(coords_7)
    box_7_ = np.int0(cv2.boxPoints(rect_7))
    box_7_ = box_7_[np.lexsort(np.rot90(box_7_))]
    h_min_7 = np.min(box_7_[:, 0]) - 6
    h_max_7 = min(np.max(box_7_[:, 0]),np.min(box_7_[:, 0])+40) +3
    w_min_7 = np.min(box_7_[:, 1]) - 3
    w_max_7 = np.max(box_7_[:, 1]) + 3    
    mask7=np.zeros_like(gray_image)
    mask7[h_min_7:h_max_7,w_min_7:w_max_7]=1
    mask_image=binary_image*mask7
    return mask_image,(h_min_7,h_max_7,w_min_7,w_max_7)

def split_num7(mask_image,mask7,rgb_image):
    '''
    在精确定位区域中分割7位码
    '''
    h_min_7,h_max_7,w_min_7,w_max_7=mask7
    # 根据连通域以自适应间距精细分割7位码
    contours = cv2.findContours(mask_image, 2, 2)[0]
    # 确定连通块
    x_list = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w*h >= 200:
            x_list.append(x)

    x_list.sort()
    x_min=x_list[0]
    del x_list[0]
    line_num_7 = 0
    letter_list=[]
    copy_image=np.copy(rgb_image)
    for i in range(len(x_list)):
        if line_num_7 == 0:
            dist_min = 20
        else:
            dist_min = 15
        # 认为该连通块是一个符号
        if x_list[i] > x_min + dist_min:
            cv2.line(copy_image, (x_list[i], h_min_7), (x_list[i], h_max_7), (0, 0, 255), 2)       
            letter_list.append(rgb_image[h_min_7:h_max_7,int(x_min)-2:x_list[i]])
            x_min = x_list[i]
            line_num_7 += 1

    if line_num_7 != 6:     # 等距分割
# 自适应分割失败，采用均等分割
        letter_list=[]
        copy_image=np.copy(rgb_image)
        interval = (w_max_7 - w_min_7 -4) / 7.5
        x_min = w_min_7+2
        for i in range(6):
            left_x=int(x_min)        
            if i == 0:              
                x_min += interval * 1.5
                right_x=int(x_min)
            else:
                x_min += interval
                right_x=int(x_min)
            letter_list.append(rgb_image[h_min_7:h_max_7,left_x:right_x])              
            cv2.line(copy_image, (right_x, h_min_7), (right_x, h_max_7), (0, 0, 255), 1)

    letter_list.append(rgb_image[h_min_7:h_max_7,int(x_min):w_max_7])

    rgb_image=copy_image
    cv2.line(rgb_image,(w_min_7,h_min_7),(w_max_7,h_min_7),(0, 0,255), 2)    
    cv2.line(rgb_image,(w_min_7,h_max_7),(w_max_7,h_max_7),(0, 0,255), 2)  
    cv2.line(rgb_image,(w_min_7,h_min_7),(w_min_7,h_max_7),(0, 0,255), 2)    
    cv2.line(rgb_image,(w_max_7,h_min_7),(w_max_7,h_max_7),(0, 0,255), 2)  
    return rgb_image,letter_list

def find_mask21(gray_image):
    '''
    对21位码定位出所在矩形位置
    '''    
    # gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
    gaussian_img_21 = cv2.GaussianBlur(gray_image, (5, 5), 0)
    binary_image = cv2.threshold(gaussian_img_21, 30, 255, cv2.THRESH_BINARY)[1]
    binary_image=255-binary_image
    # 粗定位
    mask_21 = np.zeros(binary_image.shape, dtype=np.uint8)
    mask_21[550:-10, 20:500] = 1
    binary_image=binary_image*mask_21

    coords_21 = np.column_stack(np.where(binary_image>0))
    rect_21 = cv2.minAreaRect(coords_21)
    box_21_ = np.int0(cv2.boxPoints(rect_21))
    box_21_ = box_21_[np.lexsort(np.rot90(box_21_))]
    h_max_21 = np.max(box_21_[:, 0])
    w_min_21 = np.min(box_21_[:, 1])
# 精定位
    mask_21 = np.zeros(binary_image.shape, dtype=np.uint8)
    mask_21[h_max_21-40:h_max_21, w_min_21:w_min_21+385] = 1
    binary_image=binary_image*mask_21

    coords_21 = np.column_stack(np.where(binary_image>0))
    rect_21 = cv2.minAreaRect(coords_21)
    box_21_ = np.int0(cv2.boxPoints(rect_21))
    box_21_ = box_21_[np.lexsort(np.rot90(box_21_))]
# 找到21位码位置
    h_min_21 = np.min(box_21_[:, 0]) - 5
    h_max_21 = np.max(box_21_[:, 0]) + 5
    w_min_21 = np.min(box_21_[:, 1]) - 4
    w_max_21 = np.max(box_21_[:, 1]) + 4
    mask_21=np.zeros_like(gray_image)
    mask_21[h_min_21:h_max_21,w_min_21:w_max_21]=1
    mask_image=binary_image*mask_21

    return mask_image,(h_min_21,h_max_21,w_min_21,w_max_21)

def split_num21(mask_image,mask21,rgb_image):
    '''
    在精确定位区域中分割21位码
    '''
    h_min_21,h_max_21,w_min_21,w_max_21=mask21
    contours, hierarchy = cv2.findContours(mask_image, 2, 2)
    x_min = 2000
    x_list = []
    # 找到可能是符号的连通块
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w*h >= 40:
            x_list.append(x)
    # if (len(x_list)==0):
    #     plt.imshow(mask_image)
    #     plt.show()
    x_list.sort()
    x_min=x_list[0]
    del x_list[0]
    letter_list=[]
# 自适应分割算法
    line_num_21 = 0
    copy_image=np.copy(rgb_image)
    for i in range(len(x_list)):
        if line_num_21 == 14:
            dist_min = 19
        elif line_num_21 == 13:
            x_list[i] -= 2
        else:
            dist_min = 9
        if x_list[i] > x_min + dist_min:
            cv2.line(copy_image, (x_list[i]-1, h_min_21), (x_list[i]-1, h_max_21), (0, 0, 255), 1)
            letter_list.append(rgb_image[h_min_21:h_max_21,x_min-2:x_list[i]-1])
            x_min = x_list[i]           
            line_num_21 += 1

    if line_num_21 != 20:     # 等距分割
        copy_image=np.copy(rgb_image)

        letter_list=[]
        interval = (w_max_21 - w_min_21 - 6) / 21.5
        x_min = w_min_21+3

        for i in range(20):
            left_x=int(x_min)
            if i == 14:
                x_min += interval * 1.5
            else:
                x_min += interval
            right_x=int(x_min)
            letter_list.append(rgb_image[h_min_21:h_max_21,left_x-2:right_x-1])
            cv2.line(copy_image, (right_x, h_min_21), (right_x, h_max_21), (0, 0, 255), 1)
    letter_list.append(rgb_image[h_min_21:h_max_21,int(x_min):w_max_21])
    rgb_image=copy_image
    cv2.line(rgb_image, (w_min_21, h_min_21), (w_min_21, h_max_21), (0, 0, 255), 2)
    cv2.line(rgb_image, (w_max_21, h_min_21), (w_max_21, h_max_21), (0, 0, 255), 2)
    cv2.line(rgb_image, (w_min_21, h_min_21), (w_max_21, h_min_21), (0, 0, 255), 2)
    cv2.line(rgb_image, (w_min_21, h_max_21), (w_max_21, h_max_21), (0, 0, 255), 2)
    
    return rgb_image,letter_list



def preprocess(image_path):
    '''
    任务一：车票票面检测
    '''
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    gray_image=smooth_edge(gray_image)
    gray_image=rotate_convex(gray_image)
    gray_image = cut_convex(gray_image)
    gray_image = flip(gray_image)
    # plt.imshow(gray_image,cmap='gray')
    # plt.show()
    
    return cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)


def segment(rgb_image):
    '''
    任务二：车票序列号定位与分割
    '''
    # 21位码分割
    gray_image=cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)
    mask_image, mask21 = find_mask21(gray_image)
    rgb_image,letter_list21 = split_num21(mask_image, mask21, rgb_image)
    # 7位码分割
    mask_image, mask7 = find_mask7(gray_image)
    rgb_image,letter_list7 = split_num7(mask_image, mask7, rgb_image)
    
    return rgb_image,letter_list21+letter_list7
   
   
    # cv2.imwrite('segments/'+image_name, rgb_image)
# image_path='training_data/2018-5-22-17-55-35.bmp'
# gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# rgb_image=preprocess(image_path)
# rgb_image,letter_list,number_list=segment(rgb_image)
# plt.imshow(rgb_image)
# plt.show()

def data_import():
    '''
    导入训练数据
    '''
    file_path = 'training_data/annotation.txt'
    file = open(file_path, 'r', encoding='utf-8')
    for line in file.readlines():
        image_name = line.split()[0]

        # rgb_image = cv2.imread('predeal_data/'+image_name)
        print(image_name)
        rgb_image = preprocess('training_data/'+image_name)
        rgb_image,letter_list=segment(rgb_image)
        cv2.imwrite('segments/'+image_name, rgb_image)

# data_import()
def predict(letter_list,line):
    '''
    序列号识别
    '''
    # decode_21=list(range(21))
    # decode_7=list(range(7))
    decode_21=''
    decode_7=''
    for i in range(len(letter_list)):
        # 将图片二值化
        char=cv2.cvtColor(letter_list[i], cv2.COLOR_RGB2GRAY)
        char = cv2.resize(char, (32, 32))          
        if i<21:
            _,char = cv2.threshold(char, 30, 255,cv2.THRESH_BINARY)
        else :
            _,char = cv2.threshold(char, 150, 255,cv2.THRESH_BINARY)
        # _,char = cv2.threshold(char, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # 消除其他数字的干扰
        retval, labels, stats, _ = cv2.connectedComponentsWithStats(char, connectivity=8)
        for j in range(retval):
            if stats[j][4] < 20:
                char[labels==j] = 0

        # cv2.imwrite('test/'+str(i)+'.bmp',char) 
        char = torch.from_numpy(char)
        char = char.unsqueeze(0).unsqueeze(0).float()
        if i==14 or i==21:
            model_name="letter"
        else :
            model_name='number'
        logits = model(char, model_name)
        predict = logits.max(dim=1)[1]
        if i==14 or i==21:
            predict_code=chr(predict+65)
        else:
            predict_code=str(int(predict[0]))
        if i<21:
            decode_21+=predict_code
        else :
            decode_7+=predict_code

    return decode_21+' '+decode_21[-7:]+'\n'


if __name__ == "__main__":
    print('数字图像处理大作业 董欣然 1900013018')
    parser = argparse.ArgumentParser(description='Image Processing(DongXinran)')
    # 测试图片路径参数，默认test_data
    parser.add_argument('--dir', default='test_data', type=str)
    # 测试文件路径参数，默认test_data/annotation.txt
    parser.add_argument('--txt', default='test_data/annotation.txt', type = str)
    args = parser.parse_args()
    # annotation.txt路径
    annotation_path = args.txt
    # test_data路径
    test_data_path = args.dir
    # segments路径
    segments_path = 'segments/'
    # prediction.tx路径
    prediction_path = 'prediction.txt'
    if not os.path.exists(segments_path):
        os.makedirs(segments_path)

    # 创建模型, 载入预训练模型参数
    model = Network(number_class=10, letter_class=26)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.load_state_dict(torch.load('model.pth',map_location=torch.device(device)), strict=False)
    model.eval()
    print('test data importing..')

    reader= open(annotation_path, 'r', encoding='utf-8') 
    writer = open(prediction_path, 'w', encoding='utf-8')
    lines = reader.readlines()
    ans=0
    for line in lines:
        file_name = line.split()[0]
# 票面检测、分割、识别
        image_path = os.path.join(test_data_path, file_name)
        rgb_image = preprocess(image_path)      
        rgb_image,letter_list=segment(rgb_image)
        cv2.imwrite(segments_path+file_name,rgb_image)

        ans=file_name+' '+predict(letter_list,line)

        writer.write(ans)
    print('done!')
# predict()
        
