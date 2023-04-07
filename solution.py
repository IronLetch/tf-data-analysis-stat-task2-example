import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 531503618 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    k=21
    S2 = sum([e ** 2 for e in x])
    ql = np.sqrt(S2 / (k * chi2.ppf(1 - alpha / 2, n * 2)))
    qr = np.sqrt(S2 / (k * chi2.ppf(alpha / 2, n * 2)))
    return  ql, qr
           
