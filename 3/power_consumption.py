#!/usr/bin/env python3

rate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open("input", "r") as f:
    for line in f:
        for i, char in enumerate(line):
            if char == '\n':
                pass
            elif int(char) == 0:
                rate[i] -= 1
            else:
                rate[i] += 1

gamma = "".join(["1" if x>0 else "0" for x in rate])
epsilon = "".join(["1" if x<0 else "0" for x in rate])

print(int(gamma, 2) * int(epsilon, 2))
