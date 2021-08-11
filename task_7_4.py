from collections import defaultdict
import os
import django
folder = django.__path__[0]
result = defaultdict(int)
for root, dirs, files in os.walk(folder):
    for file in files:
        size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        result[size] += 1
for size, nums in result.items():
    print(f'{size}: {nums}')
