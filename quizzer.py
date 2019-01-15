"""Module that represents a flashcard quizzer."""

from urllib.request import urlopen
from urllib.error import HTTPError


def parse_text():
    """Parse data for flashcards and store each card in a list.

    Read data from a URL and process the data to store the
    cards in a list of lists.
    """

    flashcard_data_url = ('http://web.mit.edu/jesstess/'
                          'www/IntermediatePythonWorkshop/state_capitals.txt')
    try:
        with urlopen(flashcard_data_url) as flashcard_data:
            flashcards = flashcard_data.read()
        flashcards = flashcards.decode("utf-8")
    except HTTPError:
        print('The file provided is not available. Please try again.')
    flashcards = flashcards.strip().split('\n')
    flashcards = [card.split(',') for card in flashcards]
    return flashcards


def quiz_user(flashcards):
    """Continuously quiz the user by asking for the correct answer.

    Randomly choose a card from a list of flashcards and provide
    the question. Prompt for an answer and check if the user's answer
    is correct.
    """
    
    while True:
        chosen_card = random.choice(flashcards)



parse_text()
