# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
categorical_val=bank_data.select_dtypes(include='object')
numerical_val=bank_data.select_dtypes(include='number')
#Code starts here
banks=bank_data.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
banks=banks.replace(to_replace=np.nan,value=bank_mode)
print(banks.isnull().sum().values.sum())
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)
loan_approved_se=len(banks[(banks.Self_Employed=='Yes') & (banks.Loan_Status=='Y')])
loan_approved_nse=len(banks[(banks.Self_Employed=='No') & (banks.Loan_Status=='Y')])
percentage_se=loan_approved_se*100/614
percentage_nse=loan_approved_nse*100/614
print(percentage_se)
print(percentage_nse)
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
banks['Loan_Amount_Term']=loan_term
big_loan_term=len(banks[banks.Loan_Amount_Term>=25.0])
print(big_loan_term)
loan_groupby=banks.groupby('Loan_Status')[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.agg('mean')
print(mean_values)


