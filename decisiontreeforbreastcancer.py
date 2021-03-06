# -*- coding: utf-8 -*-
"""DecisionTreeForBreastCancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_lJ7e2yyC20JJziZEZuHNZaj1Ugx94LN
"""

from sklearn.datasets import load_breast_cancer
import pandas as pd
data=load_breast_cancer()
data

df_cancer=pd.DataFrame(data['data'],columns=data['feature_names'])
df_cancer['target']=data['target']
df_cancer

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data['data'],data['target'],test_size=0.20,random_state=1)
print("X_train shape",x_train.shape)
print("X_test shape",x_test.shape)
print("Y_train shape",y_train.shape)
print("Y_test shape",y_test.shape)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')
model

model.fit(x_train,y_train)
pv=model.predict(x_test)
print(pv)
from sklearn.metrics import accuracy_score,confusion_matrix
ac=accuracy_score(y_test,pv)
print(ac)
cm=confusion_matrix(y_test,pv)
print(cm)

import seaborn as sns
sns.heatmap(cm,annot=True,cmap='cool',linewidths=0.5,yticklabels=['malignant', 'benign'],xticklabels=['pv_malignant', 'pv_benign'])

fi=pd.Series(model.feature_importances_)
index=fi.index
print(fi)
print(index)
import matplotlib.pyplot as plt
plt.figure(figsize=(40,10))
plt.bar(data['feature_names'],fi)

print(data['feature_names'])

df_cancer_final=pd.DataFrame({'worst texture':df_cancer['worst texture'],
                              'worst perimeter':df_cancer['worst perimeter'],
                              'worst concave points':df_cancer['worst concave points'],
                              'target':df_cancer['target']})
df_cancer_final.head(10)

x=df_cancer_final.iloc[:,0:3]
print(x)
y=df_cancer_final.iloc[:,3]
print(y)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=1)
print("X_train shape",xtrain.shape)
print("X_test shape",xtest.shape)
print("Y_train shape",ytrain.shape)
print("Y_test shape",ytest.shape)

model=DecisionTreeClassifier()
model.fit(xtrain,ytrain)
pv=model.predict(xtest)
ac1=accuracy_score(ytest,pv)
print(ac1)

acv=[ac,ac1]
aci=['accuracy','final_accuracy']
plt.bar(aci,acv)

