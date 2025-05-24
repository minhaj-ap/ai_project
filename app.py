from flask import Flask, request, jsonify
from generateTags import generateTags

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/rate")
# TODO:Find ratings from a given review paragraph
def findRating():
    return "Find rating from a given paragraph"


@app.route("/tags", methods=["POST"])
# TODO:genrate tags for reviews
def returnTags():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "No JSON body found"}), 400
        paragraph = data.get("paragraph")
        if not paragraph:
            return jsonify({"error": "No paragraph argument found"}), 400
        result = jsonify({"tags": generateTags(paragraph)})
        return result
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to generate tags"}), 500


@app.route("/summary")
# TODO:summarize paragraphs
def summarizeParagrpah():
    return "Summarize a long paragraph into a small one"


@app.route("/restart")
def restart():
    return "Restarting server"  # this endpoint is to prevent server from cold start


if __name__ == "__main__":
    app.run(debug=True)
