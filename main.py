def encode(pwd):
    encoding = []
    encoded = 0
    encoding[:] = pwd
    for i in range(0,len(encoding)):
        encoded = encoded*10+int(encoding[i]) + 3
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
            print(f"The encoded password is {password}, and the original password is {"x"}.\n")
        elif choice == 3:
            break