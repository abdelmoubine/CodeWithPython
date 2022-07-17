username = input("Please enter a username to get strated: ")
print("Hello, " + username.upper() + " and welcome to our game")

###################
password = "0000" #
word = ""         #
count = 0         #
time = 3          #
timeout = False   #
###################

while word != password and not(timeout):

    if count < time:
        word = input("Enter password: ")
        count += 1
        if password == word:
            print(username.upper() + ", you get the password ♥")
    else:
        timeout = True
    if timeout:
        print(username.upper() + ", Sorry out of try ↓")
        print("The Correct password is: " + password + ", you can try again")