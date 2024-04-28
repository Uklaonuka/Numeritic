import os
from collections import defaultdict

a = int(input())
spisok = []
i = 0
while i < a:
    spisok.append(input())
    i += 1


def tree():
    return defaultdict(tree)

def add(t, path):
    for node in path:
        t = t[node]

def dicts(t):
    return {k: dicts(t[k]) for k in t}

def print_tree(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + key)
        if isinstance(value, dict):
            print_tree(value, indent+1)



t = tree()
for c in spisok:
    add(t, c.split('/'))

d = dicts(t)
print_tree(d)