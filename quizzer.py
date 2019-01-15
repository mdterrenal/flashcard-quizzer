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


parse_text()
