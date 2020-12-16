import requests
from bs4 import BeautifulSoup as bs

def findInfos(isbn):
    try:
        isbn = str(int(isbn))
    except Exception as e:
        return None

    infos = []

    url = "https://www.thalia.de/suche?sq="
    html_doc = requests.get(url + isbn).text

    soup = bs(html_doc, 'html.parser')

    #find section
    section = soup.find('section', {'class': ["artikel-details"]})
    #print(section.prettify())

    if section is not None:
        #find title
        try:
            title = section.find('h3').decode_contents()
            infos.append(title)
        except Exception as e:
            infos.append(None)

        #find series
        try:
            series = section.find('a', {'class': ["serie"]}).decode_contents()
            infos.append(series)
        except Exception as e:
            infos.append(None)

        #find author(s)
        try:
            author_s = section.find('ul', {'class': ["autoren-liste"]}).find_all('a')

            for i in range(len(author_s)):
                author_s[i] = author_s[i].decode_contents()

            infos.append(author_s)
        except Exception as e:
            infos.append(None)

        return infos
    return None
