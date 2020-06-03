import transformers


MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 3
# BERT_PATH = "../input/bert_base_uncased/"
BERT_MODEL = "bert-base-uncased"
TRAINING_FILE = "../data/IMDB Dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_MODEL)