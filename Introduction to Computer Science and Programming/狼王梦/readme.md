# 《狼王梦》词汇统计和人物关系分析
## 姓名：董欣然 


## (一)	简介
《狼王梦》是一部小说，讲述了母狼紫岚培育三只小公狼成为狼王的故事。

## (二)	数据清洗
发现标点符号、空格、“的”、“了”等单字出现频率极高，为了排除这些无实意的单字，作业中去掉了所有单字。

发现小说中的重要角色不在jieba的自带词库中，例如“洛戛”“大白狗”，故将其添加进自定义词库。

发现主人公“紫岚”，有时会被划分成词汇“当紫岚”、“紫岚想”，故将“紫岚”添加进自定义词库。这样保证了一定能划分出单词“紫岚”。

同理将主人公“媚媚”添加进自定义词库。这样保证了一定能划分出单词“媚媚”。

通过整理词汇表，可知小说中的角色十分有限，故将所有角色记录在character_list中，方便与非角色词汇区分。

## (三)	代码功能
将角色和非角色的词汇分为两类，可选择展现其中任意一类。

将词汇按词频从多到少排序，可根据需求输出排名最高的若干个词汇。

将查询结果导入到excel文档中。

## (四)	结果分析
通过对角色词频的分析可知：

词频最高的是“紫岚”，“紫岚”是小说的主人公，全文是以“紫岚”的视角叙事的，词频最高非常合理。

按词频顺序接下来依次是“媚媚”，“双毛”，“蓝魂儿，这几个角色都是“紫岚”的子女，“紫岚”将培育狼王的梦想寄托在她的子女们身上，所以这些角色也是重中之重。

还有词频较高的是“老雕”。“老雕”出现在篇末，小说用巨大的篇幅描述了“紫岚”和“老雕”殊死搏斗的场景，最后紫岚死在老雕的爪下，全文告终。

通过分析可知，出现频次较高的角色和故事情节的发展息息相关，正是这些主要角色组成了全文的脉络。

通过对非角色词频的分析可知：

“自己”出现的频次最高，“一种”、“一个”、“一声”、“一只”、“一匹”等量词的词频较高，说明这篇小说用词简单易懂，易于少儿阅读。

“狼群”、“母狼“”、“公狼“的词频较高，说明这是一篇与狼息息相关的小说，与事实相符。


## （五）数据可视化

我实现了对小说《狼王梦》中角色的词频分析。分别采用了柱状图，词云，漏斗图，和饼状图来展示角色在小说中的重要程度。利用图表的方式可以清晰直观地了解整部小说的人物构成。

### 5.1 链接 [狼王梦角色词频柱状图](https://007DXR.github.io/Introduction%20to%20Computer%20Science%20and%20Programming/狼王梦/html/狼王梦角色词频柱状图.html)
### 预览
![](https://github.com/007DXR/007DXR.github.io/blob/main/Introduction%20to%20Computer%20Science%20and%20Programming/%E7%8B%BC%E7%8E%8B%E6%A2%A6/images/bar.png)


### 5.2 链接 [狼王梦角色词频词云](https://007DXR.github.io/Introduction%20to%20Computer%20Science%20and%20Programming/狼王梦/html/狼王梦角色词频词云.html)
### 预览
![](https://github.com/007DXR/007DXR.github.io/blob/main/Introduction%20to%20Computer%20Science%20and%20Programming/%E7%8B%BC%E7%8E%8B%E6%A2%A6/images/wordCloud.png)


### 5.3 链接 [狼王梦角色词频漏斗图](https://007DXR.github.io/Introduction%20to%20Computer%20Science%20and%20Programming/狼王梦/html/狼王梦角色词频漏斗图.html)
### 预览
![](https://github.com/007DXR/007DXR.github.io/blob/main/Introduction%20to%20Computer%20Science%20and%20Programming/%E7%8B%BC%E7%8E%8B%E6%A2%A6/images/loudou.png)


### 5.4 链接 [狼王梦角色词频饼状图](https://007DXR.github.io/Introduction%20to%20Computer%20Science%20and%20Programming/狼王梦/html/狼王梦角色词频饼状图.html)
### 预览
![](https://github.com/007DXR/007DXR.github.io/blob/main/Introduction%20to%20Computer%20Science%20and%20Programming/%E7%8B%BC%E7%8E%8B%E6%A2%A6/images/pie.png)



## （六）人物关系分析

为了从宏观层面对整部小说有所了解，我制作了《狼王梦》角色关系图

#### 功能：

1.用节点的大小表示角色的重要程度，用节点之间的距离表示角色关系的密切程度

2.将角色分为三类，分别是“公狼”、“母狼”和“其他动物”。

3.按照角色类别设置了三个功能键，可以根据需求查看指定类别之间的角色关系子图。

4.三类角色分别用不同的颜色和形状表示，这里运用了水滴形，圆形和三角形。

5.设置了网页背景，使视图更加美观。

#### 通过对角色关系图的分析,我们可知：

1.词频最高的是“紫岚”，“紫岚”位于整张关系图的中心，其他所有角色均匀散布在“紫岚”的四周。不难看出“紫岚”是小说的主人公，故事是围绕“紫岚”展开的。

2.从关系图中可以看出：与“紫岚”关系最为密切的是若干只公狼，因为“紫岚”是一只母狼，狼王必须是公狼，紫岚将“狼王梦”寄托在她的丈夫和儿子身上。

故事围绕着母狼紫岚培育三只小公狼成为狼王而展开，这与故事脉络相吻合。

3.通过分析可知，角色的互动和故事情节的发展息息相关，从角色关系图可以宏观领略整部小说。

### 链接
#### 点击查看[《狼王梦》角色关系图](https://007dxr.github.io/Introduction%20to%20Computer%20Science%20and%20Programming/狼王梦/html/《狼王梦》角色关系图.html)

#### 网页预览
![](https://github.com/007DXR/007DXR.github.io/blob/main/Introduction%20to%20Computer%20Science%20and%20Programming/%E7%8B%BC%E7%8E%8B%E6%A2%A6/images/relationship.png)

