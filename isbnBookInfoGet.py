import getIsbn

print("The information is structured according to the scheme 'title, book series, author(s), input ISBN'. If you get 'None' back then nothing was found.")
print("Please note that the information may be incorrect.")

while True:
    print()
    ipt = input("Eine ISBN oder 'X' angeben: ").lower()

    if ipt == "x":
        print("Beende...")
        break
    else:
        out = getIsbn.getter(ipt)
        if out is not None:
            print(out.replace('~', ', '))
        else:
            print(None)

#isbn = ["9783442268160", "978-0-553499148", "978-1-420958713", "978-3-423252812", "978-3-426281550", "3-426281554", "3-841907350", "979-1234567896", "978-3453319974", "978-3-7657-2781-8"]
