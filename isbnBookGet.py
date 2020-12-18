import getThalia, getHugendubel, getGBooks
import isbnValidator

def getter(ipt):
    checkedIpt = isbnValidator.isbnValidate(ipt)

    if checkedIpt is not None and ((len(checkedIpt) == 13) or (len(checkedIpt) == 10)):
        #find isbn 13 or 10
        infos = getThalia.findInfos(checkedIpt)
        if infos is None:
            infos = getHugendubel.findInfos(checkedIpt)
            if infos is None:
                infos = getGBooks.findInfos(checkedIpt)

        #find isbn 10 if nothing for isbn 13 was found
        if len(checkedIpt) == 13 and infos is None:
            #make isbn 10 valid
            newCheckedIpt = isbnValidator.isbn13_10Replace(checkedIpt)

            #test with isbn 10
            infos = getThalia.findInfos(newCheckedIpt)
            if infos is None:
                infos = getHugendubel.findInfos(newCheckedIpt)
                if infos is None:
                    infos = getGBooks.findInfos(newCheckedIpt)

        return infos
    return None

#isbn = ["9783442268160", "978-0-553499148", "978-1-420958713", "978-3-423252812", "978-3-426281550", "3-426281554", "3-841907350", "979-1234567896", "978-3453319974", "978-3-7657-2781-8"]

print("Die Informationen sind nach dem Schema 'Titel, Buchreihe, Autor(en)' aufgebaut. Wenn Sie 'None' zurückbekommen, dann wurde nichts gefunden.")
print("Bitte beachten Sie, dass die Informationen möglicherweise fehlerhaft sind.")

while True:
    print()
    ipt = input("Eine ISBN oder 'X' angeben: ").lower()

    if ipt == "x":
        print("Beende...")
        break
    else:
        print(getter(ipt))
