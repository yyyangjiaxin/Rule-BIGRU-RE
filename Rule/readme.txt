rule_rate.py：
    1、正则匹配时出现问题“regex bad character range"，表示字符中字符的ascii不是按顺序排列的。
       如IL-1中，- 1 的ascii码比IL小，所以出现问题，-1必须放在IL前面才能正确运行匹配。
       （目前调试将所有报这个错误的句子 所处的ascii无序位置 手工改变顺序使其有序）