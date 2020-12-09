from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from model import Model
from gevent.pywsgi import WSGIServer
import logging

app = Flask(__name__)
CORS(app)

vocab_file = r'E:\Code\Python\论文\模型对照\seq2seq-rule\data\dl-data\couplet\vocabs'
model_dir = r'E:\Code\Python\论文\模型对照\seq2seq-rule\data\dl-data\models\tf-lib\output_couplet'

m = Model(
        None, None, None, None, vocab_file,
        num_units=124, layers=4, dropout=0.2,
        batch_size=10, learning_rate=0.0001,
        output_dir=model_dir,
        restore_model=True, init_train=False, init_infer=True)


@app.route('/rule/<in_str>')
def chat_couplet(in_str):
    if len(in_str) == 0 or len(in_str) > 50:
        output = u'您的输入太长了'
    else:
        output = m.infer(' '.join(in_str))
        output = ''.join(output.split(' '))
    print(f'encoder输入：{in_str}\n'
          f'decoder结果：{output}')
    return jsonify({'decoder结果': output})


http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
