import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report
import pickle
import os

os.chdir(os.path.dirname(__file__))

# data
x_train = pd.read_csv('data/processed/train.csv', index_col=False)
x_test = pd.read_csv('data/processed/test.csv', index_col=False)
y_train = x_train.pop('label')
y_test = x_test.pop('label')


# model training
rf = RandomForestClassifier(random_state=42)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)

# save
pickle.dump(rf, open('../rf_script.pkl/', 'wb'))

#output
print(accuracy_score(y_test, y_pred_rf))

plt.rcParams['figure.figsize']=5,5
sns.set_style("white")
plot_confusion_matrix(rf, x_test, y_test, cmap=plt.cm.Blues)
plt.show()
