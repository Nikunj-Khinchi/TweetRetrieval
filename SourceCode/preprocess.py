import os
import string
import json
import nltk
import math
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

ps = PorterStemmer()


def isNumeric(subj):
    try:
        return float(subj)
    except Exception:
        return False


def tweetdict():
    listTweets = dict()
    tweets = (line.strip('\n') for line in open(
        "./assets/tweet_list.txt", 'r', encoding='utf-8-sig'))
    print(tweets)
    for tweet in tweets:
        key, value = tweet.split('\t')
        # print(key,value)
        listTweets[key] = value
    # print(listTweets)
    return listTweets


def importTweets(verbose=False):
    tweet_list = dict()
    # tweets = (line.strip('\n') for line in open('./assets/tweet_list.txt', 'r', encoding='utf-8-sig'))
    tweets = (line.strip('\n') for line in open(
        "./assets/tweet_list.txt", 'r', encoding='utf-8-sig'))

    for tweet in tweets:
        key, value = tweet.split('\t')

        # print(key,value)
        tweet_list[key] = filterSentence(value, verbose)

    return tweet_list


def importQuery(query, verbose=False):

    query_list = dict()

    # with open('./assets/test_queries.txt', 'r') as file:
    #     fileContents = file.read()

    # queryCheck = fileContents.strip('\n').split("\n")
    qlist = query.split(" ")

    # print(qlist)

    # print(queryCheck, "fggd")
    current_tweet = 1
    # for x in queryCheck:
    #     print(x)
    query_list[current_tweet] = filterSentence(query, verbose)
    #     # query_list[current_tweet] = x
    #     current_tweet += 1

    print(query_list, "dictionary list")

    return query_list


def filterSentence(sentence, verbose=False):
    edge_stopwords = ['n\'t', '\'d', 'http', 'https', '//', '...']

    custom_stopwords = set(stopwords.words('english')).union((line.strip(
        '\r\n') for line in open('./assets/stop_words.txt', 'r'))).union(edge_stopwords)

    tokens = [ps.stem(word.lower()) for word in word_tokenize(sentence)
              if word.lower() not in custom_stopwords and
              word not in string.punctuation and
              not isNumeric(word)]

    if verbose:
        print('\n Testing string: \n\n\t ' + sentence + '\n')
        print(' Tokenized:\n')
        print('\t' + '[%s]' % ', '.join(map(str, tokens)) + '\n')

    return tokens


def buildIndex(documents, verbose=False):

    inverted_index = dict()

    word_idf = dict()

    for index, document in documents.items():
        for token in document:
            if token not in inverted_index:
                inverted_index[token] = {}
            if token in inverted_index and index not in inverted_index[token]:
                inverted_index[token][index] = 1
            elif index in inverted_index[token]:
                inverted_index[token][index] += 1

    for token, current_document in inverted_index.items():
        total_occurence = 0
        for document, occurence in current_document.items():
            total_occurence += occurence

        word_idf[token] = round(
            math.log((len(documents) / total_occurence), 2), 3)

    for token, document_info in inverted_index.items():
        for document, occurence in document_info.items():
            document_info[document] = occurence * word_idf[token]

    if verbose:
        print("\r Inverted Index")
        with open("invertedIndex.json", "w") as outfile:
            json.dump(inverted_index, outfile)
        print(json.dumps(inverted_index, indent=2))
        print("-" * 40)

    return inverted_index


def lengthOfDocument(inverted_index, tweets, verbose=False):
    document_lengths = dict()

    for tweet_id, tweet in tweets.items():
        document_length = 0
        for token in tweet:
            document_length += pow(inverted_index[token][tweet_id], 2)

        document_lengths[tweet_id] = round(math.sqrt(document_length), 3)

    if verbose:
        print('Length of documents', document_lengths)

    return document_lengths


def returnDocs():
    listDocs = dict()
    DocList = []
    scoreList = []
    scoreedDocs = (line.strip('\n') for line in open(
        "./dist/Results.txt", 'r', encoding='utf-8-sig'))

    for docs in scoreedDocs:
        docno = docs[1:19].strip()
        score = docs[24:40].strip()
        DocList.append(docno)
        listDocs[docno] = score
        scoreList.append(score)

    return listDocs
