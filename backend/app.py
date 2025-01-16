from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Sample GRE vocabularies
vocab_list = [
    {"word": "Aberration", "definition": "A deviation from what is normal or expected."},
    {"word": "Equivocal", "definition": "Open to more than one interpretation; ambiguous."},
    {"word": "Prosaic", "definition": "Dull and lacking imagination."},
    {"word": "Alacrity", "definition": "An eager willingness to do something."},
    {"word": "Magnanimous", "definition": "Generous or forgiving, especially towards a rival."}
]

@app.route("/", methods=["GET", "POST"])
def flashcards():
    shuffled = False
    if request.method == "POST":
        if "shuffle" in request.form:
            random.shuffle(vocab_list)
            shuffled = True
    return render_template("flashcards.html", vocab_list=vocab_list, shuffled=shuffled)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)