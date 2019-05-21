n = int(input("enter a number"))
if n <= 1:
    print("is not prime")
else:
  for i in range(2, n):
     if n % i == 0:
        print("is not prime")
        break
  else:
     print("is prime")
