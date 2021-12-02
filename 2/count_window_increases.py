#!/usr/bin/env python3

increases = 0
window = []
with open('input', 'r') as f:
    for line in f.readlines():
        line = int(line.strip())
        window.append(line)
        if len(window) == 4:
            current = sum(window)
            if sum(window[:-1]) < sum(window[1:]): increases += 1
            window.pop(0)

print(increases)
