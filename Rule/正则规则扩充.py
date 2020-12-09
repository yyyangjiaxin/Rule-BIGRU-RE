# rules=[r'' + a + '.*[产生,伴有,症状,出现,表现,引起,造成,导致].*' + b,
#        r'[' + a + ',' + b + ']' + '.*症状',
#        r'' + a + '.*是.*' + b + '的原因',

#        r'' + a + '.*[检测,检查,监测,评估,显示,诊断,查明,观察].*' + b,
#        r'[' + a + ',' + b + ']' + '.*[检查,检测]',
#        r''+'.*检查.*'+b

#        r'' + a + '.*[减轻,缓解,抑制,治疗,预防,提高,影响,诱发].*' + b,
#        r'.*采用.*'+'[' + a + ',' + b + ']' ,

#        r'' + a + '.*[并发].*' + b,
#        r'[' + a + ',' + b + ']' + '.*并发症']

##将正则规则进行扩充，并生成规则对.txt文件
import  synonyms
import re,os,sys,datetime
sy = ['产生','伴有','症状','出现','表现','引起','造成','导致','原因']
ch = ['检测','检查','监测','评估','显示','诊断','查明','观察']
tr = ['减轻','缓解','抑制','治疗','预防','提高','影响','诱发','采用']
co = ['并发','并发症']
# sy_cilin = {}
# ch_cilin = {}
# tr_cilin = {}
# co_cilin = {}
all_word = []
all_word.append(sy)
all_word.append(ch)
all_word.append(tr)
all_word.append(co)
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
save_dir = os.path.join('./log/正则规则扩充运行log', mulu)
if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
make_print_to_file(save_dir)

#规则组合
#将近义词和上位词作为下联，同义词作为上联，计算一共有多少规则对

# 修改:不能直接进行笛卡尔积,对于每一个词及其同义词 分别查找近义词和上位词作为下联.

# def rule(k,jin,tong,shangwei):
#     up_num = 1  #上联规则数量
#     down_num = 0 #下联规则数量
#     up_num = up_num + len(tong)
#     down_num = down_num +len(jin)+len(shangwei)
#     #规则对写入文件保存
#     up = [k]+tong
#     down = jin + shangwei
#     print('%s的上联词语有%s,下联词语有%s'%(k,up,down))
#     with open('规则对.txt','a',encoding='utf-8') as f1:
#         for i in up:
#             if not '\u4e00' <= i <= '\u9fa5':  #不是中文
#                 continue
#             else:
#                 for j in down:
#                     if not '\u4e00' <= j <= '\u9fa5':
#                         continue
#                     else:
#                         s = 'a.*'+ i + '.*b'+" "+ 'a.*'+j +'.*b'
#                         f1.writelines(s+'\n')
#                         #其余形式规则的扩充
#                         if i =='症状':  # r'[' + a + ',' + b + ']' + '.*症状',
#                             ss1 = 'a.*'+ i + " " + 'a.*' + j
#                             ss2 = 'b.*'+ i + " " + 'b.*' + j
#                             f1.write(ss1+'\n')
#                             f1.write(ss2 + '\n')
#                         if i == '原因':   #r'' + a + '.*是.*' + b + '的原因',
#                             ss1 = 'a.*是.*b的'+ i +' '+'a.*是.*b的'+j
#                             f1.write(ss1+'\n')
#                         if i == '检查' or i =='检测': #r'[' + a + ',' + b + ']' + '.*[检查,检测]',
#                             ss1 = 'a.*' + i +' ' +'a.*' + j
#                             ss2 = 'b.*' + i +' ' +'b.*' + j
#                             f1.write(ss1 + '\n')
#                             f1.write(ss2 + '\n')
#                         if i == '检查':  #r''+'.*检查.*'+b
#                             ss1 = '.*' + i +'.*b' + ' ' + '.*' + j +'.*b'
#                             f1.write(ss1 + '\n')
#                         if i == '采用':    # r'.*采用.*' + '[' + a + ',' + b + ']' + '.*',
#                             ss1 = '.*'+ i +'.*a.*'+ ' ' +'.*'+ j +'.*a.*'
#                             ss2 = '.*'+ i +'.*b.*'+ ' ' +'.*'+ j +'.*b.*'
#                             f1.write(ss1 + '\n')
#                             f1.write(ss2 + '\n')
#                         if i == '并发症': #   r'[' + a + ',' + b + ']' + '.*并发症']
#                             ss1 = 'a.*'+i +' '+ 'a.*'+j
#                             ss2 = 'b.*'+i +' '+ 'b.*'+j
#                             f1.write(ss1 + '\n')
#                             f1.write(ss2 + '\n')
#
#     f1.close()
#     #每个词进行笛卡尔积后的规则对数量
#     return up_num *down_num

#找每个词的同义词和上位词
# def word(k,v):
#     tong = []
#     shangwei = []
#     for i in v:
#         if '=' in i[0]:
#             w = i[1:]
#             w.remove(k)
#             tong = tong + w
#         if '#' in i[0]:
#             w = i[1:]
#             w.remove(k)
#             shangwei= shangwei +w
#     jin = synonyms.nearby(k)[0]
#     jin.remove(k)
#     print('%s的近义词有：（使用synonyms包）：'%(k),jin)
#     print('%s的同义词有：%s' % (k, tong))
#     print('%s的上位词有：%s' % (k, shangwei))
#     num = rule(k, jin, tong, shangwei)
#     print('以%s+同义词作为上联，近义词和上位词作为下联，进行笛卡尔积后的规则对数量为：%s' % (k, num))
#     print('====================')
#     return num


#找每个词的同义词 上位词
#在词林表中   “#”代表“不等”、“同类”，属于相关词语,范围较宽泛，可以视为上位词
#每个词的同义词
def tong_word(k,v):
    tong = [k]
    for i in v:
        if '=' in i[0]:
            tong = tong + i[1:]
    #去除重复词 和不是中文的词
    tong = list(set(tong))
    my_re = re.compile(r'[A-Za-z]', re.S)
    t = []
    for w in tong:
        res = re.findall(my_re,w)
        if all(map(lambda c: '\u4e00' <= c <= '\u9fa5', w)) == True or len(res)==0: #为全中文
            t.append(w)
    return t

def jin_shangwei_word(up,lines):
    down = []
    for line in lines:
        line = line.strip().split()
        if up in line and '#' in line[0]:
            down  = down + line[1:]
    print('%s上位词有%s'%(up,down))
    down = down + synonyms.nearby(up)[0]
    # 去除重复词 、up 、不是中文的词
    if len(down)==0:
        return down
    else:
        down = list(set(down))
        down.remove(up)
        my_re = re.compile(r'[A-Za-z]', re.S)
        d = []
        for w in down:
            res = re.findall(my_re, w)
            if all(map(lambda c: '\u4e00' <= c <= '\u9fa5', w)) == True and len(res)==0:  # 为全中文
                d.append(w)
        return d



def rule(up,down):
    #规则对写入文件保存\
    # 修改：字多的为上联 字少的为下联 由细的泛化出粗的 扩散范围条件
    with open('规则对.txt','a',encoding='utf-8') as f1:
        for j in down:
            i = up
            if len(j)>len(i):
                i,j = j,i
            s = 'a.*'+ i + '.*b'+" "+ 'a.*'+j +'.*b'
            f1.writelines(s+'\n')
            #其余形式规则的扩充
            if i =='症状' or j =='症状':  # r'[' + a + ',' + b + ']' + '.*症状',
                ss1 = 'a.*'+ i + " " + 'a.*' + j
                ss2 = 'b.*'+ i + " " + 'b.*' + j
                f1.write(ss1+'\n')
                f1.write(ss2 + '\n')
            if i == '原因' or j=='原因':   #r'' + a + '.*是.*' + b + '的原因',
                ss1 = 'a.*是.*b的'+ i +' '+'a.*是.*b的'+j
                f1.write(ss1+'\n')
            if i in ['检查','检测'] or j in ['检查','检测']: #r'[' + a + ',' + b + ']' + '.*[检查,检测]',
                ss1 = 'a.*' + i +' ' +'a.*' + j
                ss2 = 'b.*' + i +' ' +'b.*' + j
                f1.write(ss1 + '\n')
                f1.write(ss2 + '\n')
            if i == '检查' or j=='检查':  #r''+'.*检查.*'+b
                ss1 = '.*' + i +'.*b' + ' ' + '.*' + j +'.*b'
                f1.write(ss1 + '\n')
            if i == '采用' or j=='采用':    # r'.*采用.*' + '[' + a + ',' + b + ']' ,
                ss1 = '.*'+ i +'.*a.*'+ ' ' +'.*'+ j +'.*a'
                ss2 = '.*'+ i +'.*b.*'+ ' ' +'.*'+ j +'.*b'
                f1.write(ss1 + '\n')
                f1.write(ss2 + '\n')
            if i == '并发症' or j=='并发症': #   r'[' + a + ',' + b + ']' + '.*并发症']
                ss1 = 'a.*'+i +' '+ 'a.*'+j
                ss2 = 'b.*'+i +' '+ 'b.*'+j
                f1.write(ss1 + '\n')
                f1.write(ss2 + '\n')

    f1.close()

if os.path.exists('规则对.txt'):
    os.remove('规则对.txt')
with open('./data/哈工大词林表.txt') as f:
    lines = f.readlines()
    for c in all_word:
        print('-------------------------------------------------------------')
        print(c)
        cilin = {}
        for i in c:
            for line in lines:
                line = line.strip().split()
                if i in line:
                    cilin[i] = cilin.get(i,[])+[line]
        print('词林：',cilin)
        # 1 为每个词求其同义词
        for k,v in cilin.items():
            print(k,v)
            tong = tong_word(k,v)
            print('%s的同义词有：%s'%(k,tong))
            # 2 分别为这个词和其同义词，找近义词和上位词
            for up in tong:
                down = jin_shangwei_word(up,lines)
                # down = jin_shangwei_word(up,cilin)
                print('%s的下联词有：%s'%(up,down))
                # 3 为每个词和其同义词建立规则（近义词和上位词为下联）,前提是该词有下联
                if len(down)!=0:
                    rule(up,down)
    # word(sy_cilin)
    # # # n = 0
    # # for k ,v in sy_cilin.items():
    # #     print(k,v)
    # #     # n = n + word(k,v)
    # # # print('相关症状规则对总数为',n)

    # for i in ch:
    #     for line in lines:
    #         line = line.strip().split()
    #         if i in line:
    #             ch_cilin[i] = ch_cilin.get(i, []) + [line]
    # print('-------------------------------------------------------------')
    # print('相关检查词林：')
    # n = 0
    # for k, v in ch_cilin.items():
    #     print(k, v)
    #     n = n + word(k, v)
    # print('相关检查规则对总数为', n)
    #
    # for i in tr:
    #     for line in lines:
    #         line = line.strip().split()
    #         if i in line:
    #             tr_cilin[i] = tr_cilin.get(i, []) + [line]
    # print('-------------------------------------------------------------')
    # print('相关治疗词林：')
    # n = 0
    # for k, v in tr_cilin.items():
    #     print(k, v)
    #     n = n + word(k, v)
    # print('相关治疗规则对总数为', n)
    #
    # for i in co:
    #     for line in lines:
    #         line = line.strip().split()
    #         if i in line:
    #             co_cilin[i] = co_cilin.get(i, []) + [line]
    # print('-------------------------------------------------------------')
    # print('相关并发症词林：')
    # n = 0
    # for k, v in co_cilin.items():
    #     print(k, v)
    #     n = n +word(k, v)
    # print('相关并发症规则对总数为', n)
    # f.close()
    #

