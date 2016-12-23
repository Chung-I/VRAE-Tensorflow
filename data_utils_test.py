import data_utils
import translate
import os

data_dir = "poems"

in_vocabulary_size = 20000
out_vocabulary_size = 20000

train_path = "{0}/l5.train.txt".format(data_dir)
dev_path = "{0}/l5.valid.txt".format(data_dir)

# Create vocabularies of the appropriate sizes.
'''in_vocab_path = os.path.join(data_dir, "vocab%d.in" % in_vocabulary_size)
out_vocab_path = os.path.join(data_dir, "vocab%d.out" % out_vocabulary_size)
data_utils.create_vocabulary(in_vocab_path, train_path + ".in", in_vocabulary_size)
data_utils.create_vocabulary(out_vocab_path, train_path + ".out", out_vocabulary_size)

in_train_ids_path = train_path + (".ids%d.in" % in_vocabulary_size)
out_train_ids_path = train_path + (".ids%d.out" % out_vocabulary_size)
data_utils.data_to_token_ids(train_path + ".in", in_train_ids_path, in_vocab_path)
data_utils.data_to_token_ids(train_path + ".out", out_train_ids_path, out_vocab_path)
prepare_poem_data(data_dir, in_vocabulary_size, out_vocabulary_size, tokenizer=None)'''
in_train, out_train, in_dev, out_dev, _, _ = data_utils.prepare_poem_data(
      data_dir, in_vocabulary_size, out_vocabulary_size, line_based=True, skip_thought=True)
train_set = translate.read_data(in_train, out_train)
print(train_set)