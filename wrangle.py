# Custom Modules
import os
# Standard ds imports:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler




########################### ACQUIRE FUNCTION #####################################



def get_fraud_data():
    '''
    This function checks if the 'PS_20174392719_1491204439457_log.csv' file exists in a local file path. It it exists it will read the file into a pandas df. Returns df.
    '''
    if os.path.isfile('PS_20174392719_1491204439457_log.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('PS_20174392719_1491204439457_log.csv', index_col=0)
        
        # Reset Index
        df = df.reset_index()
    return df



############################# PREPARE FUNCTION #####################################

def prep_fraud(df):
    '''
    Prepare a DataFrame for fraud detection analysis by performing the following steps:
    
    1. Convert column names to lowercase.
    2. Drop unnecessary columns: 'nameorig', 'namedest', and 'isflaggedfraud'.
    3. Add additional features to the DataFrame:
       - 'transact_amount_equals_account_balance': Indicates whether the transaction amount equals the old account balance.
       - '10M_transfer': Indicates whether the transaction involves a transfer of 10 million units and is of type 'TRANSFER'.
       - 'transfer_missing_dest_balance': Indicates whether a 'TRANSFER' transaction has a destination account with zero old and new balances.
       - 'cashout_missing_orig_balance': Indicates whether a 'CASH_OUT' transaction has an original account with zero old and new balances.
       - 'transfer_cashout': Indicates whether the transaction type is either 'TRANSFER' or 'CASH_OUT'.
    4. Add a baseline prediction column 'baseline' initialized to 0.
    5. Scale the 'step' column using Min-Max scaling and add it as 'step_scaled'.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing transaction data.
    
    Returns:
    pd.DataFrame: The modified DataFrame with the added features and scaled 'step' column.
    '''
    
    # change column names to lowercase
    df.columns = df.columns.str.lower()
    
    # Drop cols
    df = df.drop(columns=['nameorig', 'namedest','isflaggedfraud'])
    
    # Add Features to Dataframe
    df['complete_withdrawal'] = df.amount == df.oldbalanceorg
    df['10M_transfer'] = (df.amount == 10000000.00)& (df.type == 'TRANSFER')
    df['transfer_missing_dest_balance'] = (df['type'] == 'TRANSFER') & (df['oldbalancedest'] == 0) & (df['newbalancedest'] == 0)
    df['cashout_missing_orig_balance'] = (df['type'] == 'CASH_OUT') & (df['oldbalanceorg'] == 0) & (df['newbalanceorig'] == 0)
    df['transfer_cashout'] = (df['type'] == 'TRANSFER') | (df['type'] == 'CASH_OUT')
    
    # Add baseline prediction to dataframe
    df['baseline'] = 0
    
    # Scale step column
    scaler = MinMaxScaler()
    df['step_scaled'] = scaler.fit_transform(df[['step']])
    
    return df


############################# SPLIT FUNCTION #######################################


def split_function(df, target_varible):
    ''' 
    Function takes in 2 positional arguments for a dataframe and target variable. Returns train, validate, test, dataframes stratified on the target variable. Roughly (60/20/20) split.
    
    '''
    train, test = train_test_split(df,
                                   random_state=666,
                                   test_size=.20,
                                   stratify= df[target_varible])
    
    train, validate = train_test_split(train,
                                   random_state=666,
                                   test_size=.25,
                                   stratify= train[target_varible])
    return train, validate, test


