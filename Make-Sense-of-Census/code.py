# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print(new_record)
census=np.concatenate((data,new_record))
#Code starts here
print(census)


# --------------
#Code starts here
import numpy as np 
age=np.array(census[:,0])
print(age)
max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=np.std(age)
print(age_std)


# --------------
import numpy as np 


race_0=census[census[:,2] == 0]
len_0=len(race_0)
print(len_0)
race_1=census[census[:,2] == 1]
len_1=len(race_1)
print(len_1)
race_2=census[census[:,2] == 2]
len_2=len(race_2)
print(len_2)
race_3=census[census[:,2] == 3]
len_3=len(race_3)
print(len_3)
race_4=census[census[:,2] == 4]
len_4=len(race_4)
print(len_4)
races=[len_0,len_1,len_2,len_3,len_4]
minority_race=races.index(min(races))
print(minority_race)


# --------------
#Code starts here
import numpy as np 
senior_citizens=census[census[:,0] >60]

senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
working_hours_sum=sum(senior_citizens[:,6])
print(working_hours_sum)

avg_working_hours=working_hours_sum / senior_citizens_len
print(avg_working_hours)


    


# --------------
#Code starts here
import numpy as np 
 
high=census[census[:,1] >10]
high
low=census[census[:,1]<=10]
high_income=high[:,7]
avg_pay_high=high_income.mean()
print(avg_pay_high)
low_income=low[:,7]
avg_pay_low=low_income.mean()
print(avg_pay_low)
#low=


