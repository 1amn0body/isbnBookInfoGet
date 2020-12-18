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
            pass

        # better readability for external software (separator: ~)
        if infos is not None:
            authors = ""
            for i in infos[2]:
                authors += str(i) + "~"

            fullOutput = str(infos[0]) + "~" + str(infos[1]) + "~" + authors + str(infos[3])
            return fullOutput
        else:
            return None
    return None
