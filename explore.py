import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
pd.set_option('display.float_format', lambda x: '{:.2f}'.format(x))
sns.set_context("notebook", rc={"axes.formatter.limits": (-2, 3)})

def univariate_explore(dataframe, exclude_columns=None):
    """
    Perform univariate exploration of feature variables in a pandas DataFrame.

    Parameters:
    - dataframe: pandas DataFrame
    - exclude_columns: list of column names to exclude from exploration (default=None)

    Returns:
    - None (displays plots and statistics)
    """

    # Get a list of column names and their data types
    column_data_types = dataframe.dtypes

    for column_name, data_type in column_data_types.items():
        if exclude_columns and column_name in exclude_columns:
            continue  # Skip columns specified in exclude_columns

        if data_type == 'object':
            # Categorical variable
            print(f"Exploring '{column_name}' (Categorical Variable):")
            frequency_table = dataframe[column_name].value_counts()
            print("Frequency Table:")
            print(frequency_table)
            plt.figure(figsize=(10, 6))
            sns.countplot(data=dataframe, x=column_name)
            plt.xticks(rotation=45)
            plt.title(f'Bar Plot of {column_name}')
            plt.show()
        elif data_type in ['int64', 'float64']:
            # Numeric variable
            print(f"Exploring '{column_name}' (Numeric Variable):")
            print("Summary Statistics:")
            print(dataframe[column_name].describe())
            plt.figure(figsize=(10, 6))
            plt.hist(dataframe[column_name], bins=20, color='skyblue', edgecolor='black')
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {column_name}')
            plt.show()
        else:
            print(f"Variable '{column_name}' has an unsupported data type: {data_type}")

def fraud_by_type(train):
    '''
    
    '''
    train_fraud_only = train[train.isfraud == 1]
    sns.countplot(data=train_fraud_only, x=train_fraud_only.type)
    plt.xticks(rotation=45)
    plt.title('Bar Plot of Fraud by Transaction Type')
    plt.ylabel('Fraud Count')
    plt.xlabel('')
    plt.show()
