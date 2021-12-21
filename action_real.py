with open("key_sec_action.txt", "r") as data:
    key_sec = data.readline()

    n = len(key_sec)
    j = key_sec[3:n-1]        # Actions
    i = key_sec[:2]           # Seconds
    i = int(i)

    print(i)


with open("action_extended.txt", "r") as data:
    key_sec = data.readlines()[i*16:(i*16)+5297]

    for xx in key_sec:
        n = len(xx)
        xx = xx[:n-1]
        print(xx, file = open("action_real.txt", "a"))
