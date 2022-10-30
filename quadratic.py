import math
#Create a quadratic equation solver
#Create a function called quadratic that takes three parameters
def quadratic(a, b, c):
    #Create a variable called discriminant and assign it the value of the discriminant
    discriminant = (b**2) - (4*a*c)
    #If the discriminant is less than 0, return "No real solutions"
    if discriminant < 0:
        return "No real solutions"
    #Otherwise, if the discriminant is equal to 0
    elif discriminant == 0:
        #Create a variable called x and assign it the value of the solution
        x = -b/(2*a)
        #Return the solution
        return x
    #Otherwise, if the discriminant is greater than 0
    else:
        #Create a variable called x1 and assign it the value of the first solution
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        #Create a variable called x2 and assign it the value of the second solution
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        #Return the two solutions
        return x1, x2

#Create a function called main that takes no parameters
def main():
    #Create a variable called a and get user input
    a = float(input("Enter a: "))
    #Create a variable called b and get user input
    b = float(input("Enter b: "))
    #Create a variable called c and get user input
    c = float(input("Enter c: "))
    #Create a variable called solutions and assign it the return value of the quadratic function
    solutions = quadratic(a, b, c)
    #If the solutions are a tuple
    if type(solutions) == tuple:
        #Print the two solutions
        print("The solutions are", solutions[0], "and", solutions[1])
    #Otherwise, print the solution
    else:
        print("The solution is", solutions)

#Call the main function
main()
