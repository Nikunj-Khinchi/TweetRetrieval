import os.path
from os import path
from prettytable import PrettyTable


def resultFileCreation(Rankings):
    if (path.exists("./dist/Results.txt") == False):
        rTable = PrettyTable(['docno', 'rank', 'score'])
        rTable.align = 'l'
        rTable.border = False

        for query_num, value in Rankings.items():
            list = []
            ranking = 1
            for doc_num, cosSim in value.items():
                list = [doc_num, ranking, cosSim]
                ranking += 1
                rTable.add_row(list)

        table_text = rTable.get_string()

        f = open("./dist/Results.txt", "w+")
        f.write(table_text)

        f.close()
        return
    else:
        os.remove("./dist/Results.txt")
        resultFileCreation(Rankings)
