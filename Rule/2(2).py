#症状SY  re.compile(r'' + a + '.*[产生，伴有，症状，出现，引起，导致].*' + b)
# 检查CH re.compile(r'' + a + '.*[检测,检查,评估,显示,诊断,查明,观察].*' + b)
# 治疗TR re.compile(r'' + a + '.*[减轻,缓解,抑制,治疗,预防,提高,影响,诱发].*' + b)
# 并发症CO  re.compile(r'' + a + '.*[并发].*' + b)
#符号算法，计算规则泛化前的分数

import datetime
import re,sys,os
def Find(p,s,match_num):
    # print("find",p)
    if s.find(p)!= -1:
        match_num = match_num +1
        # print("找到",p)
    return match_num

def And_Ordered(f,s,and_num,match_num):
    distance = [] #存储各个find匹配到的位置
    # print('and_ordered',f)
    # print('and_ordered模块个数',and_num)
    for i in f:
        j = s.find(i)
        if j != -1:
            distance.append(j)
        else:
            distance.append(-1)
    # print('And_Ordered模块位置索引结果：',distance)
    #每个索引两两有序 且都是找到的 即不是-1
    for i in range(len(distance)-1):
        if distance[i+1] - distance[i]>0 and distance[i+1]!=-1 and distance[i]!= -1:
            match_num = match_num +1
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
        match_num = And_Ordered(f, s, and_num,match_num)
        print('截至And_Ordered模块，匹配到个数为：', match_num)
        match_score.append(match_num / all_num)
        rule_i = rule_i + 1
    return match_score

#打日志文件
def make_print_to_file(path):

    class Logger(object):
        def __init__(self, filename="Default.log", path="./"):
            self.terminal = sys.stdout
            self.log = open(os.path.join(path, filename), "a", encoding='utf8', )

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass

    fileName = datetime.datetime.now().strftime('log_%Y-%m-%d_%H-%M-%S')
    sys.stdout = Logger(fileName + '.log', path=path)
    print(fileName.center(60, '*'))
mulu = datetime.datetime.now().strftime('log_%Y-%m-%d_%H-%M-%S')  #时间戳
save_dir = os.path.join('./log/2(2)运行log', mulu)
if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
make_print_to_file(save_dir)

dir = './data/all_data.txt'
num = 0  #句子顺序
#计算每条规则所需要的 Find模块个数 和 And_Ordered模块个数
mokuai_num =[]  #存储每条规则的Find模块个数和And_Ordered模块个数
                # 形如[[3,2],[2,1],..],其中下标值+1=第i条规则，
                # [0][0]=3 表示第一条规则的Find模块有3个，[0][1]=2表示第一条规则的And_Ordered模块有2个
a = '1'
b = '2'
rules = [r'' + a + '.*产生.*' + b,
                 r'' + a + '.*伴有.*' + b,
                 r'' + a + '.*症状.*' + b,
                 r'' + a + '.*出现.*' + b,
                 r'' + a + '.*引起.*' + b,
                 r'' + a + '.*导致.*' + b,
                 r'' + a + '.*症状',
                 r'' + b + '.*症状',
                 r'' + a + '.*是.*' + b + '的原因',
                 r'' + a + '.*检测.*' + b,
                 r'' + a + '.*评估.*' + b,
                 r'' + a + '.*检查.*' + b,
                 r'' + a + '.*显示.*' + b,
                 r'' + a + '.*诊断.*' + b,
                 r'' + a + '.*查明.*' + b,
                 r'' + a + '.*观察.*' + b,
                 r'.*检查.*' + b,
                 r'' + a + '.*检查',
                 r'' + a + '.*检测',
                 r'' + b + '.*检查',
                 r'' + a + '.*检测',
                 r'' + a + '.*减轻.*' + b,
                 r'' + a + '.*缓解.*' + b,
                 r'' + a + '.*抑制.*' + b,
                 r'' + a + '.*治疗.*' + b,
                 r'' + a + '.*预防.*' + b,
                 r'' + a + '.*提高.*' + b,
                 r'' + a + '.*刺激.*' + b,
                 r'.*采用.*' + '' + a ,
                 r'.*采用.*' + '' + b ,
                 r'' + a + '.*并发.*' + b,
                 r'' + a + '.*并发症',
                 r'' + b + '.*并发症']
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

with open (dir,encoding='utf-8') as f:
    #按顺序排列，类别为key，该类别的最后一条规则的序号为value，如第10条为相关症状的最后一个规则
    leibie ={'Related-SY':[1,9],'Related-CH':[10,21],'Related-TR':[22,30],'Related-CO':[31,33]}
    correct = {}
    yuce = {}
    lines = f.readlines()
    # 统计每个类别包含的句子总数
    leibie_num = total(lines)
    # print('每个类别包含的句子总数', leibie_num)

    for line in lines:
        a, b, rel, s = line.strip().split()
        num = num + 1
        rules = [r'' + a + '.*产生.*' + b,
                 r'' + a + '.*伴有.*' + b,
                 r'' + a + '.*症状.*' + b,
                 r'' + a + '.*出现.*' + b,
                 r'' + a + '.*引起.*' + b,
                 r'' + a + '.*导致.*' + b,
                 r'' + a + '.*症状',
                 r'' + b + '.*症状',
                 r'' + a + '.*是.*' + b + '的原因',
                 r'' + a + '.*检测.*' + b,
                 r'' + a + '.*评估.*' + b,
                 r'' + a + '.*检查.*' + b,
                 r'' + a + '.*显示.*' + b,
                 r'' + a + '.*诊断.*' + b,
                 r'' + a + '.*查明.*' + b,
                 r'' + a + '.*观察.*' + b,
                 r'.*检查.*' + b,
                 r'' + a + '.*检查',
                 r'' + a + '.*检测',
                 r'' + b + '.*检查',
                 r'' + a + '.*检测',
                 r'' + a + '.*减轻.*' + b,
                 r'' + a + '.*缓解.*' + b,
                 r'' + a + '.*抑制.*' + b,
                 r'' + a + '.*治疗.*' + b,
                 r'' + a + '.*预防.*' + b,
                 r'' + a + '.*提高.*' + b,
                 r'' + a + '.*刺激.*' + b,
                 r'.*采用.*' + '' + a ,
                 r'.*采用.*' + '' + b ,
                 r'' + a + '.*并发.*' + b,
                 r'' + a + '.*并发症',
                 r'' + b + '.*并发症']
        print('句子%d：'%(num),a,b,rel,s)
        # 每个句子匹配每个规则，计算匹配到每个规则的分数，输出分数最高的规则
        matched_s = score(a,b,s,rules)
        print('句子%d对于每个规则的匹配分数'%(num),matched_s)

        #取最高的分数，代表句子最匹配第几条规则
        max_score = max(matched_s)
        print('出现最高分数的次数有：', matched_s.count(max_score))
        if matched_s.count(max_score) == 1:
            max_rule_i = matched_s.index(max_score)
            print('最匹配第%d条规则' % (max_rule_i + 1))
            # 该条规则是哪个类别
            for k, v in leibie.items():
                if max_rule_i + 1 >= v[0] and max_rule_i + 1 <= v[1]:
                    print('句子%d原定类别为：' % (num), rel)
                    rule_rel = k
                    print('句子%d的规则分类的类别为：' % (num), rule_rel)
        else:  # 有多个最高分数
            # 对于每一个句子的所有规则匹配分数，可能出现多个最高分，计算各个类别最高分出现的次数，取出现最多的类别为抽取到的类别
            res = {}
            for i, s in enumerate(matched_s):
                if s == max_score:
                    for k, v in leibie.items():
                        if i + 1 >= v[0] and i + 1 <= v[1]:
                            res[k] = res.get(k, 0) + 1
            for k,v in res.items():
                for i,j in leibie.items():
                    if k==i:
                        res[k] = res[k] / (j[1]-j[0]+1)
            end = sorted(res.items(), key=lambda x: x[1], reverse=True)  # 降序排列
            print('end', end)
            print('句子%d原定类别为：' % (num), rel)
            rule_rel = end[0][0]
            print('句子%d的规则分类的类别为：' % (num), rule_rel)
        yuce[rule_rel] = yuce.get(rule_rel, 0) + 1

        print('====================================================================================')
        if rule_rel == rel:
            correct[rule_rel] = correct.get(rule_rel,0)+1
        if rule_rel!=rel and rel=='Related-TR':
            print('相关并发症抽取错误句子',s)
print('测试数据各类的个数为：', leibie_num)
print('正确抽取的个数为：', correct)
print('数据预测的各类的个数：', yuce)
recall ={}
precision = {}
f1 ={}
print('=================recall===========')
for k1,v1 in correct.items():
    for k2,v2 in leibie_num.items():
        if k1==k2:
            recall[k1] = v1/v2
            # correct[k] = v/j
print(recall)
print('================precison=================')
for k1, v1 in correct.items():
    for k3, v3, in yuce.items():
        if k1 == k3:
            precision[k1] = v1 / v3
            # print(k + '=', v1 / v)
print(precision)

print('================F1======================')
for k5,v5 in recall.items():
    for k6, v6 in precision.items():
        if k5 == k6:
            f1[k5] = 2 * ((v5 * v6) / (v5 + v6))
            # print(k + '=', v1 / v)
print(f1)

# 每个类别包含的句子总数 {'Related-SY': 472, 'Related-CH': 224, 'Related-TR': 272, 'Related-CO': 126}
# 匹配结果： {'Related-SY': 377, 'Related-CH': 179, 'Related-TR': 223, 'Related-CO': 110}
# 第一次加入数据后
# 泛化前
# 每个类别包含的句子总数 {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 299, 'Related-CO': 138}
# 匹配结果： {'Related-SY': 379, 'Related-CH': 181, 'Related-TR': 245, 'Related-CO': 119}
# 匹配结果： {'Related-SY': 0.7814432989690722, 'Related-CH': 0.7479338842975206, 'Related-TR': 0.8193979933110368, 'Related-CO': 0.8623188405797102}
# 泛化后
# 每个类别包含的句子总数 {'Related-SY': 485, 'Related-CH': 242, 'Related-TR': 299, 'Related-CO': 138}
# 匹配结果： {'Related-SY': 409, 'Related-CH': 196, 'Related-TR': 242, 'Related-CO': 133}
# 匹配结果： {'Related-SY': 0.843298969072165, 'Related-CH': 0.8099173553719008, 'Related-TR': 0.8093645484949833, 'Related-CO': 0.9637681159420289}
