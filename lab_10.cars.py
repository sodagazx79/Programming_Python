#lab 10
# Zahra Sodagartojgi
# Python 3.10.2
#car_class.py



#import the car class
import car

#define the main function
def main():
    # create a Car object
    my_car = car.Car('2004','Toyota')
    # calls the accelerate method
    print("The car is accelerating . . .")
    #create a loop for accelaration
    for i in range(5):
        my_car.accelerate()
        print ("The car's speed is",my_car.get_speed())


    # calls the brake method five times.
    print ("The car is decelerating . . .")
    #create a loop for decelaration
    for i in range(5):
        my_car.brake()
        print("The car's speed is:",my_car.get_speed())
        
#call the main
        
main()

