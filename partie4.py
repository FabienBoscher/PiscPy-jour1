def ask_user() :
    while (mot := input("Saisissez un mot : ")) != "exit":
        print ("Tu as tapé ", mot)

ask_user()