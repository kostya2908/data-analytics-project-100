import requests
import pandas as pd


#r_v = requests.get('https://data-charts-api.hexlet.app/visits?begin=2023-03-01&end=2023-09-01')
#visits = pd.DataFrame(r_v.json())
#visits.user_agent.to_csv('/home/kostya/csvs/step_3_user_agents.csv')

visits = pd.read_csv('/home/kostya/csvs/step_3_user_agents.csv')

def get_bots(x):
    if 'bot' in x.lower():
        return 'bot'
    else:
        return 'human'

visits['bot_or_human'] = visits['user_agent'].apply(lambda x: get_bots(x))
#print(visits[visits['bot_or_human'] == 'bot'])
print(visits.columns.to_list())



