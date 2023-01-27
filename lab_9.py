#using dictionaries
# Zahra Sodagartojgi
# Python 3.10.2
#lab_9


def main():

    #create a list for the rooms numbers
    rooms={'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411}
    #create a list for the instructors names
    instructors={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    #create a list for the time of classes
    meeting_time={'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'12:00 p.m.'}
    #ask the user to input the course number
    course = input('Enter the course number: ')

    #create an if statment 
    if  course not in rooms:
        #give a message that the input is not valid
        print(course, 'is an invalid course number.')
    else:
        #print the room number
        print('The room number for the course',course, 'is: ',rooms[course])
        #print the instructor's name
        print("The instructor's name is : ",instructors[course])
        #print the meeting time for the course
        print('The meeting time is: ',meeting_time[course])
#call the main
main()
