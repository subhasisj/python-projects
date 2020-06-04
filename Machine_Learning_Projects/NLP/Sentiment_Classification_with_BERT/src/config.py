import transformers


MAX_LEN = 256
TRAIN_BATCH_SIZE = 4
VALID_BATCH_SIZE = 2
EPOCHS = 3
BERT_PATH = "./data/bert_base_uncased/"
# BERT_MODEL = "bert-base-uncased"
SAVE_MODEL_PATH = "./data/saved_model/best_model.bin"
TRAINING_FILE = "./data/IMDB Dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH)