import math
import json


def retrieve(query_list, inverted_index, document_length, verbose=False):

    query_tfidf = dict()
    ranking = dict()

    for query_num, query in query_list.items():
        query_index = dict()
        retrieval = dict()
        query_length = dict()

        for token in query:
            if token not in query_index:
                query_index[token] = 1
            else:
                query_index[token] += 1

        for token, occurences in query_index.items():
            try:
                for document_id, tfidf in inverted_index[token].items():
                    retrieval[token] = 1 + round(math.log(occurences, 2), 3)
                    break
            except KeyError:
                retrieval[token] = 0.0

            query_tfidf[query_num] = retrieval

        for query_num, tokens in query_tfidf.items():
            query_len = 0.0
            for token, tfidf in tokens.items():
                query_len += pow(tfidf, 2)

            query_length[query_num] = round(math.sqrt(query_len), 3)

    for query_no, query_token_info in query_tfidf.items():
        doc_cossim = dict()
        for document_id, document_len in document_length.items():
            dotproduct = 0.0
            for token, tfidf in query_token_info.items():
                try:
                    document_dp = inverted_index[token][document_id]
                except KeyError:
                    continue

                dotproduct += document_dp * tfidf

            if (dotproduct == 0.0):
                continue
            try:
                doc_cossim[document_id] = dotproduct / \
                    (document_len * query_length[query_no])
            except ZeroDivisionError:
                continue

        ranking[query_no] = {k: v for k, v in sorted(
            doc_cossim.items(), key=lambda doc_cossim: doc_cossim[1], reverse=True)}

    if (verbose):
        print('Query Ranking')
        print(json.dumps(ranking, indent=2))
        print("-" * 40)

    return ranking
