import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


def get_baseline(train):
    '''
    Calculate and print baseline evaluation metrics for a binary classification problem.

    This function calculates and prints the following baseline evaluation metrics:
    - Baseline Accuracy
    - Baseline Precision Score
    - Baseline ROC AUC Score

    Parameters:
    train (pd.DataFrame): The DataFrame containing training data with 'isfraud' and 'baseline' columns.

    Returns:
    None: The function prints the baseline metrics but does not return any values.
    '''
    # Accuracy
    baseline_acc = 3812644 / 3817572
    print(f'Baseline Accuracy: {baseline_acc:.4f}')
    
    # Precision
    print('Baseline Precision Score: {:.4f}'
          .format(precision_score(train.isfraud, train.baseline)))
    
    
    # roc_auc_score
    y_true = train['isfraud']
    y_pred_class = train['baseline']
    
    # Convert predicted class labels to "soft" labels (probabilities)
    y_pred_probabilities = np.where(y_pred_class == 1, 1, 0)
    
    roc_auc = roc_auc_score(y_true, y_pred_probabilities)
    print("Baseline ROC AUC Score:", roc_auc)
    