import requests
import urllib.request
import time
# pip install beautifulsoup4
from bs4 import BeautifulSoup

from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/data', methods=['POST'])
def facebook():
    url = request.args['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    likes = soup.find('span', attrs={'class': '_52id _50f5 _50f7'})
    for i in likes:
        numberLikes = i
        numberLikes = str(numberLikes).replace('.', '')
        print(numberLikes)
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

    return jsonify({'likes': numberLikes, 'opinions': numberOpinions})


if __name__ == "__main__":
    app.run()
