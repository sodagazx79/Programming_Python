#lab 5
#Programmer: zahra sodagartojgi 
#Language: Python 3.9.2 
#population.py

#declare variables

starting_n_organisms=0 
average_increase=0.0
days=0
population=0.0

#get the input

starting_n_organisms=int(input("Enter the value of starting count of organisms: "))
average_increase=float(input("Average daily increase [%]: ")) / 100
days=int(input("Enter number of days to multiply: "))

print("Day Approximate\tPopulation")
for days in range(starting_n_organisms,days+2):
    starting_n_organisms += population
    population = starting_n_organisms * average_increase
    print(days - 1, '\t',format(starting_n_organisms,'.6f'))



 
