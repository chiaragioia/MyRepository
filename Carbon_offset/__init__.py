from otree.api import *
from otree.api import models, widgets

doc = """
WELCOME!
We ask you to spend 5 minutes to fulfill a short survey providing sincere
answers to the questions provided. 

You will gain ()

Thank you for your participation! 
"""

class C(BaseConstants):
    NAME_IN_URL = 'mysecondproject'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    name_in_url = "slider"
    players_per_group = None
    num_rounds = 1

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
  slider_2 = models.FloatField()
  slider_1 = models.FloatField()
  
  input_text_1 = models.IntegerField()
  input_checker_g = models.CharField(
    choices=[
            ["1", 'Female'],
            ["2", 'Male'],
            ["3", 'Other']
            ],
    widget=widgets.RadioSelectHorizontal,
    )
  
  input_dropdown_d= models.CharField(
    choices=['Middle school','Highschool','Bachelor Degree','Master Degree','PhD'])
  
  input_dropdown_h= models.CharField(
    choices=['Agriculture','Anthropology','Archaeology','Architecture and design','Art','Biology','Chemistry','Computer science','Economics','Education','Engineering and technology','Geography','History','Journalism,media studies and communication','Law','Linguistics and languages','Mathematics','Medicine','Philosophy','Physics','Political science','Psychology','Religion','Sociology', 'Statistics','Other'])

  
  treatment= models.CharField()
  input_checker = models.CharField(
    choices=[
            ["1", 'Climate change'],
            ["2", 'Poverty, hunger and lack of drinking water'],
            ["3", 'Spread of infectious diseases'],
            ["4", 'The economic situation'],
            ["5", 'Deterioration of nature'],
            ["6", 'Deteroration of democracy and rule of law'],
            ["7", 'The increasing global population']],
    widget=widgets.RadioSelect,
    )
    
  input_checker_2 = models.CharField(
    choices=[
            ["1", 'National governments'],
            ["2", 'Business and industry'],
            ["3", 'The European Union'],
            ["4", 'Regional and local authorities'],
            ["5", 'You personally'],
            ["6", 'Environmental groups']],
    widget=widgets.RadioSelect,
    )

  input_radio = models.CharField(
    choices=[
            ["1",'Yes'],
            ["2",'No'] , 
            ["3",'Do not know']],
    widget=widgets.RadioSelectHorizontal)
  
  input_checker_4 = models.CharField(
    choices=[
            ["1", 'You try to reduce your waste and you regularly separate it for recycling'],
            ["2", 'You try to cut down on your consumption of disposable items whenever possible (e.g. plastic bags from the supermarket) excessive packaging'],
            ["3", 'When buying a new household appliance e.g. washing machine, fridge or tv, lower energy consumption is an important factor in your choice'],
            ["4", 'You buy and eat more organic food'],
            ["5", 'You buy and eat less meat'],
            ["6", 'You regularly use environmentally-friendly alternatives to your private car such as walking, cycling, taking public transport or car-sharing'],
            ["7", 'You consider the carbon footprint of your transport when planning your holiday and other longer distance travel and sometimes adapt your plans accordingly'],
            ["8", 'None of them']],
    widget=widgets.RadioSelect,
    )
# devo capire come fare a far selezionare più di una scelta


  
  input_radio_5 = models.CharField(
    choices=[
       ["1",'Enough'], 
       ["2",'Not Enough'],
       ["3",'Too much'],
       ["4",'Do not know'],
       ],
    widget=widgets.RadioSelectHorizontal)

  input_radio_6 = models.CharField(
    choices=[
            ["1",'Totally agree'], 
            ["2",'Tend to agree'],
            ["3",'Tend to disagree'],
            ["4",'Totally disagree'],
            ["5",'Do not know']],
    widget=widgets.RadioSelectHorizontal)

  #input_radio_donation = models.CharField(
    #choices=['Yes', 'No'],
    #widget=widgets.RadioSelect)

  statement1 = models.IntegerField()
  statement2 = models.IntegerField()
  statement3 = models.IntegerField()
  statement4 = models.IntegerField()



def creating_session(subsession):
    for g in subsession.get_groups():
        for p in g.get_players():
            if p.id_in_group % 3 == 0:
                p.treatment="Baseline"
            if p.id_in_group % 3 == 1:
                p.treatment="Amazon"
            if p.id_in_group % 3 == 2:
                p.treatment="Ryanair"



# PAGES
class MyPage(Page):
    pass

class Ryanair(Page):
  @staticmethod
  def vars_for_template(player: Player):
    return dict(
    treatment = player.treatment)
  def is_displayed(player: Player):
    return player.treatment == "Ryanair"


class Survey(Page):
    form_model = 'player'
    form_fields = ['input_checker', 'input_checker_2','slider_2']

class Survey_2(Page):
    form_model = 'player'
    form_fields = ['input_radio','input_checker_4']

class Survey_3(Page):
    form_model = 'player'
    form_fields = ['statement1','statement2','statement3','statement4']


class Survey_4(Page):
    form_model = 'player'
    form_fields = ['input_radio_5','input_radio_6']

class Demograph(Page):
    form_model = 'player'
    form_fields = ['input_text_1','input_checker_g','input_dropdown_d','input_dropdown_h']

class Pro_environ_don(Page):
    form_model = 'player'
    form_fields = ['slider_1']

class Amazon(Page):
  @staticmethod
  def vars_for_template(player: Player):
    return dict(
    treatment = player.treatment)
  def is_displayed(player: Player):
    return player.treatment == "Amazon"
      

class ResultsWaitPage(WaitPage):
    pass 


page_sequence = [MyPage, Ryanair, Amazon, Survey, Survey_2, Survey_3, Survey_4, Demograph, Pro_environ_don]
