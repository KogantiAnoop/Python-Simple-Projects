def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the half-yearly compounded interest rate (less than 1): "))
    halfInv = eval(input("Enter the half-yearly investment rate (less than 1): "))
    addOn = halfInv * principal #Used to determine the half yearly investment that is added
    for i in range(20): #I upped the range to 20 instead of 10 to account for the half-yearly compound interest.
        principal = (principal) * (1 + (apr * 0.5)) + addOn
        '''
        since i is being used as years as well, I have to shed out the random years given by i (0,2,4, etc).
         To do this, I used modulus to remove those extra loop numbers and ultimately get odd integers.
         '''
        if i % 2 != 0:
        
            '''
            Odd integers, however, are still not the numbers I would want to use.
            This is because i would ultimately result in the years becoming 1,3,5,7, ... 19.
            we are currently only attempting to get to year 10, and year 19 is not the year
            but rather the amount of times the loop occurred. To fix this,
            I divided these numbers by 2 and added 0.5 to get the appropriate years.
            Finally I nested them to integrate it to being a double from an int. 
            '''
            print("The balance after year", int(i /2 + 0.5), "is", principal)
            
    print("The value in 10 years is:", principal)

main()
