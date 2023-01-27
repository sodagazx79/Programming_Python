#calculating CO2 emissions
# Zahra Sodagartojgi
# Python 3.10.2
#CO2_emissions

#create and initialize variables and constants

co2=19.4 
  
#process

def  yearly_miles_driven (days_worked,distance):
    #create and initialize variables and constants
    miles_driven=0.0
    #process
    miles_driven=distance*2*52*days_worked
    #return the function               
    return miles_driven              
                  
def gallons_used_per_year(miles_driven,mpg):
    #create and initialize variables and constants
    gallons_used=0.0
    #process
    gallons_used=(miles_driven/mpg)
    #return the function
    return gallons_used
    
def emission_per_year (gallons_used):
    #create and initialize variables and constants
    emission=0.0
    #process
    emission=co2*gallons_used
    #return the function
    return emission
    
def main():
    #create and initialize variables and constants
    days_worked=0
    distance=0.0
    miles_driven=0.0
    mpg=0.0
    gallons_used=0.0
    emission=0.0
    #input
    distance=float(input("Enter the distance driven in miles "))
    days_worked=int(input("Enter the number of days  worked "))               
    mpg=float(input("Enter the mpg of the car "))
    #call the functions and display the returned values
    miles_driven= yearly_miles_driven (days_worked,distance)
    gallons_used=gallons_used_per_year(miles_driven,mpg)
    emission=emission_per_year(gallons_used)
    #output
    print("Distance to work \t MPG of vehicle \t Number of days/week \t Emissions for a year")
    print(format(distance, '.2f'), "miles \t\t", format(mpg, '.2f'), "mpg \t\t",days_worked,
          '\t\t\t', format(emission, '.2f'))       
main()              
              
              
                   
    
 

