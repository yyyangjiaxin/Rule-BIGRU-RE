
from model import Model

m = Model(
        'data/dl-data/couplet/train/规则in',
        'data/dl-data/couplet/train/规则out',
        'data/dl-data/couplet/test/test规则in',
        'data/dl-data/couplet/test/test规则out',
        'data/dl-data/couplet/vocabs',
        num_units=124, layers=4, dropout=0.5,
        batch_size=10, learning_rate=0.001,
        output_dir='data/dl-data/models/tf-lib/output_couplet',
        restore_model=False)

# m.train(50000)·
m.train(5000)
