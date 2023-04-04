import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 357282961 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    b = np.sqrt(2) / 2
    m = x.mean()
    s = np.abs(x - m).mean() / b
    a = 1 / (s ** 2)
    acceleration = laplace.fit(x, scale=1/a)[1]
    return acceleration
