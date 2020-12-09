#症状SY  re.compile(r'' + a + '.*[产生，伴有，症状，出现，表现，引起,造成，导致].*' + b)
# 检查CH re.compile(r'' + a + '.*[检测,检查,监测,评估,显示,诊断,查明,观察].*' + b)
# 治疗TR re.compile(r'' + a + '.*[减轻,缓解,抑制,治疗,预防,修复,影响,诱发].*' + b)
# 并发症CO  re.compile(r'' + a + '.*[并发].*' + b)
import re
def Find(p,s,match_num):
    print("find",p)
    if '[' in p and ']' in p:  #查找的不是实体a或b,如[产生，伴有，症状，出现，表现，引起,造成，导致]
        # 此处的[产生，伴有，症状，出现，表现，引起,造成，导致]是str类型
        word = p[1:len(p)-1].split(',')
        print('word',word)
        for w in word:
            if s.find(w) != -1:
                match_num = match_num +1
                print('找到',p,w)
                break
    else: #find实体 a或b
        if s.find(p)!= -1:
            match_num = match_num +1
            print("找到",p)
    return match_num

def And_Ordered(f,s,and_num,match_num):
    distance = [] #存储各个find匹配到的位置
    print('and_ordered',f)
    print('and_ordered模块个数',and_num)

    for i in f:
        t = []  #
        if '[' in i and ']' in i: #[产生，伴有，症状，出现，表现，引起,造成，导致]中每个能匹配到的值的位置，分别计算和其余的find下标是否是有序的
            word = i[1:len(i)-1].split(',')
            for w in word:
                j = s.find(w)
                if j !=-1:
                    t.append(j)
            if len(t)==0:  #全部没匹配到，位置下标置为-1，取代列表表示
                distance.append(-1)
            else:
                distance.append(t)
        else:
            j = s.find(i)
            if j != -1:
                distance.append(j)
            else:
                distance.append(-1)
    print('And_Ordered模块位置索引结果：',distance)

    #所有distance 全排列组合情况.如[1,[2,3,4],5] 结果为 [[1,2,5],[1,3,5],[1,4,5]]
    d = [[]]
    t = []
    for i in range(len(distance)):
        if type(distance[i]) == int:
            for di in d:
                di.append(distance[i])
        else:
            dd = []
            # print('下标', distance[i])
            add_xiabiao = distance[i]
            for di in d:
                # print('di', di)
                for j in add_xiabiao:
                    t = di + [j]
                    dd.append(t)
            d = dd
    print('索引全部组合情况',d)
    #对于所有组合，只要 匹配有序（即右边的索引大于左边的索引,且均不为-1）
    # 当前规则匹配成功 就加1 返回整个索引组合中匹配成功最大的值 赋值给match_num
    max_num =0
    for dis in d:
        now_num = 0
        for j in range(len(dis)-1):
            if dis[j+1] - dis[j] >0 and dis[j+1]!=-1 and dis[j]!=-1:
                now_num = now_num+1
        max_num = max(max_num,now_num)
        if max_num == and_num:
            break
    match_num = match_num +max_num
    return match_num



def score(a,b,s,rules):
    rule_i = 0 # 每条规则的下标值，用来指引每条规则的模块个数
    match_score = [] #存储匹配到每条规则的分数
    for rule in rules:  #每条规则
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
        # while and_num>0:
        #     And_Ordered(f,s,match_num)
        #     and_num = and_num -1
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
a = '1'
b = '2'
rules=[r'' + a + '.*[产生,伴有,症状,出现,表现,引起,造成,导致].*' + b,
       r'[' + a + ',' + b + ']' + '.*症状',
       r'' + a + '.*是.*' + b + '的原因',
       r'' + a + '.*[检测,检查,监测,评估,显示,诊断,查明,观察].*' + b,
       r'.*检查.*' +b,
       r'[' + a + ',' + b + ']' + '.*[检查,检测]',
       r'' + a + '.*[减轻,缓解,抑制,治疗,预防,修复,影响,诱发].*' + b,
       r'.*采用.*'+'[' + a + ',' + b + ']' + '.*',
       r'' + a + '.*[并发].*' + b,
       r'[' + a + ',' + b + ']' + '.*并发症']

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

with open (dir,encoding='utf-8') as f:
    #按顺序排列，类别为key，该类别的最后一条规则的序号为value
    leibie ={'Related-SY':[1,2,3],'Related-CH':[4,5,6],'Related-TR':[7,8],'Related-CO':[9,10]}
    correct = {}
    f1 = f
    lines = f.readlines()
    # 统计每个类别包含的句子总数
    leibie_num = total(lines)
    print('每个类别包含的句子总数', leibie_num)

    for line in lines:
        a, b, rel, s = line.strip().split()
        num = num + 1
        rules = [r'' + a + '.*[产生,伴有,症状,出现,表现,引起,造成,导致].*' + b,
                 r'[' + a + ',' + b + ']' + '.*症状',
                 r'' + a + '.*是.*' + b + '的原因',
                 r'' + a + '.*[检测,检查,监测,评估,显示,诊断,查明,观察].*' + b,
                 r'.*检查.*' + b,
                 r'[' + a + ',' + b + ']' + '.*[检查,检测]',
                 r'' + a + '.*[减轻,缓解,抑制,治疗,预防,修复,影响,诱发].*' + b,
                 r'.*采用.*' + '[' + a + ',' + b + ']' + '.*',
                 r'' + a + '.*[并发].*' + b,
                 r'[' + a + ',' + b + ']' + '.*并发症']
        print('句子%d：'%(num),a,b,rel,s)
        # 每个句子匹配每个规则，计算匹配到每个规则的分数，输出分数最高的规则
        matched_s = score(a,b,s,rules)
        print('句子%d对于每个规则的匹配分数'%(num),matched_s)

        #取最高的分数，代表句子最匹配第几条规则
        max_score = max(matched_s)
        max_rule_i = matched_s.index(max_score)
        print('最匹配第%d条规则'%(max_rule_i+1))

        #该条规则是哪个类别
        for k,v in leibie.items():
            if max_rule_i+1 in v:
                print('句子%d原定类别为：'%(num),rel)
                rule_rel = k
                print('句子%d的规则分类的类别为：'%(num),rule_rel)
        print('====================================================================================')
        if rule_rel == rel:
            correct[rule_rel] = correct.get(rule_rel,0)+1
print('每个类别包含的句子总数', leibie_num)
print('匹配结果：',correct)
# 每个类别包含的句子总数 {'Related-SY': 472, 'Related-CH': 224, 'Related-TR': 272, 'Related-CO': 126}
# 匹配结果： {'Related-SY': 414, 'Related-CH': 179, 'Related-TR': 219, 'Related-CO': 92}