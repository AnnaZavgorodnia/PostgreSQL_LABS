import sys
import json

NEW_WORDS = {}


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
    words = tweet['text'].split(' ')
    for word in words:
        score += word_sentiment_score(word, sentiment_scores)

    for word in filter(lambda w: w not in sentiment_scores, words):
        if word not in NEW_WORDS:
            NEW_WORDS[word] = []
        NEW_WORDS[word].append(score)


def main():
    sentiment_scores = load_sentiment_scores(sys.argv[1])
    tweets = load_tweets(sys.argv[2])
    for tweet in tweets:
        calc_tweet_sentiment(tweet, sentiment_scores)
    for new_word in NEW_WORDS:
        if new_word:
            scores = NEW_WORDS[new_word]
            new_score = sum(scores) / len(scores)
            print new_word.encode('utf-8'), new_score


if __name__ == '__main__':
    main()
