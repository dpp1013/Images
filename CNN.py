# 定义网络结构
import torch
class CNNnet(torch.nn.Module):
    def __init__(self):
        super(CNNnet,self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=4,
                            out_channels=8,
                            kernel_size=3,
                            stride=1,
                            padding=1),
            torch.nn.BatchNorm2d(8),
            torch.nn.ReLU()
        )
        self.conv2 = torch.nn.Sequential(
            torch.nn.Conv2d(8,16,3,1,1),
            torch.nn.BatchNorm2d(16),
            torch.nn.ReLU()
        )
        self.conv3 = torch.nn.Sequential(
            torch.nn.Conv2d(16,32,3,1,1),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU()
        )
        self.conv4 = torch.nn.Sequential(
            torch.nn.Conv2d(32,4,1,1,0),
            torch.nn.BatchNorm2d(4),
            torch.nn.ReLU()
        )
        # self.mlp1 = torch.nn.Linear(2*2*64,100)
        # self.mlp2 = torch.nn.Linear(100,10)
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        return x
model = CNNnet()
print(model)
x = torch.randn((64,4,256,256))
y = model(x)
print(y.shape)