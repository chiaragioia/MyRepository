from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'myfirstproject'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
  input_checker = models.CharField(
    choices=[
            ["0", 'Male'],
            ["1", 'Female'],
            ["2", 'Non Binary'],
            ["3", 'Prefer not to answer']
            ],
    widget=widgets.RadioSelectHorizontal,
    label="Your gender is:")


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input_checker']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
