import hangman_helper


def update_word_pattern(word, pattern, letter):
    """Function that gets a word, pattern and letter.
    checks if letter exists in word, if so, updates
    the pattern to reveal the location of the letter
    in the pattern."""
    pattern_list = list(pattern)
    for i in range(len(word)):
        if word[i] == letter:
            pattern_list[i] = word[i]
    return str("".join(pattern_list))


def initialize_start(word):
    """Function that gets a word and sets pattern and
    wrong guesses list."""
    pattern = len(word) * "_"
    return pattern, []


def isvalid_letter(letter):
    """Function that gets a letter, checks if lower
    case and english alphabet."""
    if len(letter) > 1 or letter.isalpha() is False or\
            letter.islower() is False:
        return False
    return True


def score_letter(score, word, guess):
    """Function that gets score, word and a guess of a
    letter by the player, calculates new score and returns it"""
    n = word.count(guess)
    score += (n * (n + 1)) // 2
    return score


def score_word(score, pattern):
    """Function that gets score, word and a guess of a word by the player,
    calculates new score and returns it"""
    n = pattern.count("_")
    score += (n * (n + 1)) // 2
    return score


def guessed_before(letter, wrong_guesses, pattern):
    """Function that checks if user guessed the letter before"""
    if letter in pattern or letter in wrong_guesses:
        return True
    return False


def has_won(score):
    """Function that checks if user won or lost the game"""
    return score != 0


def case_letter(guess, wrong_guesses, pattern, word, score):
    """Function that updates wrong guesses list, pattern and score
    if user entered a letter"""
    if not isvalid_letter(guess):  # Checks if guess is valid
        message = "Your guess is invalid."
        return message, pattern, score

    if guessed_before(guess, wrong_guesses, pattern):
        message = "You guessed that letter before."
        return message, pattern, score

    score -= 1
    if guess in word:  # Checks if guess is in word
        message = "Guess is correct!"
        pattern = update_word_pattern(word, pattern, guess)
        score = score_letter(score, word, guess)
        return message, pattern, score
    wrong_guesses.append(guess)
    message = "Guess is incorrect."
    return message, pattern, score


def case_word(guess, pattern, word, score):
    """Function that checks if the word the user entered is correct,
    and updates his score"""
    score -= 1
    message = "Guess is incorrect."
    if guess == word:
        score = score_word(score, pattern)
        pattern = word
    return pattern, score, message


def case_hint(words_list, wrong_guesses, pattern, score):
    """Function that gives back list of good words"""
    score -= 1
    good_list = filter_words_list(words_list, pattern, wrong_guesses)
    sub_good_list = []
    if len(good_list) > hangman_helper.HINT_LENGTH:
        for i in range(hangman_helper.HINT_LENGTH):
            sub_good_list.append(good_list[(len(good_list) * i) //
                                           hangman_helper.HINT_LENGTH])
        hangman_helper.show_suggestions(sub_good_list)
    else:
        hangman_helper.show_suggestions(good_list)
    return score


def run_single_game(words_list, score):
    """Function that runs a single game of Hangman"""
    word = hangman_helper.get_random_word(words_list)
    pattern, wrong_guesses = initialize_start(word)
    message = "Game initialized, Good luck!"

    while score > 0 and pattern != word:
        hangman_helper.display_state(pattern, wrong_guesses, score, message)
        type_of_guess, guess = hangman_helper.get_input()

        if type_of_guess == hangman_helper.LETTER:
            message, pattern, score = case_letter(guess, wrong_guesses,
                                                  pattern, word, score)

        elif type_of_guess == hangman_helper.WORD:
            pattern, score, message = case_word(guess, pattern, word, score)

        elif type_of_guess == hangman_helper.HINT:
            score = case_hint(words_list, wrong_guesses, pattern, score)

    if has_won(score) is True:
        message = "You won the game!"
    else:
        message = f"You lost the game, the right word was: {word}"

    hangman_helper.display_state(pattern, wrong_guesses, score, message)
    return score


def filter_words_list(words_list, pattern, wrong_guesses):
    """Function that gets a words list, pattern and wrong guesses,
    clears returns a list with words that may fit the pattern"""
    good_list = []
    for word in words_list:
        if len(word) == len(pattern):
            is_to_add = True
            for i in range(len(word)):
                if (pattern[i] != "_" and word[i] != pattern[i]) or\
                        word[i] in wrong_guesses:
                    is_to_add = False
                    break
                if pattern[i] == "_" and word[i] != pattern[i]:
                    if pattern.count(word[i]) != word.count(pattern[i]):
                        is_to_add = False
                        break

            if is_to_add:
                good_list.append(word)
    return good_list


def main():
    """Main function - runs the first game and after that asks
    the user if he wants to continue playing"""
    words_list = hangman_helper.load_words()
    want_to_play = True
    while want_to_play:
        score = run_single_game(words_list, hangman_helper.POINTS_INITIAL)
        times_played = 1
        while score > 0:
            added_message = f"You played {times_played} times," \
                            f" your score is {score}"
            if hangman_helper.play_again(f"Do you want to play again?"
                                         f" {added_message}"):
                times_played += 1
                score = run_single_game(words_list, score)
            else:
                return

        added_message = f"You played {times_played} times," \
                        f" your score is {score}"
        if not hangman_helper.play_again(f"Do you want to"
                                         f" play again? {added_message}"):
            want_to_play = False


if __name__ == "__main__":
    main()