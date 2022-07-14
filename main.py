print("Tossing a coin...")
h_cnt = 0
t_cnt = 0
import random
for i in range(1,4):
    t = random.randint(1,2)
    if t == 1:
        print("Round {}: Heads".format(i))
        h_cnt += 1
    else:
        print("Round {}: Tails".format(i))
        t_cnt += 1
print("Heads: {}, Tails: {}".format(h_cnt,t_cnt))