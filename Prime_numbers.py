x = int(input("\nI will quote all the prime numbers from 2 up to this number: "))
# note that 1 is not considered as a prime number
j = 0

for n in range(2, x+1):
    for i in range(2, n):
        if n % i == 0:
            break
        
    else:
        print(str(n))
        j += 1

print("There are " +str(j)+ " prime numbers from 2 up to " +str(x))
