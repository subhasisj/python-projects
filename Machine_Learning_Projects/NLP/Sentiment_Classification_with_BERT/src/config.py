import transformers


MAX_LEN = 100
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = "./data/bert_base_uncased/"
# BERT_MODEL = "bert-base-uncased"
SAVE_MODEL_PATH = "./data/saved_model/best_model.bin"
TRAINING_FILE = "./data/IMDB Dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH)