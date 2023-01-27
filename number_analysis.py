#lab 8
#Programmer: zahra sodagartojgi 
#Language: Python 3.9.2 
#number_analysis.py


#define a function to ask the user to get the values
  
def get_values():

    #ask user to enter the numbers
  
    print('Please enter 20 random numbers')

    #declare the values list
    
    values =[]

    #create a loop to get the numbers
        
    
    for i in range(20):
        
    #get the 20 random numbers from user
        
        value =int(input("Enter a random number " +str(i+1)+": "))
        
        #append each element to the list of values
        
        values.append(value)
            
    #return the values      
    return values
            

#define a num_calculation to do the calculation 

def num_calculation (numbers):

    #print the max
    print("The lowest number is: " + str(min(numbers))) 
    #print the min
    print("The highest number is: " + str(max(numbers))) 
    #print the sum
    print("The sum of the numbers is: " + str(sum(numbers))) 
    #print the average
    print("The average the numbers is: " + str(sum(numbers)/len(numbers)))

        

#define the main the function
def main():
    try:
        
        numbers = get_values()
        num_calculation(numbers)
    except ValueError:
        print('Input is not numerical')

#call main function
main() 
