class And(object):
    """
    and模块， 感觉这个可以直接从seq2seq拆解的规则中得到是0还是-1
    如：
        encoder: 跟在.*后面|跟踪 @@ 事主.*跟随
        decoder:跟在 Find_Positive 后面 Find_Positive -1 And_Ordered 跟踪 Find_Positive Or 事主 Find_Negative 跟随 Find_Negative -1 And_Ordered And_Unordered Output
    decoder中以空格分开，所以-1或者0永远在And_Ordered前？
    如果为0，and_ordered前面的两个规则字符是相邻的，且是有前后顺序的
    如果为-1，and_ordered前面的两个规则字符是任意距离的，且是有前后顺序的
    """
    def __init__(self):
        pass

    def and_ordered(self, x1, x2, d):
        pass

    def and_unordered(self, x1, x2):
        pass
