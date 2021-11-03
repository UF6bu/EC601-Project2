# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager

n = 100

def search_tweets(consumer_key, consumer_secret, access_token_key, access_token_secret):
#   get parameters
    api = TwitterAPI(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
#   number of tweets and list of keywords
    r = TwitterPager(api, 'search/tweets', {'q': 'Boston', 'count': 100})

    for item in r.get_iterator():
        if 'text' in item:
            print(item['text'])
        elif 'message' in item and item['code'] == 88:
            print('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    consumer_key = ''
    consumer_secret = ''
    access_token_key = ''
    access_token_secret = ''

    search_tweets(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This code is not finished, for I can't test it because my development account application was reviewed