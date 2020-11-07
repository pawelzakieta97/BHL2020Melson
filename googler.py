from googlesearch import search
import requests

# to search 
query = "ean: 5902198161035"
VOCABULARY = {'metal': ['puszka', '330ml', '330 ml', '330 ML', '250ml', '250 ml', 'metal', 'aluminium'],
              'plastic': ['bottle', '2l', '2L', '1,5l', 'plastik'],
              'paper': ['papier', 'carton', 'karton', 'paper']}


def get_type(query):
    best_class = None
    urls = [url for url in search(query, num=5, stop=5, pause=0.5)]
    freq = {}
    for url in urls:
        if '.pdf' in url:
            continue
        try:
            r = requests.get(url)
        except:
            continue
        best_frequency = 0
        for trash_type in VOCABULARY.keys():
            frequency = 0
            for keyword in VOCABULARY[trash_type]:
                try:
                    count = r.content.decode('utf-8').upper().count(keyword.upper())
                except UnicodeDecodeError:
                    continue
                frequency += count
                freq[keyword] = count
                if frequency > best_frequency:
                    best_frequency = frequency
                    best_class = trash_type
            print(trash_type, frequency)
    return best_class


if __name__ == '__main__':
    print(get_type(query))
