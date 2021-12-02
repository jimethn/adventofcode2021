#!/usr/bin/env python3

increases = 0
previous = 0
window = []
with open('input', 'r') as f:
    for line in f.readlines():
        line = int(line.strip())
        if len(window) == 3:
            current = sum(window)
            if previous:
                if previous < current: increases += 1
            previous = current
        window.append(line)
        if len(window) > 3:
            window.pop(0)

print(increases)
