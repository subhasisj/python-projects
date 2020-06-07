import pandas as pd
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from transformers import AdamW
from transformers import get_linear_schedule_with_warmup

from src import config
from src import dataset
from src import model as m
from src import train

import os
import warnings
warnings.filterwarnings("ignore")


np.random.seed(20)
import gc
gc.collect()
torch.cuda.empty_cache()


def run():
    # df = pd.read_csv('./data/IMDB Dataset.csv')
    df = pd.read_csv(config.TRAINING_FILE)
    df.sentiment = df.sentiment.apply(lambda x: 1 if x == 'positive' else 0)
    df = df[:20000]
    df_train,df_test = train_test_split(df,test_size = 0.1)
    df_val ,df_test = train_test_split(df_test,test_size =0.5)

    df_train.reset_index(drop=True,inplace=True)
    df_val.reset_index(drop=True,inplace=True)

    train_dataset = dataset.SentimentDataset(review = df_train.review.values, target = df_train.sentiment.values)
    train_data_loader = torch.utils.data.DataLoader(train_dataset,batch_size=config.TRAIN_BATCH_SIZE,num_workers=4)
    
    val_dataset = dataset.SentimentDataset(review = df_val.review.values, target = df_val.sentiment.values)
    val_data_loader = torch.utils.data.DataLoader(val_dataset,batch_size=config.VALID_BATCH_SIZE,num_workers=4)
    
    test_dataset = dataset.SentimentDataset(review = df_test.review.values, target = df_test.sentiment.values)
    test_data_loader = torch.utils.data.DataLoader(test_dataset,batch_size=1,num_workers=4)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model = m.BertBaseUncased(len(df.sentiment.value_counts()))
    model.to(device)

    if not os.path.isfile(config.SAVE_MODEL_PATH):


        # param_optimizer = list(model.named_parameters())

        optimizer = AdamW(model.parameters(), lr=2e-5, correct_bias=False)
        total_steps = int(len(train_data_loader)/config.TRAIN_BATCH_SIZE * config.EPOCHS)

        scheduler = get_linear_schedule_with_warmup(
                        optimizer,
                        num_warmup_steps=0,
                        num_training_steps=total_steps
                        )


        # model = torch.nn.DataParallel(model)
    
        best_accuracy = 0
        training_engine = train.Training(
                            data_loader = train_data_loader,
                            model = model,
                            optimizer= optimizer,
                            device = device,
                            scheduler = scheduler,
                            n_examples = len(df_train))
        validation_engine = train.Evaluation(
                            data_loader = val_data_loader,
                            model = model,
                            device = device,
                            n_examples = len(df_val))

        for epoch in range(config.EPOCHS):
            print('=='*50)
            print(f'Epoch: {epoch+1} / {config.EPOCHS}:')
            print('--------------')
            training_accuracy,training_loss = training_engine.train()
            print(f'Training Accuracy: {training_accuracy} -- Training Loss: {training_loss}')

            gc.collect()
            torch.cuda.empty_cache()

            validation_accuracy,validation_loss = validation_engine.evaluate()
            print(f'Validation Accuracy: {validation_accuracy} -- Validation Loss: {validation_loss}')
            # print('=='*50)
            print()

            if validation_accuracy > best_accuracy:
                torch.save(model.state_dict(),config.SAVE_MODEL_PATH)
                best_accuracy = validation_accuracy
    else:

        model.load_state_dict(torch.load(config.SAVE_MODEL_PATH))
        model.to(device)
        testing_engine = train.Evaluation(
                            data_loader = test_data_loader,
                            model = model,
                            device = device,
                            n_examples = len(df_test))

        testing_accuracy,testing_loss = testing_engine.evaluate()
        print(f'Testing Accuracy: {testing_accuracy} -- Testing Loss: {testing_loss}')
        



if __name__=='__main__':

    run()





