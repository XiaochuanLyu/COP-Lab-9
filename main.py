#Harry Lyu
#Partner: Jessica Wu

def encode(pwd):
    encoded = []
    encoded[:] = pwd
    for i in range(0,len(encoded)):
        if (int(encoded[i]) + 3) > 9:
            encoded[i] = int(encoded[i]) - 7
        else:
            encoded[i] = int(encoded[i]) + 3
    return encoded

def decode(pwd):
    decode = []
    decode[:] = pwd
    for i in range(0,len(decode)):
        if (int(decode[i]) - 3) < 0:
            decode[i] = int(decode[i]) + 7
        else:
            decode[i] = int(decode[i]) - 3

    return decode

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
            decode_list = decode(password)
            decoded_password = ""
            for i in range (len(decode_list)):
                decoded_password += str(decode_list[i])
            print(f", and the original password is {decoded_password}.\n")
        elif choice == 3:
            break
        else:
            print("Please enter valid choice number!\n")