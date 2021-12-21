global count
count = 0
global g_sec
g_sec = 0

print('50:0', file = open("action_extended.txt", "a"))

with open("add_seconds.txt", "r") as data:

    key_sec = data.readlines()
    
    for i in key_sec:
        n = len(i)
        j = i[3:n-1]        # Actions
        i = i[:2]           # Seconds
        i = int(i)
        
        # Update global second if it not exists
        if i-g_sec!=1 and i-g_sec!=0:
            g_sec += 1
            # print(g_sec)

        # print(i, file = open("action_extended.txt", "a"))
        if g_sec == i:
            if count<15:
                print(j, file = open("action_extended.txt", "a"))
                count += 1
            else:
                pass
            # g_sec = i

        else:
            if count<16:
                if count % 2 == 0:
                    for x in range(15-count):
                        print('50:0', file = open("action_extended.txt", "a"))
                else:
                    for x in range(15-count):
                        print('-50:0', file = open("action_extended.txt", "a"))
                count = 0
            print(j, file = open("action_extended.txt", "a"))

            g_sec = i

