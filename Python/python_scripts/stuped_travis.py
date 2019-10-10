# stuped_travis

known_users =["alice","bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("HI! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
      print("Hello,{}!".format(name))
    remove=input("Would you like to be removed from the system (y/n)").strip().lower()
    
    if remove =="y":
         known_users.remove(name)
    elif remove == "n":
         print("No problem, I didn't want you to leave anyway!")
             
    else:
        Print("Hmmm I don't thank I have met you yet {}").format(name)
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me =="y":
             known_users.append(name)
        elif add_me == "n":
            print("No worries, See you around!")
            
                 
