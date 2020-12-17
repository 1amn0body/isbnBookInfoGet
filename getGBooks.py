import requests, json, re
from bs4 import BeautifulSoup as bs

def findInfos(isbn):
    infos = []

    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    html_doc = requests.get(url + isbn).text

    soup = bs(html_doc, 'html.parser')

    #getJson
    sp = soup.prettify()

    # searching for unescaped double quotes
    match0 = re.search(r'""', sp)
    match1 = re.search(r'"--"', sp)

    while (match0 is not None) and (match1 is not None):
        match0 = re.search(r'""', sp)
        m = [match0.start() for match0 in re.finditer('""', sp)]
        for i in m:
            sp = sp[:i +1] + "\\" + sp[i +1:]

        #match1 = re.search(r'"--"', sp)
        m = [match1.start() for match1 in re.finditer('"--"', sp)]
        for i in m:
            if sp[i -1] != '\\':
                sp = sp[:i] + '\\' + sp[i:]

    jsonObj = json.loads(sp) # json out of multilineString

    if jsonObj is not None:
        try:
            volInfo = jsonObj["items"][0]["volumeInfo"]
        except Exception as e:
            return None

        # title
        try:
            infos.append(volInfo["title"])
        except Exception as e:
            info.append(None)

        #series
        infos.append(None)

        #author_s
        try:
            infos.append(volInfo["authors"])
        except Exception as e:
            infos.append(None)

        return infos
    return None
