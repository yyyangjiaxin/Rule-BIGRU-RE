class BagOfWords(object):
    def __init__(self, corpus=[]):
        # 统计词频
        word_counter = {}
        for sentence in corpus:
            for item in sentence.split():
                if item in word_counter.keys():
                    word_counter[item] += 1
                else:
                    word_counter[item] = 1
        print('词频：',word_counter)
        # 按词频排序,以字典的value值降序排序,返回结果为key
        word_counter_sort = sorted(word_counter, key=word_counter.__getitem__, reverse=True)
        print('排序后词频',word_counter_sort)
        # 词典
        self.vocab = set(word_counter_sort)
        # 创建词和索引的映射
        self.stoi = {}
        self.itos = {}
        for index, word in enumerate(word_counter_sort):
            self.stoi[word] = index
            self.itos[index + 1] = word

    def sentence_encoder(self, sentence):
        result = [0] * len(self.vocab)
        for item in sentence.split():
            result[self.stoi[item]] += 1
        return result

if __name__ == '__main__':
    corpus = [
        'Jane wants to go to Shenzhen',
        'Bob wants to go to Shanghai'
    ]
    bow = BagOfWords(corpus)
    print('词索引：')
    print(bow.stoi)
    # 如：to的索引位置在词索引中是0，出现次数是2，所以向量中第一个位置的值为2
    print('{} 编码：'.format(corpus[0]))
    print(bow.sentence_encoder(corpus[0]))
    print('{} 编码：'.format(corpus[1]))
    print(bow.sentence_encoder(corpus[1]))