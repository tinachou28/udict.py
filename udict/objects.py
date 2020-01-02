from bs4 import BeautifulSoup

class Definition:
    r"""Represents a single definition entry on Urban Dictionary.

    Attributes
    -----------
    ribbon: :class:`str`
        The position of the definition on the page ("Top Definition", "2", etc.)
    id: :class:`int`
        ID of the definition
    term: :class:`str`
        Term the definition is for
    meaning: :class:`str`
        The definition of the word.
    example: Optional[:class:`str`]
        The example provided by the author, could be None.
    contributor: :class:`str`
        Author of the definition
    """
    __slots__ = ('ribbon', 'url', 'id', 'term', 'meaning', 'example', 'contributor',)

    def __init__(self, soup):
        self.ribbon = soup.find('div', class_="ribbon").text
        self.id = soup.find('a', class_="word").get("name")
        self.term = soup.find('a', class_="word").text
        self.meaning = soup.find('div', class_="meaning").text
        self.example = soup.find('div', class_="example")
        self.contributor = soup.find('div', class_="contributor").find('a').text

   class Page:
    r"""Represents a page on Urban Dictionary.

    Attributes
    -----------
    definitions: List[:class:`Definition`]
        A list of definition objects the page contains, in the order they are displayed on the actual webpage.
    url: :class:`str`
        The URL of the Urban Dictionary page
    term: :class:`str`
        The term the definitions are provided for
    """

    __slots__ = ('definitions', 'url', 'term', 'id')

    def __init__(self, soup):
        self.definitions = [Definition(item) for item in soup.findAll('div', class_="def-panel")]
        self.url = "https://www.urbandictionary.com/"+soup.find('a', class_="word").get("href")
        self.term = soup.find('a', class_="word").text
        
