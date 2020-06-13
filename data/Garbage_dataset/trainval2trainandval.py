import os
import random


# 将垃圾数据集划分为训练集和验证集
trainval = []
with open('trainval.txt') as f:
    line = f.readline()
    while line:
        # data/Garbage_dataset
        line = os.path.join("data/Garbage_dataset/images", line)
        trainval.append(line)
        line = f.readline()
f.close()
print(len(trainval))
print(trainval)

random.shuffle(trainval)
train_len = int(len(trainval) * 0.8)
train = trainval[:train_len]
val = trainval[train_len:]
print(len(train))
print(len(val))
print(trainval)

with open("train.txt", "w") as f:
    for i in range(len(train)):
        # s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        # s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        f.write(train[i])


with open("valid.txt", "w") as f:
    for i in range(len(val)):
        f.write(val[i])