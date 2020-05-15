# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=data['Loan_Status'].value_counts()
print(loan_status)
#Creating a new variable to store the value counts
fig=plt.figure(figsize=(20,10))
loan_status.plot('bar')
#Plotting bar plot
plt.show()


# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
print(property_and_loan)
property_and_loan.plot(kind='bar',stacked=False,figsize=(20,10))
plt.xlabel('Property Area')
#Changing the x-axis label
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
#Changing the y-axis label
plt.show()

#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(20,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
#Changing the x-axis label
plt.xticks(rotation=45)
plt.show()
#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
#Subsetting the dataframe based on 'Education' column
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
#Plotting scatter plot
ax_1.set_title('Applicant Income')

#Setting the subplot axis title
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set_title('Coapplicant Income')
#Plotting scatter plot
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
#Setting the subplot axis title
ax_3.set_title('Total Income')

#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



