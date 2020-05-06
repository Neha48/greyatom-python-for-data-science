# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
census=np.concatenate((data,new_record),axis=0)
print(census.shape)
age=np.array([x[0] for x in census])
max_age=max(age)
min_age=min(age)
age_mean=sum(age)/age.size
print(age_mean)
age_std=age-age_mean
race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]
for i in census:
    if i[2]==0:
        race_0.append(i)
    elif i[2]==1:
        race_1.append(i)
    elif i[2]==2:
        race_2.append(i)
    elif i[2]==3:
        race_3.append(i)
    elif i[2]==4:
        race_4.append(i)
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
minority_race=min(len_0,len_1,len_2,len_3,len_4)
senior_citizens=list(filter(lambda x: x[0]>60, census))
senior_citizens_len=len(senior_citizens)
working_hours_sum=sum([x[6] for x in senior_citizens])
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=[]
low=[]
for i in census:
    if i[1]>10:
        high.append(i)
    else:
        low.append(i)
avg_pay_high=sum([x[7] for x in high])/len(high)
avg_pay_low=sum([x[7] for x in low])/len(low)
print(avg_pay_high)
print(avg_pay_low)


