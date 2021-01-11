from math import*
def prime_check(n):
    try:
        first_divisor = 0
        limit = ceil(sqrt(n)) + 1
        for i in range(2, limit+1):
            if n%(i)==0:
                first_divisor = i
                break
            else:
                pass
        
        if first_divisor == 0:
            print("Congratulations you find a prime number")
            return(True)
        
        else:
            print("This number is not prime because is divisible by {divisor}".format(divisor = first_divisor))
            return(False)
    except:
        return "Error"

def ask_if_prime():
    global prime_check
    while True:
        try:
            num = int(input("Enter a positive integer to check if it's prime or not: "))
            prime_check(num)
            break
        except:
            print("That's not a positive integer")
            ask_if_prime()
            break

ask_if_prime()