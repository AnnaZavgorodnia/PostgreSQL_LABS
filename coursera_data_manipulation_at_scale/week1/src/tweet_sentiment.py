import sys
import json


def load_sentiment_scores(filename):
    scores = {}
    with open(filename, 'r') as f:
        for line in f:
            term, score = line.split("\t")
            scores[term] = int(score)
    return scores


def word_sentiment_score(word, sentiment_scores):
    return sentiment_scores.get(word, 0)


def load_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def calc_tweet_sentiment(tweet, sentiment_scores):
    if 'text' not in tweet:
        return

    score = 0
    for word in tweet['text'].split(' '):
        score += word_sentiment_score(word, sentiment_scores)
    print score


def main():
    sentiment_scores = load_sentiment_scores(sys.argv[1])
    tweets = load_tweets(sys.argv[2])
    for tweet in tweets:
        calc_tweet_sentiment(tweet, sentiment_scores)


if __name__ == '__main__':
    main()
