from typing import Dict
import json as _json
import datetime as _dt
# Se voce caiu de paraquedas nesse arquivo, PARABENS, isso eh uma ponte ao JSON


def get_all_events() -> Dict:
    with open("events.json") as events_file:
        data = _json.load(events_file)

    return data


def get_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "Esse mes nao existe doido"


def get_events_of_day(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "Se ta maluco?"


def get_today():
    today = _dt.date.today()
    # O %B vem de datetime, significa Mes
    month = today.strftime("%B").lower()
    return get_events_of_day(month, today.day)
