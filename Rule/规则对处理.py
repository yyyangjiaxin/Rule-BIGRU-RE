# 第一步：将规则对.txt中的数据分开，处理为seq2seq模型接受的格式，并分别写入规则in,和规则out
import os
os.remove('./data/规则in')
os.remove('./data/规则out')
f1 = open('./data/规则in','a',encoding='utf-8')
f2 = open('./data/规则out','a',encoding='utf-8')
with open('./规则对2.txt',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        up,down = line.strip().split()
        up = ' '.join(up)
        down = ' '.join(down)
        f1.write(up+'\n')
        f2.write(down+'\n')
f1.close()
f2.close()


# # 这步取消!!!
# 第二步：处理获得seq2seq中test集需要的 test规则in和test规则out  (取每个不重复上联和其对应的下联)
# import os
# os.remove('./data/test规则in')
# os.remove('./data/test规则out')
# f1 = open('./data/test规则in','a',encoding='utf-8')
# f2 = open('./data/test规则out','a',encoding='utf-8')
# with open('./data/规则in',encoding='utf-8') as f3:
#     lines = f3.readlines()
#     l1 = []
#     for line in lines:
#         line = line.strip()
#         l1.append(line)
# with open('./data/规则out',encoding='utf-8') as f4:
#     lines = f4.readlines()
#     l2 = []
#     for line in lines:
#         line = line.strip()
#         l2.append(line)
# l = []
# for index,item in enumerate(l1):
#     if item not in l:
#         l.append(item)
#         up = item
#         down = l2[index]
#         f1.write(up+'\n')
#         f2.write(down+'\n')
# f1.close()
# f2.close()