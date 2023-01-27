#lab 7
#Programmer: zahra sodagartojgi 
#Language: Python 3.9.2 
#lab7.py

def main():

    file_object=None
    while file_object==None:
        
        # input name of file
        filename=input('Enter the file name ')
        # open the file
        if (filename.lower()=="labph.txt"):
             file_object=open("LabpH.txt","r")
        elif (filename.lower()=="turbidity.txt"):
            file_object=open("Turbidity.txt","r")
        else:
            print("The file is not valid, Please try again")
            
    try:
        
       #read the title
        title=file_object.readline().rstrip('\n').lower
        #declare and initialize variables
        total=0.0
        count=0
        average=0.0
        #increment loop
        for line in file_object:
            #read a line of data and convert it numerical value
            total=total+float(line)
            count+=1
            
        # close file 
        file_object.close()
        #calculate the average
        average=total/count
        
    except Exception as err:
        print(err)
    else:
        
        #print the random numbers and total
    
        print('The average is',format(average,'.2f'))
  
    
#call the main     
main()
        
