import urllib.request,json
from .models import Quote

# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

def getQuotes(): 
    with urllib.request.urlopen(base_url) as url:
        quotesResponse = url.read()
        lll = json.loads(quotesResponse)
        print(lll)
        r = []
        id = lll.get('id')
        author = lll.get('author')
        quote = lll.get('quote')

        quoteObject = Quote(id,author,quote)
        r.append(quoteObject)
        return r 



