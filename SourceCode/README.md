### Searching Relevant Tweets 
## Team Details:

# Nikunj Khinchi S20210010159
# Manthan Shinde S20210010135

## Project Overview

*An IR system to retrieve the tweets using a query entered and ranking them according to their score.*

## The following have been implemented :
*Stemming, Stopwords removal, Tokenisation.*
*Building the inverted index, and tfidf weighting.*
*Calculating the cosine similarity and ranking the documents.*
*Writing the result into "/dist/Results.txt"*
*Capturing user feedback*
*Integrating the IR system in flask.*

## Setting Up and Running the Code:

- Virtual Environment:
Create and activate a virtual environment named `myenv`:

`python -m venv myenv`   # Create virtual environment
- Activate the virtual environment
- For Windows:
`myenv\Scripts\activate`
-  For macOS / Linux:
`source myenv/bin/activate`


1. - *python installed and executable.*

2. - *nltk libaries installed all of these can be downloaded using python -> import nltk -> nltk.download('corpus | tokenize | stem.porter'):*

3. - *Install Dependencies:* Ensure you have the necessary dependencies installed. You can use the provided `requirements.txt` file. `pip install -r requirements.txt`

4. - *Navigate* to the project directory `cd code`

5. - Run the `python server.py` file and enter the query and press search.
6. - We get the result with the rank,docno, tweet, and score.
7. - The user can then choose if the tweet is relevant or not.
8. - for IR evaluation `python Evaluation.py`
