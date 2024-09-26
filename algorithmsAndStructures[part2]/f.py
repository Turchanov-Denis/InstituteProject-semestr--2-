import numpy as np
import matplotlib.pyplot as plt

# Параметры решетки и света
d = 1.0  # Расстояние между щелями
wavelength = 0.5  # Длина волны света
theta = np.linspace(-np.pi/2, np.pi/2, 1000)  # Углы от -π/2 до π/2

# Распределение интенсивности
intensity = np.sin(np.pi * d * np.sin(theta) / wavelength) ** 2

# Находим максимумы и минимумы
maxima = np.where(intensity == np.max(intensity))[0]
minima = np.where(intensity == np.min(intensity))[0]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(theta, intensity, color='blue', label='Интенсивность')
plt.scatter(theta[maxima], intensity[maxima], color='red', label='Максимумы', marker='o')
plt.scatter(theta[minima], intensity[minima], color='green', label='Минимумы', marker='x')
plt.title('Распределение интенсивности для дифракционной решетки с тремя отверстиями')
plt.xlabel('Угол θ')
plt.ylabel('Интенсивность')
plt.axhline(0, color='black', linewidth=0.5)  # Добавляем горизонтальную линию на уровне нуля
plt.grid(True)
plt.legend()
plt.show()
