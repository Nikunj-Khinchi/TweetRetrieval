from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument, tweetdict, returnDocs
from results import retrieve
from write import resultFileCreation


def evaluate(query=""):
    print(query)

    print("\n Stemming,tokenisation and removal of stop words \n")

    tweets = importTweets()

    query_file = importQuery(query)

    print("\n Preprocessing Done! \n")

    print("\n Building the inverted index \n")
    verbose = True

    index = buildIndex(tweets, verbose)

    print("\n  Done! \n")

    print("\n Retrieving and Ranking..\n")

    document_length = lengthOfDocument(index, tweets)

    ranking = retrieve(query_file, index, document_length)

    print("\n Retrieval and Ranking Done! \n")

    print("\n Writing Result File... \n")

    resultFileCreation(ranking)

    print("\n Result File Creation Done! \n")


if __name__ == "__main__":
    evaluate()
