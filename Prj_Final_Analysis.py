import pandas as pd
import matplotlib.pyplot as plt

'''take input from the user 
type_code and a respec type in that 
then filter the data accordingly 
then do analysis for that
say
    get the descending order for the states
        its just groupby states and then total sum
    see which gender will commit more
    see which age_group will commit max suicides
    all these for that particular Type in that Type_code chosen by the user'''

data = pd.read_csv(r"DataSets\SuicidesPredicted.csv")

nxt_year = max(list(data['Year'].unique()))

print("----Predicting the number of suicides in {}-----".format(nxt_year))
print("What is the basis of ur analysis?")

data_nxt_year = data[data['Year'] == nxt_year]

Type_codes = list(data_nxt_year['Type_code'].unique())

for i in range(len(Type_codes)):
    print(str(i+1),Type_codes[i])

tc_ch = int(input("Enter your choice(number): "))
Type_code = Type_codes[tc_ch-1]

data_nxt_year = data_nxt_year[data_nxt_year["Type_code"] == Type_code]
Types = data_nxt_year['Type'].unique()
count = 0
print("Available Types are: ")
for Type in Types:
    print(str(count+1),Type)
    count+=1

t_ch = int(input("Enter your choice(number): "))
Type = Types[t_ch-1]

data_nxt_year = data_nxt_year[data_nxt_year['Type'] == Type]

data_nxt_year.groupby('State').sum()['Total'].plot('barh',title='predicted State wise suicides in '+str(nxt_year))
plt.show()

# data_type = data[data['Type'] == Type]
# for state in data_type['State'].unique():
#     data_type_s = data_type[data_type['State'] == state]
#     data_type_s = data_type_s.groupby('Year').sum()
#     avg = data_type_s['Total'].mean()
#     data_type_s['Total'].plot(kind = 'line',title="Year trend in "+state)

    # pred_suicides = data_type_s['Total'][nxt_year]
    # if pred_suicides > avg:
    #     print(state+": More than average ({}) suicide deaths, diff: {}".format(round(avg,2),round(abs(pred_suicides - avg),2)))
    # else:
    #     print(state+": Less than average ({}) suicide deaths, diff: {}".format(round(avg),round(abs(pred_suicides - avg),2)))
    # plt.show()

data_nxt_year.groupby('Age_group').sum()['Total'].plot('bar',title='predicted Age_group wise suicides in '+str(nxt_year))
plt.show()

data_nxt_year.groupby('Gender').sum()['Total'].plot('bar',title='predicted Gender wise suicides in '+str(nxt_year))
plt.show()

'''This is to graphically check/show the rate of suicides due to that 
    particular cause has increased or decreased'''

data = data[data['Type'] == Type]
plt.subplot('121')
data[data['Year'] != nxt_year].groupby('Year').sum()['Total'].plot('line',title="Recorded data")
plt.subplot('122')
data.groupby('Year').sum()['Total'].plot('line',title="Including prediction")
plt.show()
# ------------

df = data.groupby('Year').sum()['Total']

rate = ((df.loc[nxt_year-1] - df[nxt_year])/df[nxt_year])*100
if rate >0:
    print("Number of suicides in India for given Type\n will Reduce by: ",rate,"%","in "+str(nxt_year))
else:
    print("Number of suicides in India for given Type\n will Increase by: ",abs(rate),"%","in "+str(nxt_year))
