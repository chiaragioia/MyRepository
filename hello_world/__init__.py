from otree.api import *


doc = """
Your app description
"""
#comment what the app does

class C(BaseConstants):
    NAME_IN_URL = 'hello_world'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="Your name:")
    age = models.IntegerField(label="Your age:")
    


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
#sequence of pages you see
