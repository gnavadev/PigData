from typing import List
import requests as _requests
import bs4 as _bs4

# Comecam com _ as funcoes que nao devem ser importadas


def _generate_url(month: str, day: int) -> str:
    """Funcao que gera uma url de acordo com os dados passados para os parametros, retorna um dado tipo str"""
    url = f'https://www.onthisday.com/day/{month}/{day}'
    return url


def _get_page(url: str) -> _bs4.BeautifulSoup:
    """ Funcao que serializa a url """
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def events_of_the_day(month: str, day: int) -> List[str]:
    """ Retorna os eventos de um determinado dia """

    url = _generate_url(month, day)
    page = _get_page(url)

    # raw_events armazena todos os objetos da pagina com a classe event, foi utilizado
    # class_ porque class eh uma palavra reservada do python
    raw_events = page.find_all(class_="event")
    # pega os eventos de raw_events
    events = [event.text for event in raw_events]
    # print(events)
    return events


events_of_the_day("february", 24)
