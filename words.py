import urllib.request


def get_words():
    try:
        target_url = 'https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt'
        l = []
        for line in urllib.request.urlopen(target_url):
            t = line.decode('utf-8')[:-1]
            if len(t) == 5 and t.isupper() and t.isalpha():
                l.append(t)
            else:
                print(t)
        return l
    except Exception as e:
        print(e)
        return None
