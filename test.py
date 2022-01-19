
# 1. Read in name and age.
# whenever I say type I mean string, integer float

name = input("Enter your name: ")
age = input("Enter your age: ") 


# changing types
name_type = str(name)
age_type = float(age)



#converting age to dog years
dog_years = age_type * 7

# I can't believe that Name is Age years old! That's Age*7 in dog years!
age_float = float(age_type)
dog_float = float(dog_years)


sentence = "I can't believe that " + name_type + " is " + str(age_float) + " years old! That's " +  str(dog_float)  +  " in dog years!"

print(sentence)

