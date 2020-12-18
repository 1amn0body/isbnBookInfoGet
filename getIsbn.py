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
            newCheckedIpt = isbnValidator.isbn13_10ReplaceCheckDigit(checkedIpt)

            #test with isbn 10
            infos = getThalia.findInfos(newCheckedIpt)
            if infos is None:
                infos = getHugendubel.findInfos(newCheckedIpt)
                if infos is None:
                    infos = getGBooks.findInfos(newCheckedIpt)

        try:
            infos.append(checkedIpt)
        except Exception as e:
            raise
        return infos
    return None
