import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from sklearn.datasets import fetch_mldata
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

#####################################################################################
##########     DATA                     #############################################
#####################################################################################

mnist = fetch_mldata('MNIST original')

X, y = mnist["data"], mnist["target"]

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]

y_train_5 = (y_train == 5)  # True for all 5s, False for all other digits.
y_test_5 = (y_test == 5)

#####################################################################################
##########     VISUALISATION          ###############################################
#####################################################################################

some_digit = X[36000]
some_digit_image = some_digit.reshape(28, 28)

plt.imshow(some_digit_image, 
           cmap = matplotlib.cm.binary,
           interpolation="nearest")

plt.axis("off")
plt.show()

label = y[36000]
print(label)

#####################################################################################
##########     MACHINE LEARNIG          #############################################
#####################################################################################

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)

prediction = sgd.predict(some_digit)

cross_val_score(sgd_clf, 
                X_train, 
                y_train_5, 
                cv=3, 
                scoring="accuracy")

confusion_matrix(y_train_5, y_train_pred)

precision_score(y_train_5, y_train_pred) 
recall_score(y_train_5, y_train_pred) 

fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)

plot_roc_curve(fpr, tpr)
plt.show()

roc_auc_score(y_train_5, y_scores)


