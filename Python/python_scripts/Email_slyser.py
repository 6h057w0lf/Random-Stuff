# Email slyser

#get user email address

email=input("What is your email address?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") +1 :]

                           
# format messages

output= "Your username is {} and Your domain name is {}".format(user, domain)

# Display output messages

print(output)
