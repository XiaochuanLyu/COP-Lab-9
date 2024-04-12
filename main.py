def encode(pwd):
    encoded = []
    encoded[:] = pwd
    for i in range(0,len(encoded)):
        if (int(encoded[i]) + 3) > 9:
            encoded[i] = int(encoded[i]) - 7
        else:
            encoded[i] = int(encoded[i]) + 3
    return encoded

if __name__ == "__main__":
    password = 0
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print("The encoded password is ",end="")
            for i in password:
                print(i,end="")
            #Requires decoded password initialized for print
            print(f", and the original password is {"x"}.\n")
        elif choice == 3:
            break
        else:
            print("Please enter valid choice number!\n")