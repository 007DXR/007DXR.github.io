'''
《数字图像处理》大作业
董欣然
1900013018
'''
import torch.nn as nn
import torch.nn.functional as F


class Network(nn.Module):
    """
    Architecture:
        conv1: in_channels=1, out_channels=10, kernel_size=5
        pool: kernel_size=2, stride=2
        conv2: in_channels=10, out_channels=20, kernel_size=3
        flatten: flatten
        fc: in_features=20*12*12, out_features=512
        fc_number: in_features=512, out_features=number_class (10)
        fc_letter: in_features=512, out_features=letter_class (26)
    """
    def __init__(self, number_class=10, letter_class=26):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)    # (1, 32, 32) -> (10, 28, 28)
        self.pool = nn.MaxPool2d(2, 2)                  # (10, 28, 28) -> (10, 14, 14)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=3)   # (10, 14, 14) -> (20, 12, 12)
        self.flatten = nn.Flatten()                     # (20, 12, 12) -> (20*12*12)
        self.fc = nn.Linear(20*12*12, 512)              # (20*12*12) -> (512)
        self.fc_number = nn.Linear(512, number_class)   # (512) -> (number_class=10)
        self.fc_letter = nn.Linear(512, letter_class)   # (512) -> (letter_class=26)

    def forward(self, x, type="number"):
        out = self.conv1(x)
        out = F.relu(out)
        out = self.pool(out)
        out = self.conv2(out)
        out = F.relu(out)
        out = self.flatten(out)
        out = self.fc(out)
        out = F.relu(out)
        if type == "number":
            logits = self.fc_number(out)
        elif type == "letter":
            logits = self.fc_letter(out)
        return logits