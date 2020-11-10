import chardet
import requests

from bs4 import BeautifulSoup

def get_encoding(infile):
    rawdata = open(infile, 'rb').read()
    result = chardet.detect(rawdata)
    return result['encoding']

def genres_list():
    URL = 'https://www.musicgenreslist.com'

    response = requests.get(URL)

    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(class_='entry-content')

    genres_list = content.div.div

    adds = genres_list.find_all('p')

    for add in adds:
        add.decompose()

    for child in genres_list:
        print(child.name)

def genre_mapping(genre):
    genres_map = {
        'alternative': [
            'punk',
            'alternative rock',
            'britpunk',
            'crossover thrash',
            'crust punk',
            'emo',
            'experimental rock',
            'folk punk',
            'goth',
            'gothic rock',
            'grunge',
            'lo-fi'],
        'anime': 'anime',
        'blues': 'blues',
        'children': ['children', 'lullaby', 'stories'],
        'classical': ['classical', 'choral', 'opera', 'symphonic'],
        'country': 'country',
        'dance': ['dance', 'edm', 'techno', 'trance', 'house'],
        'electronic': ['ambient', 'electronic', 'electro'],
        'enka': 'enka',
        'pop': 'pop',
        'folk': 'folk',
        'hip-hop': 'hip hop',
        'rap': 'rap',
        'christian & gospel': ['christian', 'cristiana', 'cristiano', 'gospel'],
        'instrumental': 'instrumental',
        'jazz': 'jazz',
        'salsa': 'salsa',
        'bachata': 'bachata',
        'bossa': 'bossa',
        'metal': 'metal',
        'new age': ['meditation', 'healing', 'relaxation'],
        'progressive': 'progressive',
        'r&b and soul': ['r&b', 'soul'],
        'reggae': 'reggae',
        'rock': 'rock',
        'soundrack': ['tv', 'movie']
    }

    for key, value in genres_map.items():
        if value in genre:
            return key

if __name__ == "__main__":
    genres_list()