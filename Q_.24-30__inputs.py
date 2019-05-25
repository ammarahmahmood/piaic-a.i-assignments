#Q _24_sum_of_n_positive_integers


N = int(input('enter positive integesr:'))
for i in range (1,N+1):
    sum_num = (i*(i+1))/2
print('sum_of_n_positive_integers =',sum_num)


#Q _25_sum_of_an_integer

n = input("enter an integer:")
sum_of_an_integer=0
for i in n:
    sum_of_an_integer  +=  int(i)
print("sum of a digit is:", sum_of_an_integer)  

#Q_26_binary_oct_hexa:

dec = int(input('enter decimal num:'))
print(dec,' = ',bin(dec), 'binary.')
print(dec,' = ',oct(dec), 'octal.')
print(dec,' = ',hex(dec), 'hexadecimal.')


#Q_27 binary into decimal:
binary = input('enter binary num')
power = len(binary)-1
dec = 0
for i in binary:
    dec +=int(i)*2**power
    power = power-1
print(binary,'binary', '=', dec,'decimal')

# Q_ 28 octal into decimal:
octal = input('enter octal num')
power = len(octal)-1
dec = 0
for i in octal:
    dec +=int(i)*8**power
    power = power-1
print(octal,'octal', '=', dec,'decimal')

# Q_ 29_ hexadecimal into decimal:

hexa = input('enter hexa num')
power = len(hexa)-1
dec = 0
for i in hexa:
    dec +=int(i)*16**power
    power = power-1
print(hexa,'hexa', '=', dec,'decimal')
# Q_30 count caracter:
string = "100001"
count = 0
for i in string: 
    if i == '0': 
        count = count + 1  
print ("Count of 0 in 100001 : " ,  str(count))
