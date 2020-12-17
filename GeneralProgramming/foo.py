import requests
import random

alpha_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(10):
    r = ''.join(random.choices(alpha_num, k=6))
    print(f'gs.3g.cn/D/{r}')
