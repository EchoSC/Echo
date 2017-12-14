from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import json
from pandas import DataFrame, Series
os.chdir("G:\\python\\test")
path = (r'G:\\python\\test\\usagov_bitly_data.txt')
open(path).readline()  # 打开txt读取文件
records = [json.loads(line) for line in open(path)]
print(records[0]['tz'])
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

# def get_counts(sequence):
    # counts = {}
    # for x in sequence:
        # if x in counts:
            # counts[x] += 1  # 依次读取序列sequence，计算每个列表元素的个数
        # else:
            # counts[x] = 1  #只有1个的意思
    # return counts
# counts = get_counts(time_zones)
# print(counts['Europe/Uzhgorod'])

# def top_counts(count_dict, n=10):
    # value_key_pairs = [(count, tz) for tz, count in count_dict.items()]  #按元组的形式取出count_dict的某对值
    # value_key_pairs.sort()  #排序,默认升序
    # return value_key_pairs[-n:]  #输出后n个，其实是频率高的前10
# print(top_counts(counts))


frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
plt.figure(figsize=(10, 4))
tz_counts[:10].plot(kind='barh', rot=0)
plt.show()