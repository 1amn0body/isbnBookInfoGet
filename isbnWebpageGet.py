import getThalia
import getGBooks

def getter(ipt):
    if (len(ipt) == 13) or (len(ipt) == 10):
        #find isbn 13 or 10
        infos = getThalia.findInfos(ipt)
        if infos is None:
            infos = getGBooks.findInfos(ipt)

        #find isbn 10 if nothin for isbn 13 found
        if len(ipt) == 13 and infos is None:
            try:
                infos = getThalia.findInfos(ipt[3:])
            except Exception as e:
                infos = None

            if infos is None:
                try:
                    infos = getGBooks.findInfos(ipt[3:])
                except Exception as e:
                    infos = None

        return infos
    return None

#isbn = ["9783442268160", "9780553499148", "9781420958713", "9783423252812", "9783426281550", "3426281554", "3841907350"]

while True:
    print()
    ipt = input("Eine ISBN oder 'X' angeben: ").lower()

    if ipt == "x":
        print("Beende...")
        break
    else:
        print(getter(ipt))
