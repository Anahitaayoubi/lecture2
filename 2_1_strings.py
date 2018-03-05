####################################
# following variables are the same #
####################################
str1=" Anahita "
str2='Anahita'

######################
## concat two string #
######################
family='Ayoubi'
full name= str1+family
print(full name)

greeting2=str1+" "+family
print(full name)
#
# print(("\'"+greeting2+" \'") * 3)
######################################
## some useful operations on strings #
######################################
print(greeting2.capitalize())
print(greeting2.upper())
print(greeting2.rsplit(' ')) # splitting the string by blank
print(greeting2.strip(' ')) # remove the blanks before and after the string

###########################################
### another sample of printing a varibale #
###########################################
#pi = 3.14
#print(pi)
#str_pi = str(pi)
#print("pi number is : ", pi)  # print each part of input separately
#print("pi number is : " + str(pi))  # concat two string
