#lab 5
#Programmer: zahra sodagartojgi 
#Language: Python 3.9.2 
#rainfall.py

#declare variables

total_Rainfall = 0.0
month_Rainfall = 0.0
average_Rainfall = 0.0
years = 0
total_Months = 0

#get the input

years=int(input('Enter number of years: '))


#calculation

for year in range(years):
     for month in range(1,13):
         total_Months += 1
         month_Rainfall = float(input('Enter amount of rainfall (inches) for the month: ' ))
         total_Rainfall += month_Rainfall
                                      
average_Rainfall = total_Rainfall / total_Months
print('For',total_Months,'months, total rainfall is ',format(total_Rainfall,'.2f'),'inches and average rainfall is ',format(average_Rainfall,'.2f'),'inches')
        
        

