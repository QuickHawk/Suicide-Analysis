import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv(r"DataSets\Suicides.csv")
un_State = pd.Series(['Total (All India)','Total (States)','Total (Uts)'])
data = data[~data['State'].isin(un_State)]
data = data.reset_index().drop(['index'],axis=1)

years = data['Year'].unique()
States = data['State'].unique()
Type_codes = data['Type_code'].unique()

missing_data = pd.DataFrame(columns=['State','Year','Type_code','Type','Gender','Age_group','Total'])
remove_index = []

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

                    missing_years = []
                    for year in years:
                        if year not in fil_data['Year'].values: #i.e., if some year is not found then note it
                            missing_years.append(year)
                    '''
                        so basically if there are any missing years then we predict for that using 
                        the model we train with the available data
                    '''
                    if len(missing_years)!=0 :
                        test_size = int(fil_data.shape[0]*0.2) 
                        '''
                            i took 0.2 just to make sure that we train our model for more number of
                            samples,
                            now if the fil_data has 1,2,3 or 4 records only the test_size(size*0.2) will be 
                            zero coz there is no round fun
                        '''
                        
                        if test_size == 0:
                            """
                                this means that fil_data has less number of records as told abv
                                so basically we can just predict nothing as we will not be able 
                                to train the model well 
                                so i'll just note down their indices and just remove all of these 
                                from the data
                                coz our basic aim is to show the analysis for that type in the 
                                coming year(s) 
                            """
                            remove_index.append(list(fil_data.index))
                            '''
                                every time fil_data satisfies test_size == 0
                                this abv stat will be executed and this will make 
                                remove_index as a list of list which contain indices of all those
                                records which are of no use
                                i.e.,those Type in that particualar state for which we will not 
                                do a future prediction
                            '''
                            '''
                                its just that in the abv steps we are getting a sample number of years
                                and there resp totals to train the model
                            '''
                        else:
                            train_set = fil_data[:-test_size]
                            train_x = train_set.iloc[:,1:2]
                            train_y = train_set.iloc[:,-1:-2:-1]
        
                            Lregr = LinearRegression()
                            Lregr.fit(train_x,train_y)

                            '''
                                now after the model is ready we predict it for missing years
                                but for that we will have to convert the missing_years to a 2D array
                            '''
                            missing_years = np.array(missing_years).reshape(len(missing_years),1)
                            req_missing = Lregr.predict(missing_years) # we get it as a 2D array with one prediction in every row
                            
                            req_missing = [int(round(req_missing[i][0])) for i in range(missing_years.shape[0])]
                            req_missing = [0 if pred <0 else pred for pred in req_missing] 

                            for year,total in zip(missing_years,req_missing): 
                                df = pd.DataFrame([[State,int(year),Type_code,Type,gender,age_grp,total]],columns=['State','Year','Type_code','Type','Gender','Age_group','Total'])
                                # we are having int(year) coz missing_years is a 2D arr and gives an array for every iteration
                                missing_data = missing_data.append(df,ignore_index=True)
                    else:
                        pass
req_indices = []
# print("Remove index: ",remove_index)
print("shape before removing unnecessary records:",data.shape[0])

for index in data.index:
    exists = False
    for sublist in remove_index:
        if index in sublist:
            exists = True
            break
    if exists is not True:
        req_indices.append(index)

# print(max(req_indices))

'''
    so basically we are trying to get indices from the data.index which are not in the remove_index
'''
data = data.iloc[req_indices,:]

print("shape After removing unnecessary records:",data.shape[0])

data = data.reset_index().drop(['index'],axis=1)
print("The number of missing values predicted:",missing_data.shape[0])
data = data.append(missing_data,ignore_index=True)
print("After filling data with missing values:",data.shape[0])

data.to_csv(r"DataSets\Pre_Procesed_Suicides.csv",index=False) 
print("successfully done")