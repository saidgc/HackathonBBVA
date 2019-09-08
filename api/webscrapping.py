import requests
import urllib.request
import time
# pip install beautifulsoup4    
from bs4 import BeautifulSoup


def facebook(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    likes = soup.find('span', attrs={'class': '_52id _50f5 _50f7'})
    for i in likes:
        print(i)
        numberLikes = i.replace('.','')
        break

    try:
        opinons = soup.find('span', attrs={'class': '_331d'})
        for i in opinons:
            print(i)
            numberOpinions = i
            break
    except NoneType as error:
        print(error)
        numberOpinions = 0

    return [numberLikes, numberOpinions]


if __name__ == "__main__":
    # url = 'https://www.facebook.com/FCCsecretariaacademica/'
    # url = 'https://www.facebook.com/chilismx/'
    url = 'https://www.facebook.com/XiaomiMexico/'

    print(facebook(url))

    # response = requests.get(url)

    # soup = BeautifulSoup(response.text, "html.parser")

    # likes = soup.find('span', attrs={'class': '_52id _50f5 _50f7'})

    # for i in likes:
    #     print(i)
    #     break

    # opinons = soup.find('span', attrs={'class': '_331d'})
    # for i in opinons:
    #     print(i)
    #     break
    # # print(likes)
