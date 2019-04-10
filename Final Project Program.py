#Import csv

#filename= open(‘Crimes_-_2018.csv‘)
#Csv_filename = csv.reader(filename)

print("For more information type help for data descriptions, instructions on different")
command = input("Enter Command:")
while command != "exit":
    if command == "help":
        print("Options for categorical data: district,....")
        help_option = input("Enter help category:")
        if help_option == "district":
            print("something ")
            help_option = input("Enter help category:")
        elif help_option == "general":
                print("something2")
    elif command == "instruction":
        print("Choose Option 1, Option 2, Option 3")
        instruction = input("Enter instruction:")
        if instruction == "What does this function do?:":
            print("something3")
            #options = input("
        elif instruction == "well":
            print("something4")
    command = input("Enter Command:")
##        else:
##            print("Invalid Comment")
##            command = input("Enter Command:")
##    elif command.lower() == "exit":
##            return
##    if command == "option 3"
##
##
##for row in csv_filename:
##    



