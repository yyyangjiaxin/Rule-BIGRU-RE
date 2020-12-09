class GetIndexInRule(object):
    """
    传入一条拆解后的规则，及规则操作符，如Find_positive，And_Ordered等，返回在拆解后的规则中的索引列表
    该操作符的前一个索引对应的字符x即为需要进行Find(x)的
    :param  decoder_rule: seq2seq拆解后的规则树
            part_of_decoder_rule： 规则树中的某一部分，如：跟在 Find_Positive   中的Find_Positive，则“跟在”在Find_Positive的前一个位置
    :returns:   index of the decoder_rule,  type: list
    """
    def __init__(self, decoder_rule):
        self.decoder_rule = decoder_rule

    def get_index2rule(self, part_of_decoder_rule):
        return [i for i, part in enumerate(self.decoder_rule) if part == part_of_decoder_rule]


class Find(object):
    score = 0
    """
    Find模块， x 为规则树中 Find_positive 或者 Find_negative所对应的规则,即操作符索引的前一个元素即为 the part of the decoder_rule
    按照规则树的顺序Find(), 找到就加分或者减分，找不到就不加分也不减分
    """
    def __init__(self, x, sentence):
        self.x = x
        self.sentence = sentence

    def find_positive(self):
        if self.x in self.sentence:
            Find.score += 1

    # 第一种减分方式：负规则存在就减一分,或者不是减一分，减别的分？
    def find_negative1(self):
        if self.x in self.sentence:
            Find.score -= 1

    # 第二种减分方式：负规则存在分数直接置为-1，全否
    def find_negative2(self):
        if self.x in self.sentence:
            Find.score = -1

    @staticmethod
    def get_score():
        return Find.score
