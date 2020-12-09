# -*- coding: utf-8 -*-
# @Time : 2020/10/14 10:24
# @Author : zls
# @File : test1.py
# @Software: PyCharm
from NN_model.find import Find

x = '丧失'
sentence = '运动神经的丧失会导致瘫痪'
find = Find(x, sentence)
find.find_positive()
score = find.get_score()
print(score)

# s = '跟在 Find_Positive 后面 Find_Positive -1 And_Ordered 跟踪 Find_Positive Or 事主 Find_Negative 跟随 Find_Negative -1 And_Ordered And_Unordered Output'
# s = s.split(' ')
# print([i for i, x in enumerate(s) if x == 'Find_Positive'])
