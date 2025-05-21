from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/rate")
# TODO:Find ratings from a given review paragraph
def findRating():
    return "Find rating from a given paragraph"


@app.route("/tags")
# TODO:genrate tags for reviews
def generateTag():
    return 'Generate suitable tags for a paragrpah (eg:"Angry","Happy","Sad")'


@app.route("/summary")
# TODO:summarize paragraphs
def summarizeParagrpah():
    return "Summarize a long paragraph into a small one"

@app.route("/restart")
def restart():
    return "Restarting server" #this endpoint is to prevent server from cold start
if __name__ == "__main__":
    app.run(debug=True)
