import pandas as pd

r1 = pd.read_csv('/media/opus-bot-team/Ubuntu Works/OpusTech_Ubuntu/action_sync/all_csv/all_frames.txt')
r2 = pd.read_csv('/media/opus-bot-team/Ubuntu Works/OpusTech_Ubuntu/action_sync/all_csv/all_actions.txt')

xx = pd.concat([r1, r2], axis=1)
xx.to_csv ('/media/opus-bot-team/Ubuntu Works/OpusTech_Ubuntu/action_sync/all_csv/all_50_csv.csv', index=None)

