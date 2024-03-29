# -*- coding: utf-8 -*-


Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c6KsoPLl2hdN7Wr_f00UoE7uZ6i9jyks

#Download
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
# % matplotlib inline

dt = pd.read_csv('/content/robot_inverse_kinematics_dataset.csv')
dt.head()

"""#Headmap"""

sns.pairplot(dt)

zx = dt.drop(['z'], axis = 1)
zy = dt['z']

yx = dt.drop(['y'], axis = 1)
yy = dt['y']

xx = dt.drop(['x'], axis = 1)
xy = dt['x']

zy.shape,zx.shape

yy.shape,yx.shape

xy.shape,xx.shape

zx.head()

xx.head()

"""#Split"""

from sklearn.model_selection import train_test_split
zx_train, zx_test, zy_train, zy_test = train_test_split(zx, zy, test_size = 0.25, random_state = 0)

yx_train, yx_test, yy_train, yy_test = train_test_split(yx, yy, test_size = 0.2, random_state = 0)

xx_train, xx_test, xy_train, xy_test = train_test_split(xx, xy, test_size = 0.3, random_state = 42)

"""#Scaler"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
zx_train = sc.fit_transform(zx_train)
zx_test = sc.transform(zx_test)

yx_train = sc.fit_transform(yx_train)
yx_test = sc.transform(yx_test)

xx_train = sc.fit_transform(xx_train)
xx_test = sc.transform(xx_test)

"""#Decision Tree"""

from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor(random_state=0)   # random sate = 0
tree_reg.fit(zx_train,zy_train)

from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor(random_state=100) 
tree_reg.fit(yx_train,yy_train)

from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor(random_state=0) 
tree_reg.fit(xx_train,xy_train)

"""#Predict"""

zy_pred = tree_reg.predict(zx_test)

yy_pred = tree_reg.predict(yx_test)

xy_pred = tree_reg.predict(xx_test)

"""#Visualization"""

text_representation = tree.export_text(tree_reg)
print(text_representation)

"""#Accuracy score"""

zscore = tree_reg.score(zx_test,zy_test)

print(zscore)

yscore = tree_reg.score(yx_test, yy_test)

print(yscore)

xscore = tree_reg.score(xx_test, xy_test)

print(xscore)

"""#Random Forest

zscore to Random Forest
"""

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf.fit(zx_train,zy_train)

zy_pred2 = rf.predict(zx_test)

zscore = rf.score(zx_test,zy_test)

print(zscore)

"""yscore to Random Forest"""

rf.fit(yx_train,yy_train)

yy_pred2 = rf.predict(yx_test)

yscore = rf.score(yx_test,yy_test)

print(yscore)

"""xscore to Random Forest"""

rf.fit(xx_train,xy_train)

xy_pred2 = rf.predict(xx_test)

xscore = rf.score(xx_test,xy_test)

print(xscore)