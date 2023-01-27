#import random module

import random

def random_num(number):
    #create a loop to generate random numbers
    for count in range ( quantity_of_numbers):
        number=random.randint(1,500)
    # convert the numbers to a string and write them to the file
        random_numbers.write(str(number)+ '\n')
    return random_num

def main():
    # Open the random_num.txt file
    random_numbers = open('random_num.txt', 'r')
    #declare and initialize variables
    quantity_of_numbers=0
    total=0.0
    count=0.0
    #ask the user how many random numbers wants to be holded
    quantity_of_numbers=int(input('How many random numbers do you want to be holded to the file? '))
    
    #create a loop to read the file
    for line in random_numbers:
        print(line)
        total=total+float(line)
        count=count+1
    #close the file
    random_numbers.close()
    
    #print the random numbers and total
    print ('The list of random numbers: ',count)
    print('the total is',format(total,'.2f'))
     
main()
