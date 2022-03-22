import pandas as pd
import numpy as np
import sys
import pickle
from pandas.core.dtypes.missing import isna

topics = sys.argv[1]
queryclass=sys.argv[2]
qrel = sys.argv[3]


#delet colmun and creat new file from original dataset
def edit_trec2009MQ(dataset):
    data = pd.read_csv(f'dataset/{dataset}', encoding = "ISO-8859-1", sep=':',header=None, index_col=False)
    data=data.drop(data.columns[1],axis=1)
    data.to_csv(r'topics.trecMQ', header=None, index=None, sep=' ', mode='a')
    #data1 = pd.read_csv(f'topics.trecMQ', encoding = "ISO-8859-1", sep=' ',header=None, index_col=False)

# this is a proof that all queries in queryclass dataset  are exist in topic dataset
def find_query_type(queryclass, topics):
    queryclass = pd.read_csv(f'dataset/{queryclass}',encoding='utf-8', sep='\t')
    topics= pd.read_csv(f'topics.trecMQ', encoding = "ISO-8859-1", sep=' ',header=None, index_col=False)
    for i in range(len(topics)):
        for j in range(len(queryclass)):
            if queryclass["Topic"][j]==topics[0][i]:
                (topics.loc[[i]]).to_csv(r'final_queries', header=None, index=None, sep=' ', mode='a')
                (queryclass.loc[[j]]).to_csv(r'final_types', header=None, index=None, sep=' ', mode='a')
        data1 = pd.read_csv(f'final_queries', encoding="ISO-8859-1", sep=' ', header=None, index_col=False)
        data2 = pd.read_csv(f'final_types', encoding="ISO-8859-1", sep=' ', header=None, index_col=False)
        print(len(data1),len(queryclass))

        #(data.loc[[i]]).to_csv(r'final_queries', header=None, index=None, sep=' ', mode='a')
       # print(queryclass.loc[[i]])
    #data1 = pd.read_csv(f'final_queries', sep=' ', header=None, index_col=False)
    print(queryclass["Topic"][0])

    #data.to_csv(r'topics.trecMQ', header=None, index=None, sep=' ', mode='a')


data1 = pd.read_csv(f'final_queries', encoding = "ISO-8859-1", sep=' ',header=None, index_col=False)
print(data1)
#if __name__ == "__main__":
   #edit_trec2009MQ(topics)
   #find_query_type(queryclass, topics)

