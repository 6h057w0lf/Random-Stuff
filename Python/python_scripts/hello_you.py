#hello You

#ask for name

name = input("What is your name?: ")

# ask for age
age = input("how old are you?: ")

# ask where they live
city = input("What city do you live in?: ")

# ask what they enjoy
enjoy = input("What do you enjoy?: ")

# create output text

hello = "Your name is {} and you are {} years old. you live in {} and you enjoy {}."
output = hello.format(name, age, city, enjoy)

#print output
print(output)
