# -*- coding: utf-8 -*-
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='NanumGothic')

print("🚀 PyTorch (CPU-only) 환경 시작!")

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
print("a + b =", a + b)

n = np.array([10, 20, 30])
print("NumPy 배열:", n)

df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 4, 9]})
print("Pandas DataFrame:\n", df)

plt.plot(df['x'], df['y'])
plt.title("간단한 시각화")
plt.savefig("plot.png")
print("📊 시각화 완료: plot.png 저장됨")
