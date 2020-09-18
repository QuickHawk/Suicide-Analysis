# import matplotlib.pyplot as plt
# from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

'''plz predict the missing values before model fitting'''

data = pd.read_csv(r"DataSets\Pre_Processed_Suicides.csv")
print(data.shape)

Type = pd.Series(['Causes Not known','Other Causes (Please Specity)','Others (Please Specify)'])
data = data[~data['Type'].isin(Type)]

data = data[data['Age_group'] != '0-100+']

data = data.reset_index().drop(['index'],axis=1)

'''This is not working as there is no strong relation 
    b/w Total and Age_grp (-0.0017)'''
# data = data[data['Total'] > 0 ]
# print(data.shape[0])
# data['coded_Age_group'] = data['Age_group'].astype('category')
# data['coded_Age_group'] = data['coded_Age_group'].cat.codes

# print(data['Age_group'].unique())
# print(data['coded_Age_group'].unique())
# print(data.corr())
# --------------------

States = data['State'].unique()
Type_codes = data['Type_code'].unique()

pred_next_year = pd.DataFrame(columns=['State','Year','Type_code','Type','Gender','Age_group','Total'])

test_size = int(round(data['Year'].unique().shape[0]*0.2))

next_year = np.array(max(list(data['Year'].unique()))+1).reshape(1,1)

actual_list = data.groupby('Year').sum()['Total']
actual_list = np.array(actual_list[-test_size:]).reshape(test_size,1) 
# this will have totals of the last test_size number of years

pred_list = np.linspace(0,0,test_size+1).reshape(test_size+1,1) 
    #including the year to be predicted as well

'''    we actually are having these to cal RMSE'''

for State in States:
    s_fil_data = data[data['State'] == State]
    
    for Type_code in Type_codes:
        Tc_fil_data = s_fil_data[s_fil_data['Type_code'] == Type_code]
        
        for Type in Tc_fil_data['Type'].unique():
            t_fil_data = Tc_fil_data[Tc_fil_data['Type'] == Type] 
            
            for gender in t_fil_data['Gender'].unique():
                g_fil_data = t_fil_data[t_fil_data['Gender'] == gender]
                
                for age_grp in g_fil_data['Age_group'].unique():
                    fil_data = g_fil_data[g_fil_data['Age_group'] == age_grp]
                    
                    train_set = fil_data[:-test_size]
                    test_set = fil_data[-test_size:]
                    train_x = train_set.iloc[:,1:2].values
                    test_x = test_set.iloc[:,1:2].values
                    train_y = train_set.iloc[:,-1].values
                    train_y = train_y[:,np.newaxis]
                    
                    Lregr = LinearRegression()
                    Lregr.fit(train_x,train_y)
                    #this will train the data for the years from the first test_size number of years
                    
                    pred_y = Lregr.predict(test_x) 
                    # this will pred for the last test_size number of years includin the next year

                    '''this prediction may have negative and is a 2D array
                    of float type but as the number of suicides cannot be float
                    or negative we correct it in the next two steps'''

                    pred_y = [int(round(pred_y[i][0])) for i in range(test_size+1)]
                    pred_y = [0 if i<0 else i for i in pred_y]
                    
                    pred_list += np.array(pred_y).reshape(test_size+1,1)

                    # df = pd.DataFrame([[State,next_year[0][0],Type_code,Type,gender,age_grp,pred_y[-1]]],columns=['State','Year','Type_code','Type','Gender','Age_group','Total'])
                    # pred_next_year = pred_next_year.append(df,ignore_index=True)
                    """now this pred_y is the number of suicides committed by ppl in the 
                        year 2013
                        of 'Gender' = gender belonging to 'Age_group' = age_grp
                        with 'Type_code' = Type_code having 'Type' = Type 
                        belonging to 'State' = State"""
                
# data = data.append(pred_next_year, ignore_index = True)
# data.to_csv(r"DataSets\SuicidesPredicted.csv",index = False)
# print("predictedValues :",pred_list)
# print("Actual Values : ",actual_list)
print("RMSE: ",np.sqrt(mean_squared_error(pred_list[:-1],actual_list))) 
    #since actual list has only test_size values and the pred one has test_size+1

# 2 min 15 sec