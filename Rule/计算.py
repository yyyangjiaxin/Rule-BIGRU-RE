# 泛化后：
# 测试数据各类的个数为： {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
# 正确抽取的个数为： {'Related-SY': 409, 'Related-CH': 196, 'Related-TR': 254, 'Related-CO': 133}
# 数据预测的各类的个数： {'Related-SY': 462, 'Related-TR': 357, 'Related-CH': 216, 'Related-CO': 139}

# 经过模型：
# 未匹配数据各类的个数为： {'Related-SY': 76, 'Related-CH': 46, 'Related-TR': 55, 'Related-CO': 5}
# 重新匹配后正确抽取的个数为： {'Related-SY': 52, 'Related-CH': 20, 'Related-TR': 37, 'Related-CO': 1}
# 数据预测的各类的个数： {'Related-SY': 81, 'Related-CH': 26, 'Related-TR': 67, 'Related-CO': 8}

# 所以再经过BIGRU模型后的结果为：
# 测试数据各类的个数为： {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
# 正确抽取的个数为： {'Related-SY': 409+52, 'Related-CH': 196+20, 'Related-TR': 254+37, 'Related-CO': 133+1}
# 数据预测的各类的个数： {'Related-SY': 462, 'Related-TR': 357, 'Related-CH': 216, 'Related-CO': 139}
# front = {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
# end = {'Related-SY': 461, 'Related-CH': 216, 'Related-TR': 291, 'Related-CO': 134}
# yuce = {'Related-SY': 462, 'Related-CH': 216,'Related-TR': 357 , 'Related-CO': 139}
# recall = {}
# precision ={}
# f1 = {}
# for k, v in front.items():
#     for k1, v1, in end.items():
#         if k == k1:
#             recall[k] = v1 / v
#             # print(k+'=',v1/v)
# print(recall)
# print('================precison=================')
# for k, v in end.items():
#     for k1, v1, in yuce.items():
#         if k == k1:
#             precision[k] = v / v1
#             # print(k + '=', v1 / v)
# print(precision)
# print('================F1======================')
# for k, v in recall.items():
#     for k1, v1, in precision.items():
#         if k == k1:
#             f1[k] = 2 * (v1 * v) / (v1 + v)
#             # print(k + '=', v1 / v)
# print(f1)


#经过关系发现词模型后
# 测试数据各类的个数为： {'Related-SY': 76, 'Related-CH': 46, 'Related-TR': 55, 'Related-CO': 5}
# 重新匹配后正确抽取的个数为： {'Related-CH': 20, 'Related-TR': 25, 'Related-SY': 59, 'Related-CO': 1}
# 数据预测的各类的个数： {'Related-TR': 46, 'Related-CH': 31, 'Related-SY': 95, 'Related-CO': 10}
# 所以再经过BIGRU模型后的结果为：
# 测试数据各类的个数为： {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
# 正确抽取的个数为： {'Related-SY': 409+59, 'Related-CH': 196+20, 'Related-TR': 254+40, 'Related-CO': 133+2}
# 数据预测的各类的个数： {'Related-SY': 462, 'Related-TR': 357, 'Related-CH': 216, 'Related-CO': 139}
front = {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
end = {'Related-SY': 468, 'Related-CH': 216, 'Related-TR': 294, 'Related-CO': 135}
yuce = {'Related-SY': 462, 'Related-CH': 216,'Related-TR': 357 , 'Related-CO': 139}
recall = {}
precision ={}
f1 = {}
for k, v in front.items():
    for k1, v1, in end.items():
        if k == k1:
            recall[k] = v1 / v
            # print(k+'=',v1/v)
print(recall)
print('================precison=================')
for k, v in end.items():
    for k1, v1, in yuce.items():
        if k == k1:
            precision[k] = v / v1
            # print(k + '=', v1 / v)
print(precision)
print('================F1======================')
for k, v in recall.items():
    for k1, v1, in precision.items():
        if k == k1:
            f1[k] = 2 * (v1 * v) / (v1 + v)
            # print(k + '=', v1 / v)
print(f1)