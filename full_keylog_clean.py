import sys
output=""
with open(r"D:\OpusTech_Ubuntu\action_sync\all_csv\all_actions.txt") as f:
    for line in f:
        if not line.isspace():
            output+=line

f = open(r"D:\OpusTech_Ubuntu\action_sync\all_csv\all_actions_final.txt","w")
f.write(output)
