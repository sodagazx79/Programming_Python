#lab 10
# Zahra Sodagartojgi
# Python 3.10.2
#pet_class.py

#import the pet class

import pet

#define the main function
def main ():

    # Creating the default Pet object
    my_pet = pet.Pet()
    # getting input from user
    name = input('Please enter the name : ')
    my_pet.set_name(name)

    #get the animal type from the user
    animalType = input('Please enter animal Type : ')
    my_pet.set_animal_type(animalType)

    #get the animal age
    age = input('Please enter the age of Pet : ')
    my_pet.set_age(age)
    # Printing the result
    print('The pet name is : ' , my_pet.get_name())
    print('The animal Type is :', my_pet.get_animal_type())
    print('The Pet age is : ', my_pet.get_age())

#call the main function
main()
