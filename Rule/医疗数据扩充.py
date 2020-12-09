# rules = ['a.*产生.*b', 'a.*发生.*b', 'a.*伴有.*b', 'a.*伴随.*b', 'a.*症状.*b', 'a.*病病.*b', 'a.*出现.*b', 'a.*消失.*b', 'a.*引起.*b',
#          'a.*引发.*b', 'a.*导致.*b', 'a.*造成.*b', 'a.*症状', 'a.*病病', 'b.*症状', 'b.*病病', 'a.*是.*b的原因', 'a.*夹查.*b',
#          'a.*检测.*b', 'a.*鉴验.*b', 'a.*评估.*b', 'a.*依.**b', 'a.*检查.*b', 'a.*检测.*b', 'a.*显示.*b', 'a.*可见.*b', 'a.*诊断.*b',
#          'a.*确诊.*b', 'a.*查明.*b', 'a.*密.*b', 'a.*观察.*b', 'a.*量测.*b', '.*检查.*b', '.*检测.*b', 'a.*检查', 'a.*检测', 'a.*检测',
#          'a.*鉴验', 'b.*检查', 'b.*检测', 'b.*检测', 'b.*鉴别',
#          'a.*减轻.*b', 'a.*减少.*b', 'a.*缓解.*b', 'a.*消除.*b', 'a.*抑制.*b', 'a.*降低.*b', 'a.*治疗.*b', 'a.*手术.*b', 'a.*预防.*b',
#          'a.*改善.*b', 'a.*提高.*b', 'a.*增加.*b', 'a.*诱发.*b', 'a.*诱导.*b', '.*采用.*a.*', '.*可用.*a', '.*采用.*b.*', '.*可用.*b',
#          'a.*并发.*b', 'a.*诱发.*b', 'a.*并发症', 'a.*伴发', 'b.*并发症', 'b.*伴发']

# 发生、伴随、消失、引发、造成
# 鉴验、检测、可见、确诊、密、量测、鉴别 !
# 减少、消除、降低、手术、改善、增加、诱导、可用 !
# 诱发、伴发 !

import json,datetime,os,sys
dir = 'F:\科研论文\实验数据\medical.json'
sy_word = ['伴随','消失','造成','引发']
ch_word = ['鉴验','检测','可见','确诊','量测','鉴别']
tr_word = ['减少','消除','降低','手术','改善','增加','诱导','可用']
co_word = ['诱发','伴发']

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
save_dir = os.path.join('./log/医疗数据扩充/log', mulu)
if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
make_print_to_file(save_dir)

with open(dir,'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = json.loads(line)
        for k,v in line.items():
            for sy_w in sy_word:
                if sy_w in v:
                    print('sy关键词:',sy_w)
                    print('name是:',line['name'])
                    print('所在句子:',v)
                    print('====================================')
            for ch_w in ch_word:
                if ch_w in v:
                    print('ch关键词:',ch_w)
                    print('name是:', line['name'])
                    print('所在句子:', v)
                    print('====================================')
            for tr_w in tr_word:
                if tr_w in v:
                    print('tr关键词:',tr_w)
                    print('name是:', line['name'])
                    print('所在句子:', v)
                    print('====================================')
            for co_w in co_word:
                if co_w in v:
                    print('co关键词:',co_w)
                    print('name是:', line['name'])
                    print('所在句子:', v)
                    print('====================================')