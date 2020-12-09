#coding=utf-8
#症状SY  re.compile(r'' + a + '.*[产生，伴有，症状，出现，表现，引起,造成，导致].*' + b)
# 检查CH re.compile(r'' + a + '.*[检测,检查,监测,评估,显示,诊断,查明,观察].*' + b)
# 治疗TR re.compile(r'' + a + '.*[减轻,缓解,抑制,治疗,预防,修复,影响,诱发].*' + b)
# 并发症CO  re.compile(r'' + a + '.*[并发].*' + b)
# 符号算法，计算规则泛化后的分数

import re,os,sys,datetime

def Find(p,s,match_num):
    print("find",p)
    if s.find(p)!= -1:
        match_num = match_num +1
        print("找到",p)
    return match_num

def And_Ordered(f,s,and_num,match_num):
    distance = [] #存储各个find匹配到的位置
    print('and_ordered',f)
    print('and_ordered模块个数',and_num)
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
            match_num = match_num +1
    return match_num

def score(a,b,s,rules):
    rule_i = 0 # 每条规则的下标值，用来指引每条规则的模块个数
    match_score = [] #存储匹配到每条规则的分数
    for rule in rules:  #每条规则
        rule = rule.replace('a',a)
        rule = rule.replace('b',b)
        print('rule%d为：'%(rule_i+1),rule)
        find_num = mokuai_num[rule_i][0] #Find模块个数
        and_num= mokuai_num[rule_i][1] #And_Ordered模块个数
        all_num = find_num + and_num  #所有模块个数
        match_num = 0
        #匹配句子，计算每个Find模块和And_Ordered模块能匹配到的个数，匹配到+1，未匹配到+0
        # 每条规则的匹配分数 = pipei_num / all_num

        #匹配find模块
        f = rule.split(".*") #需要Find的所有值
        for p in f:
            match_num = Find(p,s,match_num)
        print('截至Find模块,匹配到个数为：',match_num)

        #匹配 And_Ordered模块
        match_num = And_Ordered(f, s, and_num,match_num)
        print('截至And_Ordered模块，匹配到个数为：', match_num)
        match_score.append(match_num / all_num)
        rule_i = rule_i + 1
    return match_score


dir = './data/all_data.txt'
num = 0  #句子顺序
#计算每条规则所需要的 Find模块个数 和 And_Ordered模块个数
mokuai_num =[]  #存储每条规则的Find模块个数和And_Ordered模块个数
                # 形如[[3,2],[2,1],..],其中下标值+1=第i条规则，
                # [0][0]=3 表示第一条规则的Find模块有3个，[0][1]=2表示第一条规则的And_Ordered模块有2个

# rules = ['a.*产生.*b', 'a.*诱发.*b', 'a.*伴有.*b', 'a.*伴发.*b', 'a.*症状.*b', 'a.*病病.*b', 'a.*出现.*b', 'a.*消失.*b', 'a.*引起.*b', 'a.*引发.*b', 'a.*导致.*b', 'a.*诱发.*b', 'a.*症状', 'a.*病病', 'b.*症状', 'b.*病病', 'a.*是.*b的原因', 'a.*夹查.*b', 'a.*检测.*b', 'a.*鉴验.*b', 'a.*评估.*b', 'a.*依.**b', 'a.*检查.*b', 'a.*检测.*b', 'a.*显示.*b', 'a.*可见.*b', 'a.*诊断.*b', 'a.*确诊.*b', 'a.*查明.*b', 'a.*密.*b', 'a.*观察.*b', 'a.*量测.*b', '.*检查.*b', '.*检测.*b', 'a.*检查', 'a.*检测', 'a.*检测', 'a.*鉴验', 'b.*检查', 'b.*检测', 'b.*检测', 'b.*鉴别', 'a.*减轻.*b', 'a.*减少.*b', 'a.*缓解.*b', 'a.*消除.*b', 'a.*抑制.*b', 'a.*调节.*b', 'a.*治疗.*b', 'a.*手术.*b', 'a.*预防.*b', 'a.*防治.*b', 'a.*提高.*b', 'a.*增加.*b', 'a.*诱发.*b', 'a.*触发.*b', '.*采用.*a.*', '.*可用.*a', '.*采用.*b.*', '.*可用.*b', 'a.*并发.*b', 'a.*诱发.*b', 'a.*并发症', 'a.*伴发', 'b.*并发症', 'b.*伴发']
rules = ['a.*产生.*b', 'a.*发生.*b', 'a.*伴有.*b', 'a.*伴随.*b', 'a.*症状.*b', 'a.*病病.*b', 'a.*出现.*b', 'a.*消失.*b', 'a.*引起.*b', 'a.*引发.*b', 'a.*导致.*b', 'a.*造成.*b', 'a.*症状', 'a.*病病', 'b.*症状', 'b.*病病', 'a.*是.*b的原因', 'a.*夹查.*b',
                 'a.*检测.*b', 'a.*鉴验.*b', 'a.*评估.*b', 'a.*依.**b', 'a.*检查.*b', 'a.*检测.*b', 'a.*显示.*b', 'a.*可见.*b', 'a.*诊断.*b', 'a.*确诊.*b', 'a.*查明.*b', 'a.*密.*b', 'a.*观察.*b', 'a.*量测.*b', '.*检查.*b', '.*检测.*b', 'a.*检查', 'a.*检测', 'a.*检测', 'a.*鉴验', 'b.*检查', 'b.*检测', 'b.*检测', 'b.*鉴别',
                 'a.*减轻.*b', 'a.*减少.*b', 'a.*缓解.*b', 'a.*消除.*b', 'a.*抑制.*b', 'a.*降低.*b', 'a.*治疗.*b', 'a.*手术.*b', 'a.*预防.*b', 'a.*改善.*b', 'a.*提高.*b', 'a.*增加.*b', 'a.*刺激.*b', 'a.*诱导.*b', '.*采用.*a.*', '.*可用.*a', '.*采用.*b.*', '.*可用.*b',
                 'a.*并发.*b', 'a.*诱发.*b', 'a.*并发症', 'a.*伴发', 'b.*并发症', 'b.*伴发']
#计算每个规则需要的Find模块计算 和And模块计算的次数
for rule in rules:
    # 将规则以 .* 进行切割，切成几份就有多少个Find模块，有几个 .* 就有几个And_Ordered模块
    t = []
    find_num = len(rule.split(".*")) #Find模块个数
    t.append(find_num)
    and_num = rule.count(".*")  # And_Ordered模块个数
    t.append(and_num)
    mokuai_num.append(t)
# print(mokuai_num)

def total(lines):
    leibie_num = {}
    for line in lines:
        line = line.strip().split()
        leibie_num[line[2]] = leibie_num.get(line[2],0)+1
    return leibie_num
# sentence = []  #有多个相同最高分数的句子
# def many_leibie(sentence):
#     pass
if os.path.exists('未匹配数据.txt'):
    os.remove('未匹配数据.txt')
f1 = open('未匹配数据.txt','a',encoding='utf-8')
with open (dir,encoding='utf-8') as f:
    #按顺序排列，类别为key，该类别的最后一条规则的序号为value，如第10条为相关症状的最后一个规则
    leibie ={'Related-SY':[1,18],'Related-CH':[19,42],'Related-TR':[43,60],'Related-CO':[61,66]}
    correct = {}
    lines = f.readlines()
    # 统计每个类别包含的句子总数
    leibie_num = total(lines)
    print('每个类别包含的句子总数', leibie_num)

    for line in lines:
        a, b, rel, s = line.strip().split()
        num = num + 1
        rules = ['a.*产生.*b', 'a.*发生.*b', 'a.*伴有.*b', 'a.*伴随.*b', 'a.*症状.*b', 'a.*病病.*b', 'a.*出现.*b', 'a.*消失.*b', 'a.*引起.*b', 'a.*引发.*b', 'a.*导致.*b', 'a.*造成.*b', 'a.*症状', 'a.*病病', 'b.*症状', 'b.*病病', 'a.*是.*b的原因', 'a.*夹查.*b',
                 'a.*检测.*b', 'a.*鉴验.*b', 'a.*评估.*b', 'a.*依.**b', 'a.*检查.*b', 'a.*检测.*b', 'a.*显示.*b', 'a.*可见.*b', 'a.*诊断.*b', 'a.*确诊.*b', 'a.*查明.*b', 'a.*密.*b', 'a.*观察.*b', 'a.*量测.*b', '.*检查.*b', '.*检测.*b', 'a.*检查', 'a.*检测', 'a.*检测', 'a.*鉴验', 'b.*检查', 'b.*检测', 'b.*检测', 'b.*鉴别',
                 'a.*减轻.*b', 'a.*减少.*b', 'a.*缓解.*b', 'a.*消除.*b', 'a.*抑制.*b', 'a.*降低.*b', 'a.*治疗.*b', 'a.*手术.*b', 'a.*预防.*b', 'a.*改善.*b', 'a.*提高.*b', 'a.*增加.*b', 'a.*刺激.*b', 'a.*诱导.*b', '.*采用.*a.*', '.*可用.*a', '.*采用.*b.*', '.*可用.*b',
                 'a.*并发.*b', 'a.*诱发.*b', 'a.*并发症', 'a.*伴发', 'b.*并发症', 'b.*伴发']


        print('句子%d：'%(num),a,b,rel,s)
        # 每个句子匹配每个规则，计算匹配到每个规则的分数，输出分数最高的规则
        matched_s = score(a,b,s,rules)
        print('句子%d对于每个规则的匹配分数'%(num),matched_s)

        #取最高的分数，代表句子最匹配第几条规则
        max_score = max(matched_s)
        print('出现最高分数的次数有：',matched_s.count(max_score))
        if matched_s.count(max_score)==1:
            max_rule_i = matched_s.index(max_score)
            print('最匹配第%d条规则'%(max_rule_i+1))
            #该条规则是哪个类别
            for k,v in leibie.items():
                if max_rule_i+1 >=v[0] and max_rule_i+1 <=v[1]:
                    print('句子%d原定类别为：'%(num),rel)
                    rule_rel = k
                    print('句子%d的规则分类的类别为：'%(num),rule_rel)

        else: #有多个最高分数
            # 对于每一个句子的所有规则匹配分数，可能出现多个最高分，计算各个类别最高分出现的次数，取出现最多的类别为抽取到的类别
            # 已修改： 应是计算各个类别最高分出现次数/该类别总规则数，用分量占比来 进行最后归类
            res = {}
            for i,s in enumerate(matched_s):
                if s == max_score:
                    for k, v in leibie.items():
                        if i+1 >=v[0] and i+1 <=v[1]:
                            res[k] = res.get(k,0)+1
            for k,v in res.items():
                for i,j in leibie.items():
                    if k==i:
                        res[k] = res[k] / (j[1]-j[0]+1)
            print('res=============',res)
            end = sorted(res.items(),key = lambda x:x[1],reverse=True)  #降序排列
            print('end',end)
            rule_rel = end[0][0]
            print('句子%d原定类别为：' % (num), rel)
            print('句子%d的规则分类的类别为：' % (num), rule_rel)

        print('====================================================================================')
        if rule_rel == rel:
            correct[rule_rel] = correct.get(rule_rel,0)+1
        else:
            f1.write(line)
print('每个类别包含的句子总数', leibie_num)
print('匹配结果：',correct)
for k,v in correct.items():
    for i,j in leibie_num.items():
        if k==i:
            correct[k] = v/j
print('匹配结果：',correct)


# 修改最后归类方式后的结果：不用次数，使用比重
# 泛化前
# 匹配结果： {'Related-SY': 377, 'Related-CH': 176, 'Related-TR': 223, 'Related-CO': 119}
# 匹配结果： {'Related-SY': 0.7987, 'Related-CH': 0.7857, 'Related-TR': 0.8198, 'Related-CO': 0.9444}
# 泛化后
#匹配结果： {'Related-SY': 396, 'Related-CH': 178, 'Related-TR': 218, 'Related-CO': 121}
# 匹配结果： {'Related-SY': 0.8390, 'Related-CH': 0.7946, 'Related-TR': 0.8015, 'Related-CO': 0.9603}

# 加入数据后
# 泛化前：
# 每个类别包含的句子总数 {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
# 匹配结果： {'Related-SY': 379, 'Related-CH': 181, 'Related-TR': 241, 'Related-CO': 119}
# 匹配结果： {'Related-SY': 0.78144, 'Related-CH': 0.7479, 'Related-TR': 0.7799, 'Related-CO': 0.8623}
# 泛化后：
# 每个类别包含的句子总数 {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 309, 'Related-CO': 138}
# 匹配结果： {'Related-SY': 409, 'Related-CH': 196, 'Related-TR': 254, 'Related-CO': 133}
# 匹配结果： {'Related-SY': 0.8433, 'Related-CH': 0.8099, 'Related-TR': 0.8220, 'Related-CO': 0.9637}
