import streamlit as st
import os
from src import config
from src import model as m
import torch
import torch.nn.functional as F


def main():
    st.header('Sentiment Classification using BERT')
    review = st.text_input('Enter Text to Classify')
    review = str(review)
    review = " ".join(review.split())

    if st.button('Predict'):
        if os.path.isfile(config.SAVE_MODEL_PATH):
            device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
            model = m.BertBaseUncased(2)
            model.to(device)

            encoded_text = config.TOKENIZER.encode_plus(
                review,
                add_special_tokens=True,
                max_length=config.MAX_LEN,
                return_token_type_ids = False,
                pad_to_max_length = True,
                return_attention_mask = True,
            # return_tensors = 'pt'
            )

            ids = encoded_text['input_ids']
            mask = encoded_text['attention_mask']

            ids = torch.tensor(ids, dtype=torch.long).unsqueeze(0)
            mask = torch.tensor(mask, dtype=torch.long).unsqueeze(0)

            ids = ids.to(device, dtype=torch.long)
            mask = mask.to(device, dtype=torch.long)

            with torch.no_grad():
                probabilities = F.softmax(model(ids,mask),dim =1)

            confidence,predicted_class = torch.max(probabilities,dim=1)
            predicted_class = predicted_class.cpu().item()
            probabilities = probabilities.flatten().cpu().numpy().tolist()
            CLASS_NAMES = [
                    "Negative",
                    "Positive"
                    ]

           
            st.write()

            result = {

                    "Predicted Class" : CLASS_NAMES[predicted_class],
                    "Confidence" : float(confidence),
                    "Probabilities" :dict(zip(CLASS_NAMES, probabilities))

            }




            st.write(result)


            


if __name__ == '__main__':
    main()