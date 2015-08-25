import urllib, urllib2, json

from helga.plugins import command

_help_text = 'Displays stock information'

yq_url = 'https://query.yahooapis.com/v1/public/yql?'

@command('stock', help = _help_text)
def stock(client, channel, nick, message, cmd, args):

    options = {
        'format': 'json',
        'env':'store://datatables.org/alltableswithkeys'
    }
    options['q'] = 'select symbol, Change, Name, LastTradePriceOnly from yahoo.finance.quote where symbol = "{symbol}"'.format(symbol=args[0])

    f = urllib2.urlopen(yq_url + urllib.urlencode(options))

    result = json.loads(f.read())

    print result['query']['results']['quote']

    return '{Name} ({symbol}) is priced at {LastTradePriceOnly} ({Change})'.format(**result['query']['results']['quote'])
