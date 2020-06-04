import pandas as pd
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from transformers import AdamW
from transformers import get_linear_schedule_with_warmup

import config
import dataset
import model


np.random.seed(20)


def run():
    df = pd.read_csv('../data/IMDB Dataset.csv')
    df.sentiment.apply(lambda x: 1 if x == 'positive' else 0)

    df_train,df_test = train_test_split(df,test_size = 0.1)
    df_val ,df_test = train_test_split(df_test,test_size =0.5)

    df_train.reset_index(drop=True,inplace=True)
    df_val.reset_index(drop=True,inplace=True)

    train_dataset = dataset.SentimentDataset(review = df_train.review.values, target = df_train.sentiment.values)
    train_data_loader = torch.utils.data.DataLoader(train_dataset,batch_size=config.TRAIN_BATCH_SIZE,num_workers=4)
    
    val_dataset = dataset.SentimentDataset(review = df_val.review.values, target = df_val.sentiment.values)
    val_data_loader = torch.utils.data.DataLoader(val_dataset,batch_size=config.TRAIN_BATCH_SIZE,num_workers=4)
    
    test_dataset = dataset.SentimentDataset(review = df_test.review.values, target = df_val.sentiment.values)
    test_data_loader = torch.utils.data.DataLoader(test_dataset,batch_size=config.TRAIN_BATCH_SIZE,num_workers=4)

    model = BertBaseUncased(len(df.sentiment.value_counts()))

    # param_optimizer = list(model.named_parameters())

    optimizer = AdamW(model.parameters(), lr=2e-5, correct_bias=False)
    total_steps = len(train_data_loader) * config.EPOCHS

    scheduler = get_linear_schedule_with_warmup(
                    optimizer,
                    num_warmup_steps=0,
                    num_training_steps=total_steps
                    )






