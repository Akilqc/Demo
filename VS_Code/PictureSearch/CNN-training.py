import torch
import torch.nn as nn
import torchvision
import matplotlib.pyplot as plt

device = torch.device('cuda:0')

num_epochs = 6
num_classes = 10
batch_size_pre = 100
learning_rate = 0.001

train_data_set = torchvision.datasets.MNIST(root = './mnist_set', train = True, transform = torchvision.transforms.ToTensor(), download = True)
test_data_set = torchvision.datasets.MNIST(root = './mnist_set', train = False, transform = torchvision.transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset = train_data_set,
                                           batch_size = batch_size_pre,
                                           shuffle = True)
test_loader = torch.utils.data.DataLoader(dataset = test_data_set,
                                          batch_size = batch_size_pre,
                                          shuffle = False)


class CNN_Net(nn.Module):

    def __init__(self):
        super(CNN_Net, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size = 5, stride = 1, padding = 2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(stride = 2, kernel_size = 2)
        )

        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size = 5, padding = 2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(stride = 2, kernel_size = 2)
        )
        self.fc = nn.Linear(7 * 7 * 32, 10)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out


cnn = CNN_Net()

cnn = cnn.to(device)
cost = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(cnn.parameters(), lr = learning_rate)

los = []
ep_count = 0
# Train the model
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        # forward = backward = optimize
        outputs = cnn(images)
        loss = cost(outputs, labels)
        los.append(loss)
        ep_count += 1
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i + 1) % 100 == 0:
            print('Epoch[{}/{}], Step[{}/{}], Loss:{:.4f}'
                  .format(epoch + 1, num_epochs, i + 1, len(train_data_set), loss.item()))

# test model
cnn.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = cnn(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum()

print('Test Accuracy of the model on the 10000 test images: {} %'.format(100 * correct / total))
# plt.plot(list(range(ep_count)), los, color = 'green')
# plt.show()