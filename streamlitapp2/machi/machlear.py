import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv("penguins_cleaned.csv")
data=df.copy()
target='species'
encode=['sex','island']

for col in encode:
        dummy=pd.get_dummies(data[col],prefix=col)
        data=pd.concat([data,dummy],axis=1)
        del data[col]
target_mapper={'Adelie':0,'Chinstrap':1,'Gentoo':2}
def target_encode(val):
        return target_mapper[val]
data['species']=data['species'].apply(target_encode)

x=data.drop('species',axis=1)
y=data['species']

clf=RandomForestClassifier()
clf.fit(x,y)

import pickle
pickle.dump(clf,open('peng.pkl','wb'))