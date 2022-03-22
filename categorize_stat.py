import pandas as pd
import numpy as np
import sys
import pickle
from pandas.core.dtypes.missing import isna

dataset_name = sys.argv[1]


def read_ds(dataset):
    data = pd.read_csv(f'dataset/{dataset}', sep='\t')
    return data

def generate_query(ds_name):
    info_O=[]
    info_C=[]
    nav=[]
    groups = read_ds(ds_name)
    for i in range(len(groups["Class"])):
        if groups["Class"][i]=="Information_Close":
            info_C.append(groups["Topic"][i])
        elif groups["Class"][i]=="Information_Open":
            info_O.append(groups["Topic"][i])
        elif groups["Class"][i]=="Navigational":
            nav.append(groups["Topic"][i])
    with open(f'info_O.pkl', 'wb') as f:
        pickle.dump(info_O, f)
    with open(f'info_C.pkl', 'wb') as f:
        pickle.dump(info_C, f)
    with open(f'nav.pkl', 'wb') as f:
        pickle.dump(nav, f)
    with open('info_C.pkl', 'rb') as f:
            info_C_result = pickle.load(f)
    with open('info_O.pkl', 'rb') as f:
            info_O_result = pickle.load(f)
    with open('nav.pkl', 'rb') as f:
        nav_result = pickle.load(f)
    print("info_c is:",len(info_C_result))
generate_query(dataset_name)