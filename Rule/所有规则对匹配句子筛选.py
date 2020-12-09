#将规则对.txt匹配所有句子，过滤掉没有匹配到句子的规则对，存储为规则对2.txt
import os,re,sys,datetime
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
save_dir = os.path.join('./log/所有规则对匹配句子筛选', mulu)
if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
make_print_to_file(save_dir)
# def pipei(rule,sentences):
#     flag =0
#     print('开始匹配所有句子')
#     for r in rule:
#         print('规则%s' % (r))
#         for sen in sentences:
#             pipei_rule = r
#             a,b,rel,s = sen.strip().split()
#             pipei_rule = pipei_rule.replace('a',a)
#             pipei_rule = pipei_rule.replace('b',b)
#             rr = re.compile(pipei_rule)
#             res = rr.findall(s)
#             if len(res)!= 0:
#                 flag = flag+1 #匹配到句子
#                 print('匹配到句子%s,flag=%d'%(s,flag))
#                 break
#     if flag == 2:
#         print('都匹配到了句子，写入规则对2')
#         f2.write(' '.join( str(i) for i in rule)+'\n')
#     else:
#         print('删除规则对',rule)
#         d.append(rule)
def pipei(rule,sentences):
    flag =0
    print('开始匹配所有句子')
    for r in rule:
        print('规则%s' % (r))
        for sen in sentences:
            pipei_rule = r
            a,b,rel,s = sen.strip().split()
            pipei_rule = pipei_rule.replace('a','')
            pipei_rule = pipei_rule.replace('b','')
            pipei_rule = pipei_rule.replace('.*', '')
            rr = re.compile(pipei_rule)
            res = rr.findall(s)
            if len(res)!= 0:
                flag = flag+1 #匹配到句子
                print('匹配到句子%s,flag=%d'%(s,flag),pipei_rule)
                break
    if flag == 2:
        print('都匹配到了句子，写入规则对2')
        f2.write(' '.join( str(i) for i in rule)+'\n')
    else:
        print('删除规则对',rule)
        d.append(rule)

f1 = open('./data/all_data.txt',encoding='utf-8')
sentences = f1.readlines()
if os.path.exists('./规则对2.txt'):
    os.remove('./规则对2.txt')
f2 = open('./规则对2.txt','a',encoding='utf-8')
d = []  # 存储过滤掉的规则对
i = 1
# 为每一个规则对 匹配句子，其中任一规则匹配不到句子，就删掉这条规则对
with open('./规则对_.txt',encoding='utf-8') as f:
    rules = f.readlines()
    for rule in rules:
        print('==========规则对%d为:'%(i),rule)
        rule= rule.strip().split(' ')
        pipei(rule,sentences)
        i = i +1
print(d)
print(len(d))