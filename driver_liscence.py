#lab 8
#Programmer: zahra sodagartojgi 
#Language: Python 3.9.2 
#driver's_liscence.py


#define the main function
def main():
    #create traps
    
    try:
    
        #the list of the correct answers to this test
        correct_answers=['B','C','A','A','D','D','B','B','C','C','D','A','B','A','D','A','C','B','D','A']
        # creating a list of student answers
        student_answers = []
        #open the student_answers.txt file for reading
        file=open('studenT_answers.txt','r')
        #read the file
        student_answer=file.readlines()
        #close the file
        file.close()

        #declare and initialize variable mark
        mark=0
        #wroong answers list in order to storing the wrong answers
        wrong_answers=[]

        #create a  loop for calculating right or wrong answers
        for i in range (0,len(student_answer)):
            if student_answer[i]== correct_answers[i]:
                mark +=1
            else:
                wrong_answers.append(i)
            
        if mark >=15:
            print ('You passed the exam')
            
        else:
            print('You failed the exam')
        #show how many answers did they correct
        print('Number of correct answers: ', mark)
        #show how many answers did they incorrect
        print('Number of incorrect answers: ', len(student_answer)-mark)
        #show the incorrect answers
        print('Your incorrect questions: ',wrong_answers)
        

        #make exceptions for the programm
    except IOError:
        print('There is an error trying to read the file')
    except ValueError:
        print('Non numeric data found in the file')
    except IndexError:
        print('Invalid index')

#call the main function
main()
            
            
