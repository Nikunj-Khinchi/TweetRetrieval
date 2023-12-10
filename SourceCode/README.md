# Searching Relevant Tweets 
## Team Details:

- Nikunj Khinchi S20210010159
- Manthan Shinde S20210010135

## Project Overview

*An IR system to retrieve the tweets using a query entered and ranking them according to their score.*

## The following have been implemented :
- *Stemming, Stopwords removal, Tokenisation.*
- *Building the inverted index, and tfidf weighting.*
- *Calculating the cosine similarity and ranking the documents.*
- *IR evaluation calculate the recall and precision graph and 11 point Interpolation*
- *Writing the result into "/dist/Results.txt"*
- *Capturing user feedback*
- *Integrating the IR system in flask.*

## Setting Up and Running the Code:

- Virtual Environment:
Create and activate a virtual environment named `myenv`:

`python -m venv myenv`   # Create virtual environment
- Activate the virtual environment
- For Windows:
`myenv\Scripts\activate`
-  For macOS / Linux:
`source myenv/bin/activate`


 - *python installed and executable.*

 - *nltk libaries installed all of these can be downloaded using python -> import nltk -> nltk.download('corpus | tokenize | stem.porter'):*

 - *Install Dependencies:* Ensure you have the necessary dependencies installed. You can use the provided `requirements.txt` file. `pip install -r requirements.txt`

 - *Navigate* to the project directory `cd SourceCode`

 - Run the `python server.py` file and enter the query and press search.
 - We get the result with the rank,docno, tweet, and score.
 - Demo input  `assests/test_queries.txt`
 - After clicking the submit button, put the code simultaneously while keeping the webpage functional and display the operational data in the terminal for observation.
 - The user can then choose if the tweet is relevant or not.
 - for IR evaluation `python Evaluation.py`
