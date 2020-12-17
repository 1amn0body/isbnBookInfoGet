import getThalia
import getGBooks
import isbnValidator

def getter(ipt):
    checkedIpt = isbnValidator.isbnValidate(ipt)

    if checkedIpt is not None and ((len(checkedIpt) == 13) or (len(checkedIpt) == 10)):
        #find isbn 13 or 10
        infos = getThalia.findInfos(checkedIpt)
        if infos is None:
            infos = getGBooks.findInfos(checkedIpt)

        #find isbn 10 if nothing for isbn 13 was found
        if len(checkedIpt) == 13 and infos is None:
            infos = getThalia.findInfos(checkedIpt[3:])

            if infos is None:
                infos = getGBooks.findInfos(checkedIpt[3:])

        return infos
    return None

#isbn = ["9783442268160", "9780553499148", "9781420958713", "9783423252812", "9783426281550", "3426281554", "3841907350"]

print("Die Informationen sind nach folgendem Schema aufgebaut: 'Titel, Buchreihe, Autor(en)' Wenn Sie 'None' zurückbekommen, dann wurde nichts gefunden.")
print("Bitte Beachten Sie, dass diese möglicherweise fehlerhaft sind oder leicht von der originalen ISBN abweichen.")

while True:
    print()
    ipt = input("Eine ISBN oder 'X' angeben: ").lower()

    if ipt == "x":
        print("Beende...")
        break
    else:
        print(getter(ipt))
