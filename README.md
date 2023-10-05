# Fraud Detection in Online Payments:
<hr style="border:2px solid black">

## <u>Project Description</u>
Billions of dollars of fraud in online transactions occures every year. Identifying the most common fraud tactics is the first step in preventing fraud. Being able to automate fraud detection will allow financial institutions to better protect themselves and their customers while using fewer resources.

## Goals: 
* Discover patterns of fraudulent activity in online payments
* Create a classification model to identify fraudulent transactions with high level of precision and recall

<hr style="border:2px solid black">

# Initial Thoughts
 * Fraud is likely going to occur in only certain transactions types. 
 * Because these transactions are online fraud tactics are going to limited to what someone can influence remotely. Be on the watchout for data manipulation. If I can find patterns of string manilupation in a small sample will they be statistically significant in the population data?

 
<hr style="border:2px solid black"> 


# Data Dictionary
| Feature               | Definition |
|:----------------------|:-----------|
| step |                            (int64) represents a unit of time where 1 step equals 1 hour|
| type |                                                    (object) type of online transaction |
| amount |                                              (float64) the amount of the transaction |
| nameOrig |                                          (object) customer starting the transaction|
| oldbalanceOrg|                                       (float64) balance before the transaction |
| newbalanceOrig|                                        (float64) balance after the transaction|
| nameDest|                                                (object) recipient of the transaction|
| oldbalanceDest|                 (float64) initial balance of recipient before the transaction |
| newbalanceDest|                  (float64) the new balance of recipient after the transaction |
| isFraud |                                                      (int64) fraudulent transaction |


## Summary

- There are 6,362,620 rows (transactions)
- The target variable is `isfraud`, indicating whether a transaction is fraudulent or not.
<hr style="border:2px solid black"> 


# The Plan
 
Plan --> Acquire --> Prepare --> Explore --> Model --> Deliver
 

#### Acquire
    * Download csv from https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset/data and read into pandas DataFrame
#### Prepare
    * Rename Columns
    * Create new Variables
    * Scale 'step'
    * Add Baseline prediction to DataFrame
    * Split data into train, validate and test (approx. 60/20/20), stratifying on 'isfraud'
#### Explore
    * Filter for fraudulent activity only to search for patterns
    * Vizualize fraud distribution across 'step' and 'type'
    * Perform stats tests to verify significance of findings
    * Choose features for the model
#### Model
    * Decistion Tree Classifier 
    * Logistic Regression
    * Logistic Regression w/ new feature set

<hr style="border:2px solid black"> 

# Steps to Reproduce
>1) Clone this repo.
>2) Download csv from goole drive https://drive.google.com/file/d/1mrGk_zVKbxdxAAPlYaMCJ3h_uHG1oD-t/view?usp=sharing
>3) Run notebook.
<hr style="border:2px solid black"> 

# Summary
 
### <u>Recommendations:</u>

>* Implement security protocols to prevent complete withdrawals of an account without identification.
>* Investigate IT vulnerabilities that could allow hackers to change transfer destination.

### <u>Next Steps:</u>
>* For high value transactions where the predicted probability of fraud was high, but not high enough to classify as fraudulent, pass to a human for further investigation.