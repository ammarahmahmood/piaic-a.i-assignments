

def ammmarah_0():
    print("ammarah\nmahmood\n9th")
ammmarah_0()

print("                                        mark_sheet")
print("_______________________________________________________________________________________________________")
print("| subjects                               marks                                          obtained_marks|")
print("|_____________________________________________________________________________________________________|")
a = int(input("|chemistry                                100                                                      "))
b = int(input("|english                                   75                                                      "))
c = int(input("|computer                                 100                                                      "))
d = int(input("|sindhi                                    75                                                      "))
e = int(input("|pak studies                               75                                                      "))
print("|______________________________________________________________________________________________________")
total = a + b + c + d + e 
print("\n total_marks                                   425                                                 " +str(total))
percentage = (total / 425)*100

print("\n Percentage :" + str(percentage))

if percentage >= 80:
     print ("grade : A+")
elif percentage >= 70:
     print ("grade : A")
elif percentage >= 60:
     print("grade :B")
elif percentage >= 50:
     print ("grade :C")
else:
     print ("fail")