# distance = d
d = float(input('enter_value_in_feet:'))
# 1ft = 12inch
# 1ft = 1/3yard
# 1ft = 5280mile
ft_into_inches = (d)*12
ft_into_yard = (1/3)*(d)
ft_into_mile = (1/5280)*(d)
print('d =', ft_into_inches, 'inches')
print('d =', ft_into_yard, 'yard')
print('d =', ft_into_mile,'mile')