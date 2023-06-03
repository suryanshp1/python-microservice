import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    return wikipedia.summary(name, length)


def search_wiki(name):
    """Search wikipedia for names"""

    return wikipedia.search(name)


def phrases(name):
    """Return phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
