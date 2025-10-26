import pickle as pkl
import pandas as pd

with open("netflix_dataset.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)
df.to_csv(r'netflix_dataset.csv')