# seq2seq model

https://blog.csdn.net/m0_38106923/article/details/86307434?utm_source=app

https://github.com/wb14123/seq2seq-couplet

数据预处理代码：`reader.py`，里面可以自定义encoder的向量长度

训练数据和测试数据放在`data/dl-data/couplet`目录下，字表如果用自己的，则要在开头加入`<s></s>`,分别表示decoder的开始和结束符

数据字符用空格分开，在一起的字符为一个整体进行词嵌入

`rule_train.py`开始训练，里面的各种参数可以调整

predict文件预测的时候，路径要改一下，用相对路径一直有点问题，所以用绝对路径了

运用于自己数据上：
迭代次数为5000时，在3000次时，score为60.67最高