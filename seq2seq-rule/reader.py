from queue import Queue
from threading import Thread
import random

"""
数据预处理，把数据集转化为数字与字符对照的字典，
然后根据数字与字符对照的字典进行encoder及decoder的向量
"""


# 长度不够则在后面进行补0,丢入的batch_size中最长的句子长度为max_len，对于不足max_len的句子后面补0
def padding_seq(seq):
    results = []
    max_len = 0
    for s in seq:
        if max_len < len(s):
            max_len = len(s)
    for i in range(0, len(seq)):
        l = max_len - len(seq[i])
        results.append(seq[i] + [0 for j in range(l)])
    return results


# 需要进行encoder的字词  返回每个词的索引值
def encode_text(words, vocab_indices):
    return [vocab_indices[word] for word in words if word in vocab_indices]


def decode_text(labels, vocabs, end_token='</s>'):
    results = []
    for idx in labels:
        word = vocabs[idx]
        if word == end_token:
            return ' '.join(results)
        results.append(word)
    return ' '.join(results)


# 读整个字典
def read_vocab(vocab_file):
    print('开始运行read_vocab，读词典=========================')
    f = open(vocab_file, 'rb')
    vocabs = [line.decode('utf8')[:-1] for line in f]
    f.close()
    return vocabs


# encoder向量的最长长度为50，不够的在后面进行补0操作
class SeqReader():
    def __init__(self, input_file, target_file, vocab_file, batch_size,
                 queue_size=2048, worker_size=2, end_token='</s>',
                 padding=True, max_len=50):  #max_len 句子最长不超过50
        print('开始运行SeqReader的初始化============================')
        self.input_file = input_file
        self.target_file = target_file
        self.end_token = end_token
        self.batch_size = batch_size
        self.padding = padding
        self.max_len = max_len
        # self.vocabs = read_vocab(vocab_file) + [end_token]
        self.vocabs = read_vocab(vocab_file)  #self.vocabs存储的是vocabs文件中所有的词，type是list
        self.vocab_indices = dict((c, i) for i, c in enumerate(self.vocabs)) #以字典形式表示每个字和其索引。key为词，value为索引值
        self.data_queue = Queue(queue_size)
        self.worker_size = worker_size
        with open(self.input_file, encoding='utf-8') as f:
            for i, l in enumerate(f):
                pass
            f.close()
            self.single_lines = i + 1  #存储一共有多少条数据
        self.data_size = int(self.single_lines / batch_size) #data_size表示需要多少个iterations才能完成一次epoch
        self.data_pos = 0
        self._init_reader()
        print('结束运行SeqReader的初始化============================')

    def start(self):
        return

    '''
        for i in range(self.worker_size):
            t = Thread(target=self._init_reader())
            t.daemon = True
            t.start()
    '''

    def read_single_data(self):
        if self.data_pos >= len(self.data):
            random.shuffle(self.data)  #将列表元素打乱
            self.data_pos = 0
        result = self.data[self.data_pos]
        self.data_pos += 1
        return result

    def read(self):
        while True:
            batch = {'in_seq': [],
                     'in_seq_len': [],
                     'target_seq': [],
                     'target_seq_len': []}
            for i in range(0, self.batch_size):
                item = self.read_single_data()
                batch['in_seq'].append(item['in_seq'])
                batch['in_seq_len'].append(item['in_seq_len'])
                batch['target_seq'].append(item['target_seq'])
                batch['target_seq_len'].append(item['target_seq_len'])
            if self.padding:
                batch['in_seq'] = padding_seq(batch['in_seq'])
                batch['target_seq'] = padding_seq(batch['target_seq'])
            yield batch

    # 将输入输出进行编码
    def _init_reader(self):
        print('开始运行_init_reader，将输入输出进行编码==========================')
        self.data = []  #保存所有的规则对序列和长度
        input_f = open(self.input_file, 'rb')
        target_f = open(self.target_file, 'rb')
        for input_line in input_f:
            input_line = input_line.decode('utf-8')[:-2]
            target_line = target_f.readline().decode('utf-8')[:-2]
            input_words = [x for x in input_line.split(' ') if x != '']
            #输入：输入句子最长不超过50，超过部分去掉，在句子最后加上结束符</s>
            if len(input_words) >= self.max_len:
                input_words = input_words[:self.max_len - 1]
            input_words.append(self.end_token)
            # 输出：输出句子最长不超过50，超过部分去掉，在句子前面加上开始符<s>,在最后加上结束符</s>
            target_words = [x for x in target_line.split(' ') if x != '']
            if len(target_words) >= self.max_len:
                target_words = target_words[:self.max_len - 1]
            target_words = ['<s>', ] + target_words
            target_words.append(self.end_token)
            # print('输入：',input_words) 如输入： ['晚', '风', '摇', '树', '树', '还', '挺', '</s>']
            # print('输出target',target_words) 如输出target ['<s>', '晨', '露', '润', '花', '花', '更', '红', '</s>']
            #编码输入和输出，结果为 每个词的索引值组成的列表
            in_seq = encode_text(input_words, self.vocab_indices)
            target_seq = encode_text(target_words, self.vocab_indices)
            self.data.append({
                'in_seq': in_seq,
                'in_seq_len': len(in_seq),
                'target_seq': target_seq,
                'target_seq_len': len(target_seq) - 1
            })
        input_f.close()
        target_f.close()
        self.data_pos = len(self.data) #保存一共有多少条规则对
        print('结束运行_init_reader==========================')
