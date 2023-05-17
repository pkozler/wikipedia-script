import wikipedia


def download(article):
    try:
        page = wikipedia.page(article, auto_suggest=False)
        result = page.content.split('\n')[0]
    except wikipedia.exceptions.DisambiguationError as e:
        result = f"Bylo nalezeno více článků s názvem '{article}':\n" + "\n".join(f"\t{x}" for x in e.options)
    except wikipedia.exceptions.PageError:
        result = f"Článek s názvem '{article}' nebyl nalezen. "
        search = wikipedia.search(article)

        if len(search):
            result += ("Zadaný text se vyskytuje v článcích s tímto názvem:\n" + "\n".join(f"\t{x}" for x in search))
        else:
            result += "Zadaný text se nevyskytuje v žádném článku."

    return result


class Search:
    def __init__(self, lang='cs'):
        self.results = {}
        wikipedia.set_lang(lang)

    def query(self, name):
        article = name.strip().lower()

        if article == '':
            return ''

        if article not in self.results.keys():
            self.results[article] = download(article)

        return self.results[article]
