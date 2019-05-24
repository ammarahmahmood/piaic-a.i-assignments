prinp_amount = int(input('pin.p_amonut:'))
int_rate = float(input('int_rate:'))
yrs = int(input('yrs:'))
future_value = prinp_amount * ((1+int_rate)) ** yrs 
print ('future_value:', future_value )