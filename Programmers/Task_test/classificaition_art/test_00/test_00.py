import torch, torchvision
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
import cv2
from zipfile import ZipFile
import numpy as np
from torchvision.models import resnet18
import PIL
import csv

# get img from zip file
# with ZipFile('./train.zip', 'r') as zipobj:
#     file_list = zipobj.namelist()
#     for file in file_list:
#         if file.endswith('jpg'):
#             zip_read = zipobj.read(file)
#             img = cv2.imdecode(np.frombuffer(zip_read, np.uint8), 1)


class myDataset(Dataset):
    def __init__(self, file_path, transform=None):
        super(myDataset, self).__init__()
        self.file_path = file_path
        self.transform = transform
        self.zip_file = ZipFile(file_path, 'r')
        file_list = self.zip_file.namelist()
        self.file_list = [file for file in file_list if file.endswith('jpg')]

        self.label_dic = dict(
            dog=0,
            elephant=1,
            giraffe=2,
            guitar=3,
            horse=4,
            house=5,
            person=6
        )
    def __getitem__(self, idx):

        label = self.file_list[idx].split('/')[1]
        img = cv2.imdecode(np.frombuffer(self.zip_file.read(self.file_list[idx]), np.uint8), 1)

        if self.transform:
            img = self.transform(img)
        else:
            img = transforms.ToTensor(img)

        if label in self.label_dic:
            result = self.label_dic[label]
        else:
            result = 0

        return img, result

    def __len__(self):
        return len(self.file_list)


def train(*args, **kwargs):
    model = kwargs['model']
    dataloader = kwargs['dataloader']
    optimizer = kwargs['optimizer']
    criterion = kwargs['criterion']
    epoch = kwargs['epoch']
    schedular = kwargs['schedular']

    model.train()
    loss_list = []
    acc = []
    for imgs, labels in dataloader:
        input_imgs = imgs.to('cuda:0')
        labels = labels.to('cuda:0')
        labels_onehot = torch.nn.functional.one_hot(labels, 7).to('cuda:0', dtype=torch.float32)
        pred = model(input_imgs)
        target = torch.argmax(pred, dim=-1)
        optimizer.zero_grad()
        loss = criterion(pred, labels_onehot)
        # print(loss.item())
        loss_list.append(loss.item())
        loss.backward()
        optimizer.step()

        acc.extend((target == labels).tolist())
    # schedular.step()
    print(f'epoch {epoch} / loss - {np.mean(loss_list)} / acc - {np.mean(acc)}')
    torch.save(model.state_dict(),f'./E{epoch}_acc_{round(np.mean(acc), 5)}.pth')

def test(*args, **kwargs):
    model = kwargs['model']
    dataloader = kwargs['dataloader']
    model.to('cuda:0')
    model.eval()
    result = []
    for imgs, _ in dataloader:
        input_imgs = imgs.to('cuda')
        pred = model(input_imgs)
        pred_label = torch.argmax(pred, dim=-1).tolist()

        result.extend(pred_label)

    with open('test_answer_sample_.csv', 'w', newline='') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(['', 'answer value'])
        for i, r in enumerate(result):
            csv_file.writerow([str(i), str(r)])


import timm


class FineTunedModel(torch.nn.Module):
    def __init__(self, model_str='resnet18'):
        super().__init__()
        self.net = timm.create_model(model_str, pretrained=True, num_classes=7)

    def forward(self, x):
        x = self.net(x)

        return x
def main(*args, **kwargs):

    # model = resnet18(num_classes=7).to('cuda:0')
    model = FineTunedModel()
    if kwargs['mode'] == 'train':
        optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
        criterion = torch.nn.MSELoss()
        schedular = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, 10, 0.0001)

        train_transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.RandomCrop(224),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
            transforms.RandomHorizontalFlip(p=1),
            transforms.ToTensor()
        ])
        train_dataset = myDataset('../train.zip', train_transform)

        train_dataloader = DataLoader(train_dataset,
                                      batch_size=100,
                                      shuffle=True,
                                      num_workers=0)

        epochs = 100

        for epoch in range(epochs):
            train(epoch=epoch,
                  model=model,
                  dataloader=train_dataloader,
                  optimizer=optimizer,
                  criterion=criterion,
                  schedular=schedular)

    elif kwargs['mode'] == 'test':
        test_transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.ToTensor()
        ])

        test_dataset = myDataset('../test.zip', test_transform)


        test_dataloader = DataLoader(test_dataset,
                                     batch_size=100,
                                     shuffle=False,
                                     num_workers=0)

        state_dict = torch.load('C:/Users/82103/Desktop/git_repos/Algorithm_study/Programmers/Task_test/classificaition_art/test_01/saved_models/K0_E11_96.625.pth')
        model.load_state_dict(state_dict)

        test(model=model, dataloader=test_dataloader)



if __name__ == "__main__":
    main(mode='test')
