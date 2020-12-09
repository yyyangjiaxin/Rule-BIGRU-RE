#获取Find模块和And模块 进行训练所需要的数据
#即使用2(2)中的符号算法，计算每个句子对应35条初始规则，所得到的Find分数和And_ordered分数
#生成 规则 句子 分数 的格式，以供bert模型进行训练打分机制

import re,os
def Find(p,s,find_num):
    print("find",p)
    if s.find(p)!= -1:
        find_num = find_num +1
        print("找到",p)
    return find_num

def And_Ordered(f,s,and_num):
    distance = [] #存储各个find匹配到的位置
    print('and_ordered',f)
    for i in f:
        j = s.find(i)
        if j != -1:
            distance.append(j)
        else:
            distance.append(-1)
    print('And_Ordered模块位置索引结果：',distance)
    #每个索引两两有序 且都是找到的 即不是-1
    for i in range(len(distance)-1):
        if distance[i+1] - distance[i]>0 and distance[i+1]!=-1 and distance[i]!= -1:
            and_num= and_num +1
    return and_num

def data(a,b,s,rules):
    rule_i = 0 # 每条规则的下标值
    # match_score = [] #存储匹配到每条规则的分数
    for rule in rules:  #每条规则
        # print('rule%d为：'%(rule_i+1),rule)
        # find_num = mokuai_num[rule_i][0] #Find模块个数
        # and_num= mokuai_num[rule_i][1] #And_Ordered模块个数
        # all_num = find_num + and_num  #所有模块个数
        # match_num = 0
        #匹配句子，计算每个Find模块和And_Ordered模块能匹配到的个数，匹配到+1，未匹配到+0
        # 每条规则的匹配分数 = pipei_num / all_num

        #匹配find模块
        f = rule.split(".*") #需要Find的所有值
        find_num = and_num = 0
        for p in f:
            find_num = Find(p,s,find_num)
        print('截至Find模块,匹配到个数为：',find_num)
        f1.write(rule+' '+ s + " "+ str(find_num)+ "\n")

        #匹配 And_Ordered模块
        and_num = And_Ordered(f, s, and_num)
        print('截至And_Ordered模块，匹配到个数为：', and_num)
        f2.write(rule + ' '+ s +' '+ str(and_num)+'\n')
        rule_i = rule_i + 1


dir = './data/all_data.txt'
num = 0  #句子顺序
os.remove('./data/find_data')
os.remove('./data/and_data')
f1 = open('./data/find_data','a',encoding='utf-8')
f2 = open('./data/and_data','a',encoding='utf-8')
with open (dir,encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        a, b, rel, s = line.strip().split()
        num = num + 1
        rules = [r'' + a + '.*产生.*' + b,r'' + a + '.*发生.*' + b,
                 r'' + a + '.*伴有.*' + b,r'' + a + '.*伴随.*' + b,
                 r'' + a + '.*症状.*' + b,r'' + a + '.*病病.*' + b,
                 r'' + a + '.*出现.*' + b,r'' + a + '.*消失.*' + b,
                 r'' + a + '.*引起.*' + b,r'' + a + '.*引发.*' + b,
                 r'' + a + '.*导致.*' + b,r'' + a + '.*造成.*' + b,
                 r'' + a + '.*症状',r'' + a + '.*病病',
                 r'' + b + '.*症状',r'' + b + '.*病病',
                 r'' + a + '.*是.*' + b + '的原因',r'' + a + '.*夹查.*' + b ,
                 r'' + a + '.*检测.*' + b,r'' + a + '.*鉴验.*' + b,
                 r'' + a + '.*评估.*' + b,r'' + a + '.*依.**' + b,
                 r'' + a + '.*检查.*' + b,r'' + a + '.*检测.*' + b,
                 r'' + a + '.*显示.*' + b,r'' + a + '.*可见.*' + b,
                 r'' + a + '.*诊断.*' + b,r'' + a + '.*确诊.*' + b,
                 r'' + a + '.*查明.*' + b,r'' + a + '.*密.*' + b,
                 r'' + a + '.*观察.*' + b,r'' + a + '.*量测.*' + b,
                 r'.*检查.*' + b,r'.*检测.*' + b,
                 r'' + a + '.*检查',r'' + a + '.*检测',
                 r'' + a + '.*检测',r'' + a + '.*鉴验',
                 r'' + b + '.*检查',r'' + b + '.*检测',
                 r'' + b + '.*检测',r'' + b + '.*鉴别',
                 r'' + a + '.*减轻.*' + b,r'' + a + '.*减少.*' + b,
                 r'' + a + '.*缓解.*' + b,r'' + a + '.*消除.*' + b,
                 r'' + a + '.*抑制.*' + b,r'' + a + '.*降低.*' + b,
                 r'' + a + '.*治疗.*' + b,r'' + a + '.*手术.*' + b,
                 r'' + a + '.*预防.*' + b,r'' + a + '.*改善.*' + b,
                 r'' + a + '.*提高.*' + b,r'' + a + '.*增加.*' + b,
                 r'' + a + '.*诱发.*' + b,r'' + a + '.*诱导.*' + b,
                 r'.*采用.*' + '' + a,r'.*可用.*' + '' + a,
                 r'.*采用.*' + '' + b,r'.*可用.*' + '' + b,
                 r'' + a + '.*并发.*' + b,r'' + a + '.*诱发.*' + b,
                 r'' + a + '.*并发症',r'' + a + '.*伴发',
                 r'' + b + '.*并发症',r'' + b + '.*伴发']
        print('句子%d：'%(num),a,b,rel,s)
        # 每个句子匹配每个规则，计算匹配到每个规则的分数，输出分数最高的规则
        data(a,b,s,rules)
f1.close()
f2.close()
