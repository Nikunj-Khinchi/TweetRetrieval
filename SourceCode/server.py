from flask import Flask
from flask import render_template
from flask import request
import main
from preprocess import returnDocs, tweetdict
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/display-results", methods=["GET"])
def hello_world():
    query = request.args.get('query', '')
    print(request)
    main.evaluate(query)
    tweetsMap = tweetdict()
    scoreMap = returnDocs()
    KrelevantDocs = dict(list(scoreMap.items())[1:11])
    # print(KrelevantDocs)
    finList = []
    k = 0
    for key, val in KrelevantDocs.items():
        mylist = []
        k += 1
        mylist.append(k)
        mylist.append(tweetsMap[key])
        mylist.append(val)
        mylist.append(key)
        finList.append(mylist)
    print(finList)

    return render_template("displayTable.html", tweet_list=finList)


app.run()
