import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset, batch_size=64)


class Tudui(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x


tudui = Tudui()
print(tudui)

writer = SummaryWriter("logs")

step = 0
for data in dataloader:
    imgs, target = data
    output = tudui(imgs)
    print(imgs.shape)
    print(output.shape)
    writer.add_images("input", imgs, step)

    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images("output", output, step)

    step += 1

writer.close()
