#Giovanni Sanchez

if __name__ == "__main__":
    def encode(astring):
        outstring = ""
        for each in astring:
            newint = int
            if int(each) < 7:
                newint = int(each) + 3
            else:
                if each == "7":
                    newint = 0
                if each == "8":
                    newint = 1
                if each == "9":
                    newint = 2
            outstring += str(newint)
        return outstring

    def decode(astring):
        ostring = ""
        for each in astring:
            newint = int
            if 3 < int(each) <= 9:
                newint = int(each) - 3
            else:
                if each == "0":
                    newint = 7
                if each == "1":
                    newint = 8
                if each == "2":
                    newint = 9
            ostring += str(newint)
        return ostring

        pass

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        opt = input("Please enter an option: ")
        print()

        if opt == "1":
            string_enc = input("Please enter your password to encode: ")
            encoded_string = encode(string_enc)
            print("Your password has been encoded and stored!\n")

        if opt == "2":
            solved = decode(encoded_string)
            print(f"The encoded password is {encoded_string}, and the original password is {solved}.")

        if opt == "3":
            break