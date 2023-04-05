
import flask
from flask import render_template, request
import sys
sys.path.append('../backend')
from api import *


app = flask.Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Home page, contains a search bar and a link to the advanced search page.
@app.route('/')
def simpleHome():
    return render_template('home.html', port=port)

# Leads to the about page, 
# which contains information about the dataset, the project and us.
@app.route('/about',)
def simpleAbout():
    return render_template('about.html', port=port)

# Leads to the "Advanced Search" page, 
# which offers more search options than on the Homepage.
@app.route('/advancedSearch')
def simpleAdvSearch():
    return render_template('advSearch.html', port=port, error="")

# Leads to the source page, 
# which contains information about the source of the dataset.
@app.route('/source')
def simpleSource():
    return render_template('source.html', port=port)

# Extracts the search parameters from the form on the advanced search page. 
# Also calls API, and returns the results of the query.
@app.route('/results', methods=['GET', 'POST'])
def simpleResults():
    if request.method == 'POST':
        result = request.form

        title = result.get("title")
        author = result.get("author")
        publisher = result.get("publisher")
        topic = result.get("topic")
        nation = result.get("country")
        language = result.get("language")
        startYear = result.get("startYear")
        endYear = result.get("endYear")

        api = earlyBooksAPI()
        if(not(title or author or publisher or topic or nation or language or startYear or endYear)):
            return render_template('advSearch.html', port=port, error="Please enter at least one search parameter.")
        
        listOfBooks = api.searchInDataBase(title, author, publisher, topic, nation, language, startYear, endYear)
        numerOfBooks = len(listOfBooks)
    return render_template('results.html', results = listOfBooks, numberOfBooks=numerOfBooks, port=port)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)