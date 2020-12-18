import requests
from bs4 import BeautifulSoup as bs

def findInfos(isbn):
    infos = []

    url = "https://www.hugendubel.de/de/quickSearch?searchString="
    html_doc = requests.get(url + isbn).text

    soup = bs(html_doc, 'html.parser')
    #print(soup)

    #find section
    section = soup.find('div', {'id': "productPageMainInfoTitel"})
    #print(section.prettify())

    if section is not None:
        #find title
        try:
            title = section.find('h1').decode_contents().replace('\n', '')
            infos.append(title)
        except Exception as e:
            infos.append(None)

        #find series
        infos.append(None)

        #find author(s)
        try:
            author_s = section.find('div', {'id': "productPageAuthors"}).find_all('a')

            for i in range(len(author_s)):
                author_s[i] = author_s[i].decode_contents()

            infos.append(author_s)
        except Exception as e:
            infos.append(None)

        return infos
    return None

#isbn = ["9783442268160", "978-0-553499148", "978-1-420958713", "978-3-423252812", "978-3-426281550", "3-426281554", "3-841907350", "979-1234567896", "978-3453319974", "978-3-7657-2781-8"]
