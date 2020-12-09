# py文件：求四个类别的 规则覆盖率
# 最后结果：
# 类别 总数 覆盖数 覆盖率
# SY:  472 438 0.9279661016949152
# CH:  224 195 0.8705357142857143
# TR:  272 143 0.5257352941176471
# CO:  126 122 0.9682539682539683
import re
#四个类别句子总数，正则覆盖句子数
sy_s = sy_f = 0
ch_s = ch_f = 0
tr_s = tr_f = 0
co_s = co_f = 0

#覆盖率函数
def rate(a,b,rel,s):
    rules = []  #所有规则
    if rel == "Related-SY":
        # print(a,b,s)
        global sy_s,sy_f
        sy_s = sy_s + 1
        rules.append(re.compile(r'' + a + '.*[产生,伴有,症状,出现,表现,引起,造成,导致].*' + b))
        rules.append(re.compile(r'[' + a + ',' + b + ']' + '.*症状'))
        rules.append(re.compile(r'' + a + '.*是.*' + b + '的原因'))
        # print(sy_s)
        #匹配该类中所有规则，匹配成功就退出规则匹配，覆盖数+1
        for rule in rules:
            # rule.findall()返回结果为list,匹配成功时返回匹配结果，失败时为空list
            if len(rule.findall(s)) !=0:
                sy_f = sy_f+1
                break
    if rel == "Related-CH":
        # print(a,b,s)
        global ch_s, ch_f
        ch_s = ch_s + 1
        rules.append(re.compile(r'' + a + '.*[检测,检查,监测,评估,显示,诊断,查明,观察].*' + b))
        rules.append(re.compile(r'.*检查.*' +b))
        rules.append(re.compile(r'[' + a + ',' + b + ']' + '.*[检查,检测]'))
        # print(ch_s)
        #该类中另一个规则，检查出现在实体中
        if '检查' in a or "检查" in b:
            ch_f = ch_f + 1
            return
        # 匹配该类中所有规则，匹配成功就退出规则匹配，覆盖数+1
        for rule in rules:
            # rule.findall()返回结果为list,匹配成功时返回匹配结果，失败时为空list
            if len(rule.findall(s)) != 0:
                ch_f = ch_f + 1
                break
    if rel == "Related-TR":
        # print(a,b,s)
        global tr_s,tr_f
        tr_s = tr_s + 1
        rules.append(re.compile(r'' + a + '.*[减轻,缓解,抑制,治疗,预防,修复,影响,诱发].*' + b))
        rules.append(re.compile(r'.*采用.*'+'[' + a + ',' + b + ']' + '.*'))
        # print(tr_s)
        #匹配该类中所有规则，匹配成功就退出规则匹配，覆盖数+1
        for rule in rules:
            # rule.findall()返回结果为list,匹配成功时返回匹配结果，失败时为空list
            if len(rule.findall(s)) !=0:
                tr_f = tr_f+1
                break
    if rel == "Related-CO":
        # print(a, b, s)
        global co_s, co_f
        co_s = co_s + 1
        rules.append(re.compile(r'' + a + '.*[并发].*' + b))
        rules.append(re.compile(r'[' + a + ',' + b + ']' + '.*并发症'))
        # print(co_s)
        # 匹配该类中所有规则，匹配成功就退出规则匹配，覆盖数+1
        for rule in rules:
            # rule.findall()返回结果为list,匹配成功时返回匹配结果，失败时为空list
            if len(rule.findall(s)) != 0:
                co_f = co_f + 1
                break

dir = './data/all_data.txt'
with open(dir,encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        #每行数据 a,b,rel,s 分别表示 实体1，实体2，实体对关系，句子
        a,b,rel,s = line.strip().split()
        rate(a,b,rel,s)
    print('类别 总数 覆盖数 覆盖率')
    print('SY: ', sy_s, sy_f, sy_f/sy_s)
    print('CH: ', ch_s, ch_f, ch_f/ch_s)
    print('TR: ', tr_s, tr_f, tr_f/tr_s)
    print('CO: ', co_s, co_f, co_f/co_s)


