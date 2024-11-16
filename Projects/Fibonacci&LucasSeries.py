import math
import matplotlib.pyplot as plt
import numpy as np



def lucas_series(n):
    no = 2
    n1 = 1
    new = 0
    if(n == 0):
        return 2
    elif(n==1):
        return 1
    else:
        for i in range(2,n + 1):
            new = no + n1 #becomes the next part of the series and a footholder for replacement
            no = n1 #no becomes n1 to go up the series
            n1= new #n1 then gets replaced with new so that the next lucas series can take place
        return new
def fibonacci_series(n):
    no = 0
    n1 = 1
    new = 0
    if( n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        for i in range(2,n + 1):
            new = n1 + no #similar to Lucas series, the new acts as the next part of the series and a footholder for replacement for n1 in the future
            no = n1 #no gets replaced with n1 in preparation for the next stage of the series
            n1  = new
        return new
        
def fibonacci_error(N, φ):
    
    if (fibonacci_series(N-1) == 0): # to avoid the problem where the denominator equals 0, resulting in a crash
        return
    else:
        E1 = abs((fibonacci_series(N)/fibonacci_series(N-1)) - φ) #equation to solve the fibonacci error and return it
        return E1
    
def main():
    N = int(input("Enter an integer N (N > 2): "))
    K = int(input("Enter an even integer K (2 <= K < N): "))
    while N <= 2: #Incase they dont type a number greater then 2, while loop to continuously ask them to change it to be appropriate
        N = int(input("Retype a number greater than two: "))
    while K % 2 != 0 and K < 2: #Incase number isnt even or is less than 2, re-input K
        K = int(input("retype an even number greater than 2: "))


    var = 0
    print("Lucas series (up to N=10): [", end = "")
    while(var != N):
        print(str(lucas_series(var)) + ", ", end="") #to print out the string with all of the lucas series until the specified number N
        var +=1
    print(str(lucas_series(N)) + "]")


    var1 = 0
    print("Fibonacci series (up to N=10): [", end = "")

    while(var1 != N):
        print(str(fibonacci_series(var1)) + ", ", end = "") #to print out the string with all of the fibonacci series until the specified number N 
        var1 += 1
    print(str(fibonacci_series(N)) + "]")


    GR = (1 + math.sqrt(5))/2
    print("Golden Ratio(φ):",GR)
    E1 = fibonacci_series(N - K) #Implementing the equations seperately for organization to ultimately determine  right hand and left hand sides of the equation
    E2 = fibonacci_series(N + K)
    E3 = fibonacci_series(N) * lucas_series(K)
    print("Left-hand side of equation (1): F[N-K] + F[N+K] =", E1 + E2)
    print("Right-hand side of equation (1): F[N] * L[K] =", E3)
    if(E1 + E2 == E3):
        print("Equation(1) holds true!")
    else:
        print("Equation(1) doesnt hold true")


    if N < 40:
        print("fibonacci error at N =", str(N) + ":",round(fibonacci_error(N, GR),K))
    else:
                        #if statement to follow directory
        print( "Error: Value too small")
    print("The natural logarithm of the Fibonacci number up to N=10: [" + str(-math.inf), end = "") #to print out the string with all of the nl's of the fibonacci numbers
    var2 = 1
    while var2 <= 10:
          val= math.log(fibonacci_series(var2))
          print("," , round(val, 2), end = "")
          var2 += 1
    print("]")
        
    plt.figure() #First Plot
    plt.title('the ratio FN / FN-1 for the Fibonacci series against N')
    plt.xlabel("N")
    plt.ylabel("f(N)/F(N-1)") #Overall just labels, etc for the plot
    x_values = list(range(N + 1)) #Gets the value of N that is inputed by individual on plot
    y_values = []
    for i in range(N+1):
        if fibonacci_series(i) ==0: #Removes the risk of crash from 0 denom
            y_values.append(0)
        else:
            y_values.append(fibonacci_series(i + 1)/fibonacci_series(i)) #gets y value and adds to the y value list
    plt.plot(x_values,y_values,label = 'Fibonacci Ratio FN/FN-1') #plots the equation
    plt.axhline(y=GR,linestyle = '--', color = 'red', label ='Golden Ratio(φ)')#plots golden ratio horiz. line using axhline
    plt.legend(loc = 'lower right') #legend design


    plt.figure() #second plot
    plt.title('Fibonacci Error values against N')
    plt.xlabel("N")
    plt.ylabel("Error Values")
    x1_values = list(range(N+1)) 
    y1_values = []
    for i in range(N+1): #obtain list of x values based off User input and fibonacci error
        if(fibonacci_error(i, GR) is None):
            y1_values.append(math.inf) #incase the value becomes undefined(probably unnecessary but says in instructions to use)
        else:
            y1_values.append(fibonacci_error(i, GR)) #obtain y values and add them to list
    plt.plot(x1_values,y1_values) 

    plt.figure() #3rd plot
    plt.title('Fibonacci and Lucas sequences growth VS. quadratic functions')
    plt.xlabel("N")
    x2_values = list(range(N+1))
    y2_values = []# y values for fib series
    y3_values = []# y values for lucas series
    y4_values = []# y values for quadratic
    for i in range(N+1): #loop to get all the y values properly integrated within the list based off user input
        y2_values.append(fibonacci_series(i))
        y3_values.append(lucas_series(i))
        y4_values.append(i**2)
    plt.plot(x2_values,y4_values, color = 'blue', label = 'Quadratic')
    plt.plot(x2_values,y2_values,color = 'orange',label = 'Fibonacci' )#}plot all the points for each graph
    plt.plot(x2_values,y3_values, color = 'green', label = 'Lucas') 
    
    plt.legend(loc = "upper left")
    
    
    plt.show()

    
    
    

main()



        
        
