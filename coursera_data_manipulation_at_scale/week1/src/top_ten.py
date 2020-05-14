import sys
import json

HASTAGS = {}


def load_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def process_tweet(tweet):
    if 'text' not in tweet:
        return
    hashtags = [e['text'] for e in tweet['entities']['hashtags']]
    for hashtag in hashtags:
        HASTAGS[hashtag] = HASTAGS.get(hashtag, 0) + 1


def get_top_ten_hashtags():
    hashtags = [(k, v) for k, v in HASTAGS.items()]
    sorted_hashtags = sorted(hashtags, key=lambda x: x[1], reverse=True)
    return sorted_hashtags[:10]


def main():
    tweets = load_tweets(sys.argv[1])
    for tweet in tweets:
        process_tweet(tweet)
    for hashtag, frequency in get_top_ten_hashtags():
        print hashtag.encode('utf-8'), frequency


if __name__ == '__main__':
    main()
