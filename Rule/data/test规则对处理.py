#将test规则对中的规则对处理成 seq2seq接受的格式
import os
os.remove('./test规则in')
os.remove('./test规则out')
f1 = open('./test规则in','a',encoding='utf-8')
f2 = open('./test规则out','a',encoding='utf-8')
with open('./test规则对',encoding='utf-8') as f3:
    lines = f3.readlines()
    for line in lines:
        up, down = line.strip().split()
        up = ' '.join(up)
        down = ' '.join(down)
        f1.write(up+'\n')
        f2.write(down +'\n')
f1.close()
f2.close()