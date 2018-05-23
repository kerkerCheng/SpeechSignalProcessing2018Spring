import numpy as np
from collections import defaultdict

f = open('Big5-ZhuYin.map', 'r', encoding='cp950')
chs = []
phs = []
for line in f:
    seg = line.strip().split()
    phones = seg[1].split('/')
    for ph in phones:
        chs.append(seg[0])
        phs.append(ph)

f.close()

dic = defaultdict(list)
for i, ph in enumerate(phs):
    dic[ph[0]].append(chs[i])

f_out = open('ZhuYin-Big5.map', 'w', encoding='cp950')
sorted_key = ''.join(sorted(dic.keys()))

for key in sorted_key:
    f_out.write((key + "      "))
    f_out.write((" ".join(dic[key])))
    f_out.write('\n')
    for word in dic[key]:
        f_out.write(word + "      " + word)
        f_out.write('\n')
f_out.close()