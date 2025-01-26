import requests
import json

api_key = 'DIR5RSL9GUR92X0Z'
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# base_url = 'https://www.alphavantage.co/query?function='
forex_tags = {
    'daily':'FX_DAILY',
    'weekly': 'FX_WEEKLY',
    'monthly' : 'FX_MONTHLY',
    'news_general' : 'NEWS_SENTIMENT'
}


def url_builder(forex_time = 'daily'):
    feeds_url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'
    url = ''
    if forex_time == 'daily':
        url = f"https://www.alphavantage.co/query?function={forex_tags['daily']}&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey={api_key}"
    elif forex_time == 'weekly':
        url = f"https://www.alphavantage.co/query?function={forex_tags['weekly']}&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey={api_key}"
    elif forex_time == 'monthly':
        url = f"https://www.alphavantage.co/query?function={forex_tags['monthly']}&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey={api_key}"
    elif forex_time == 'news_general':
        url = f"https://www.alphavantage.co/query?function={forex_tags['news_general']}&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=1000&apikey={api_key}"
    return url





def read_forex_data(url):
    r = requests.get(url)
    data = r.json()
    feed_list = []
    for x in range(len(data['feed'])):
        feed_list.append(data['feed'][x])
    # clean_data = json.dumps(feed_list)
    clean_data = ', '.join(json.dumps(item) for item in feed_list)
    return clean_data


url = url_builder(forex_time='news_general')

data = read_forex_data(url)
print(data)