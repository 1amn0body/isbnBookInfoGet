def isbn13Validate(isbn13):
    #get checkDigit
    odd = 0
    even = 0

    for i in range(0, len(isbn13) -1, 2): # odd
        odd += int(isbn13[i])

    for i in range(1, len(isbn13) -1, 2): # even
        even += int(isbn13[i])

    checkDigit = str((10 - ((odd + (3 * even)) % 10)) % 10) # get check Digit

    # check checkDigit
    if isbn13[-1] == str(checkDigit):
        return isbn13
    return None

def isbn10Validate(isbn10):
    #get checkDigit
    checkDigit = 0
    for i in range(len(isbn10) -1):
         checkDigit += ((i+1) * int(isbn10[i]))

    checkDigit = checkDigit % 11

    #test checkdigit
    if isbn10[-1] == str(checkDigit):
        return isbn10
    return None

def isbn13_10ReplaceCheckDigit(isbn13):
    isbn10Unchecked = isbn13[3:]

    #get checkDigit
    checkDigit = 0
    for i in range(len(isbn10Unchecked) -1):
         checkDigit += ((i+1) * int(isbn10Unchecked[i]))

    checkDigit = checkDigit % 11

    #set checkDigit
    isbn10 = isbn10Unchecked[:-1] + str(checkDigit)

    return isbn10

def isbnValidate(isbn):
    # only numbers
    isbn = isbn.replace('-', '')
    try:
        isbn = str(int(isbn))
    except Exception as e:
        return None

    # test isbn 13
    if len(isbn) == 13:
        if isbn[:3] == '978':
            return isbn13Validate(isbn)
        elif isbn[:3] == '979':
            if isbn[3] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return isbn13Validate(isbn)

    # test isbn 10
    elif len(isbn) == 10:
        return isbn10Validate(isbn)

    return None
