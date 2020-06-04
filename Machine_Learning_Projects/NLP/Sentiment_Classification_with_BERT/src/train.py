import torch
import numpy as np
from tqdm import tqdm

class Training:

    def __init__(self,data_loader,model,optimizer,scheduler,device,n_examples):
        
        self.data_loader = data_loader
        self.model = model
        self.optimizer = optimizer
        self.device = device
        self.loss_fn = torch.nn.CrossEntropyLoss().to(device)
        self.n_examples = n_examples
        self.scheduler = scheduler
    

    def train(self):

        self.model.train()
        losses = []
        correct_predictions = 0
        for batch, data in tqdm(enumerate(self.data_loader),total = len(self.data_loader)):

            outputs, targets = convert_inputs_for_model(self.model,data,self.device)

            _,preds = torch.max(outputs,dim = 1)
            targets = targets.long()
            loss = self.loss_fn(outputs,targets)
            correct_predictions += torch.sum(preds == targets)
            losses.append(loss.item())

            loss.backward()
            torch.nn.utils.clip_grad_norm(self.model.parameters(),max_norm = 1.0)

            self.optimizer.step()
            self.scheduler.step()
            self.optimizer.zero_grad()
        
        return correct_predictions.double() / self.n_examples , np.mean(losses)

def convert_inputs_for_model(model, data,device):

    input_ids = data["ids"].to(device,dtype = torch.long)
    attention_mask = data["attention_mask"].to(device,dtype = torch.long)
    targets = data["targets"].to(device,dtype = torch.float)

    outputs = model(
        input_ids = input_ids,
        attention_mask = attention_mask
    )
    return outputs, targets



class Evaluation:
    def __init__(self,data_loader,model,device,n_examples):
        self.model = model
        self.data_loader = data_loader
        self.device = device
        self.n_examples = n_examples
        self.loss_fn = torch.nn.CrossEntropyLoss().to(device)

    def evaluate(self):

        self.model.eval()
        losses = []
        correct_predictions = 0

        for batch, data in tqdm(enumerate(self.data_loader),total = len(self.data_loader)):
           
            outputs, targets = convert_inputs_for_model(self.model,data,self.device)

            _,preds = torch.max(outputs,dim = 1)
            targets = targets.long()
            loss = self.loss_fn(outputs,targets)
            correct_predictions += torch.sum(preds == targets)
            losses.append(loss.item())

        return correct_predictions.double() / self.n_examples , np.mean(losses)

