import sys
import json
import re

OCCURENCES = {}


def load_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def process_tweet(tweet):
    if 'text' not in tweet:
        return

    terms = filter(lambda x: x, tweet['text'].split(' '))
    for term in terms:
        term = term.replace('\n', '')
        OCCURENCES[term] = OCCURENCES.get(term, 0) + 1


def process_occurences():
    total_terms_count = 0
    for term in OCCURENCES:
        total_terms_count += OCCURENCES[term]
    for term in OCCURENCES:
        OCCURENCES[term] = OCCURENCES[term] / float(total_terms_count)
        print term.encode('utf-8'), OCCURENCES[term]


def main():
    tweets = load_tweets(sys.argv[1])
    for tweet in tweets:
        process_tweet(tweet)
    process_occurences()


if __name__ == '__main__':
    main()
