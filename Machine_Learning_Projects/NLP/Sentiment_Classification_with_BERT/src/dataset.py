from src import config 
import torch

class SentimentDataset:

    def __init__(self,review,target):

        self.review = review
        self.target = target
        self.tokenizer = config.TOKENIZER
        self.max_len = config.MAX_LEN

    def __len__(self):
        return len(self.review)

    def __getitem__(self,item):

        review = str(self.review[item])
        review = " ".join(review.split())
        target = self.target[item]
        # print('-'*20)
        # print(target)

        inputs = self.tokenizer.encode_plus(
            review,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids = False,
            pad_to_max_length = True,
            return_attention_mask = True,
            # return_tensors = 'pt'
        )


        ids = inputs['input_ids']
        mask = inputs['attention_mask']
        # token_type_ids = inputs['token_type_ids']

        return {
            "ids": torch.tensor(ids,dtype = torch.long),
            "attention_mask": torch.tensor(mask,dtype = torch.long),
            # "token_type_ids": torch.tensor(token_type_ids,dtype = torch.long),
            "targets": torch.tensor(target,dtype = torch.float)
            
        }

