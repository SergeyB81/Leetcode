import os
import json
from PIL import Image

import torch
import torch.utils.data as data
import torchvision.transforms.v2 as tfs
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm


class DigitDataset(data.Dataset):
    def __init__(self, base_path, train=True, transform=None):
        # 1. Сначала сохраняем базовый путь, чтобы избежать AttributeError
        self.base_path = base_path
        # 2. Определяем конкретную папку (train или test)
        self.folder_path = os.path.join(base_path, "train" if train else "test")
        self.transform = transform

        # Загружаем формат из корня датасета
        with open(os.path.join(base_path, "format.json"), "r") as fp:
            self.format = json.load(fp)

        self.files = []
        # Мы будем использовать CrossEntropyLoss с индексами классов,
        # поэтому One-Hot (torch.eye) внутри Dataset обычно не нужен.

        for _dir, _target in self.format.items():
            dir_full_path = os.path.join(self.folder_path, _dir)
            if os.path.exists(dir_full_path):
                list_files = os.listdir(dir_full_path)
                for _f in list_files:
                    self.files.append((os.path.join(dir_full_path, _f), int(_target)))

    def __getitem__(self, item):
        path_file, target = self.files[item]
        img = Image.open(path_file).convert('L')  # Конвертируем в ч/б на всякий случай

        if self.transform:
            # Превращаем в тензор и вытягиваем в вектор
            img = self.transform(img)
            img = torch.flatten(img).float() / 255.0

        # CrossEntropyLoss в PyTorch ожидает индекс класса (Long), а не One-Hot вектор
        return img, torch.tensor(target, dtype=torch.long)

    def __len__(self):
        return len(self.files)


class DigitNN(nn.Module):
    def __init__(self, input_dim, num_hidden, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, num_hidden),
            nn.ReLU(),
            nn.Linear(num_hidden, output_dim)
        )

    def forward(self, x):
        return self.net(x)


# --- Настройки ---
input_size = 28 * 28
model = DigitNN(input_size, 32, 10)
to_tensor = tfs.ToImage()

# Загрузка данных
try:
    d_train = DigitDataset("dataset", train=True, transform=to_tensor)
    train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)
except FileNotFoundError:
    print("Ошибка: Проверьте, что папка 'dataset' и файл 'format.json' существуют.")
    exit()

# Обучение
optimizer = optim.Adam(params=model.parameters(), lr=0.001)  # Снизил lr, 0.01 многовато для Adam
loss_function = nn.CrossEntropyLoss()
epochs = 5

model.train()
for _e in range(epochs):
    loss_mean = 0
    train_tqdm = tqdm(train_data, leave=True)

    for x_train, y_train in train_tqdm:
        predict = model(x_train)
        loss = loss_function(predict, y_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        loss_mean = 0.9 * loss_mean + 0.1 * loss.item()  # Экспоненциальное среднее для красоты
        train_tqdm.set_description(f"Epoch [{_e + 1}/{epochs}], loss={loss_mean:.3f}")

# Тестирование
d_test = DigitDataset("dataset", train=False, transform=to_tensor)
test_data = data.DataLoader(d_test, batch_size=500, shuffle=False)

model.eval()
correct = 0
total = 0

with torch.no_grad():
    for x_test, y_test in test_data:
        outputs = model(x_test)
        _, predicted = torch.max(outputs.data, 1)
        total += y_test.size(0)
        correct += (predicted == y_test).sum().item()

accuracy = correct / total if total > 0 else 0
print(f"\nAccuracy на тестовой выборке: {accuracy:.2%}")