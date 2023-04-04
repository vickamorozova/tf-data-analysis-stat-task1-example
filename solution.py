import pandas as pd
import numpy as np


chat_id = 357282961 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # вычисляем параметр масштаба распределения Лапласа
    b = np.mean(np.abs(x - np.mean(x)))
    # вычисляем коэффициент ускорения
    path_mean = np.mean(x)
    a = 2 * path_mean / (97**2)
    return a
