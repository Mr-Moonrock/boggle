from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"

game = Boggle()

@app.route('/', methods=['GET', 'POST'])
def home_page():
    """ Show Board"""

    board = game.make_board()
    session['board'] = board
    high_score = session.get('high_score', 0)
    num_plays= session.get('num_plays', 0)

    return render_template('home.html', board=board, num_plays=num_plays, high_score=high_score)

@app.route('/check-word', methods=['GET', 'POST'])
def check_guess_on_board():
    """ Check if user_guess is in dictionary """

    word = request.args['word']
    board = session['board']
    response = game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route('/post-score', methods=['GET', 'POST'])
def calculate_high_score(found_words):

    """ Calculate the high score based on found words"""

    score = request.json['score']
    high_score = session.get('high_score', 0)
    num_plays = session.get('num_plays', 0)

    session['num_plays'] = num_plays + 1
    session['high_score'] = max(score, high_score)

    return jsonify(brokeRecore= score > high_score)
   



