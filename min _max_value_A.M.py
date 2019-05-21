import random
lst = []
for i in range(6):
    lst.append(random.randint(100, 500))
print(lst)  
min_value = lst[0]
min_indx = 0
for i in range(1, len(lst)):
    if min_value > lst[i]:
        min_value = lst[i]
        min_indx = i
    
print("minimum_value :" , min_value)
print("mininmum_index :", min_indx)
max_value = lst[0]
max_indx = 0
for i in range(1, len(lst)):
    if max_value < lst[i]:
        max_value = lst[i]
        max_indx = i
print("maximum_value :" , max_value)
print("maxinmum_index :", max_indx)
sum_of_obs = 0
for num in lst:
     sum_of_obs += num
print("sum_of _observation :", sum_of_obs)
no_of_obs = len(lst)
mean = sum_of_obs / no_of_obs
print("Mean :", mean)



   



