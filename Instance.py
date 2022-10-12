# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       :  Instance.py
@Time       :  2022/10/12
@Author     :  Yuanting Ma
@Version    :  1.0
@Site       :  https://github.com/YuantingMaSC
@Contact    :  yuantingma@189.cn
"""

import random

random.seed(32)


# State:阶段，即工件有几道工序，Job:工件数，Machine['type':list],对应各阶段的并行机数量
def Generate(State, Job, Machine):
    PT = []
    for i in range(State):
        Si = []  # 第i各加工阶段
        for j in range(Machine[i]):
            S0 = [random.randint(1, 20) for k in range(Job)]
            Si.append(S0)
        PT.append(Si)
    return PT


Job = 20
State = 5
Machine = [3, 3, 2, 3, 3]

PT = Generate(State, Job, Machine)