from model import Model
import logging

vocab_file = './data/dl-data/couplet/vocabs'
model_dir ='./data/dl-data/models/tf-lib/max_output'

m = Model(
        None, None, None, None, vocab_file,
        num_units=124, layers=4, dropout=1.0,
        batch_size=10, learning_rate=0.0001,
        output_dir=model_dir,
        restore_model=True, init_train=False, init_infer=True)
# while True:

rules = ['a.*产生.*b','a.*伴有.*b','a.*症状.*b','a.*出现.*b','a.*引起.*b','a.*导致.*b','a.*症状','b.*症状','a.*是.*b的原因',
         'a.*检测.*b','a.*评估.*b','a.*检查.*b','a.*显示.*b','a.*诊断.*b','a.*查明.*b','a.*观察.*b','.*检查.*b','a.*检查',
         'a.*检测','b.*检查','b.*检测',
         'a.*减轻.*b','a.*缓解.*b','a.*抑制.*b','a.*治疗.*b','a.*预防.*b','a.*提高.*b','a.*诱发.*b','.*采用.*a.*','.*采用.*b.*',
         'a.*并发.*b','a.*并发症','b.*并发症']
fanhua = []
end_rule = []
for rule in rules:
    end_rule.append(rule)
    in_str = ' '.join(rule)
    print('输入规则：',in_str)
    output = m.infer(in_str)
    print("输出规则：", output)
    end_rule.append(output.replace(' ',''))
    fanhua.append(output)
    print('=================================')
print(fanhua)
print(end_rule)
    # in_str = input('请输入需要拆解的规则,输入q结束：')
    # if in_str == 'q':
    #     break
    # elif len(in_str) == 0 or len(in_str) > 50:
    #     output = u'您的输入太长了'
    # else:
    #     output = m.infer(' '.join(in_str))
    #     # output = ''.join(output.split(' '))  # 不以空格分开
    #     print("拆解后的规则为（默认以空格分开）：\n", output)
