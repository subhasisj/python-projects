from src import config
import transformers
import torch.nn as nn

class BertBaseUncased(nn.Module):
    def __init__(self,n_classes):
        super(BertBaseUncased, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(config.BERT_PATH)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(self.bert.config.hidden_size,n_classes)

    def forward(self,input_ids,attention_mask):
        _, pooled_output = self.bert(
                input_ids = input_ids,
                attention_mask = attention_mask
            )

        output = self.bert_drop(pooled_output)
        return self.out(output)




