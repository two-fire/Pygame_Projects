words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

counter = {}
for word in words:
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

for word in counter:
    print("{}:{}".format(word, counter[word]))
from collections import Counter

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

cnt = Counter()
for word in words:
    cnt[word] += 1

print(cnt)
for w in cnt.keys():
    print("{}:{}".format(w, cnt[w]))
from collections import defaultdict

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

dd = defaultdict(lambda : 0)
for word in words:
    dd[word] += 1

print(dd)
for word in dd.keys():
    print("{}:{}".format(word, dd[word]))
