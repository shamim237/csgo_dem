global g_sec
g_sec = 0
count = 0

with open("key_sec_action.txt", "r") as data:

    key_sec = data.readlines()
    key_sec = key_sec[:-1]

    for i in key_sec:
        n = len(i)
        j = i[2:n-1]
        i = i[:2]
        i = int(i)

        if g_sec == 0:
            print(f"{g_sec:02d}", j, file = open("add_seconds.txt", "a"))

        if i-g_sec>1:
            while i-g_sec!=1:
                g_sec += 1
                print(f"{g_sec:02d}", '50:0', file = open("add_seconds.txt", "a"))

        if i-g_sec<0:
            if g_sec!=59:
                while g_sec!=59:
                    g_sec += 1
                    print(f"{g_sec:02d}", '-50:0', file = open("add_seconds.txt", "a"))
            g_sec = 0

        if i-g_sec==1 or i-g_sec==0:
            g_sec = i
            print(f"{i:02d}", j, file = open("add_seconds.txt", "a"))

