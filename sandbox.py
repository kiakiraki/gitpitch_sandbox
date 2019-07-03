#%%
import pandas as pd
import seaborn as sns
from sklearn import datasets


sns.set()
sns.set_context('talk')

#%%
iris = sns.load_dataset("iris")
iris.head()


#%%
sns.pairplot(iris, hue='species', palette="husl")


#%%
