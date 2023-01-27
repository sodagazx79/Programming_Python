#Activity
#Programmer: zahra sodagartojgi 
#Language: Python 3.9.2 
#write_read_sum.pyy

def get_save_data(num1,num2,num3):
    # Open a file for writing.
    outfile=open('numbers.txt','w')
    #return the function
    return get_save_data

def main():
    #open the numbers.txt file
    outfile = open('numbers.txt', 'w')
    #declare and initialize variables
    num1=0.0
    num2=0.0
    num3=0.0
    total=0.0
    # Get three numbers from the user
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    num3 = float(input('Enter another number: '))
    
    # Write the numbers to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
    
    # Close the file.
    outfile.close()
    # Add the three numbers.
    total = num1 + num2 + num3
    # Display the numbers and their total.
    print('Data was successfully saved to numbers.txt')
    print('The numbers are:', format (num1,'.2f'),format (num2,'.2f'),format (num3,'.2f'))
    print('Their total is:', format(total,'.2f'))
# Call the main function.
main()
