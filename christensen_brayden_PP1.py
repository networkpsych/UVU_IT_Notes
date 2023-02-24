import csv

def main():
    """
    Declare dictionary
    open the file
        loop over file with csv.DictReader
            add file contents to dictionary
    
    print welcome statement and dash buffer
    while true
        get user input for a state
        if the user input is equal to x, break loop
        try
            print state and state capital with user input
        except for key errors
            print that users entry is not in the database
            continue
    """
    tmp_dict = {}
    with open("states.txt", 'r') as file:
        for item in csv.DictReader(file):
            tmp_dict[item['State'].upper()] = item['Capital']
    
    print(f"Welcome to Brayden's State Capital Lookup App!\n{'-'*40}\n")
    while True:
        user = input("Please enter a State and I will return the Capital (x to exit): ")
    
        if user.lower() == 'x':
            break
        try:
            print(f"\nState: {user.title()}\nCapital: {tmp_dict[user.upper()]}\n")
        except KeyError:
            print(f"\nCould not find {user} in the database.\n")
            continue

if "__main__"==__name__:
    main()