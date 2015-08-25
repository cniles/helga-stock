"""Plugin that uses the Yahoo public stock quote api to provide some
information about a stocks current status"""

import urllib, urllib2, json

from helga.plugins import command

_HELP_TEXT = 'Displays stock information'

YQ_URL = 'https://query.yahooapis.com/v1/public/yql?'

@command('stock', help=_HELP_TEXT)
def stock(client, channel, nick, message, command, args):
    """ Entry point for stock command  """

    options = {
        'format': 'json',
        'env':'store://datatables.org/alltableswithkeys'
    }

    options['q'] = 'select symbol, Change, Name, LastTradePriceOnly\
    from yahoo.finance.quote where symbol = "{symbol}"'.format(symbol=args[0])

    result = json.loads(urllib2.urlopen(YQ_URL + urllib.urlencode(options)))

    phrase = '{Name} ({symbol}) is priced at {LastTradePriceOnly} ({Change})'

    return phrase.format(**result['query']['results']['quote'])
