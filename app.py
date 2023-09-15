from boggle import Boggle
from flask import Flask, render_template, request, session
from flask_session import Session
# redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
game = Boggle()
# debug = DebugToolbarExtension(app)

def get_current_board():

    """ Get the current game board from the session or generate new one"""

    board = session.get('board')
    if board is None:
        board = game.make_board()
        session['board'] = board
    return board

def add_word_to_session(word):

    """ Add a found word to the session's list of found words"""

    found_words = session.get('found_words', [])
    found_words.append(word)
    session['found_words'] = found_words

# def check_guess_on_board(user_guess, board, seen):

#     """ Check if user_guess is on the board """
#     board = get_current_board()
#     seen = {(0,0)}
#     is_valid_word = game.find_from(board, user_guess,1, seen)
#     print('check_guess_on_board - is_valid_word:', is_valid_word)
#     return is_valid_word

def calculate_high_score(found_words):

    """ Calculate the high score based on found words"""

    word_scores = [len(word) for word in found_words]
    return sum(word_scores)


@app.route('/', methods=['POST', 'GET'])
def home_page():
    """Display the board/ homepage"""

    if request.method == 'POST':
        user_guess = request.form.get('guess')
        print('Recieved user_guess:', user_guess)
        # Checking dictionary for valid word """
        if user_guess:
            user_guess = user_guess.strip().upper()
            print('Formatted user_guess:', user_guess)

            board = get_current_board()
            # is_valid_word = check_guess_on_board(user_guess, board, set())
            print('is_valid_word:', is_valid_word)

        #     if is_valid_word:
        #         add_word_to_session(user_guess)

        #         #Calculate high score
        #         found_words = session.get('found_words', [])
        #         high_score = calculate_high_score(found_words)
        #         session['high_score'] = high_score
        #         print('High score:', high_score)

        #         return jsonify({'message': 'Valid word', 'high_score': high_score, 
        # 'found_words': found_words})
        #     else:
        #         return jsonify({'message': 'Word is not valid on board'})

    board = get_current_board()
    return render_template('home.html', board=board)


if __name__ == '__main__':
    app.run()