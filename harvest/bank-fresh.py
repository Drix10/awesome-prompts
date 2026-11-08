"""Bank fresh sweep results into harvest/<bank>.json, skipping seen + already-promo'd.
Usage: python3 harvest/bank-fresh.py <fresh.json> <bank.json> [skip:<id-prefix-note>]
Marks entries whose IDs appear in r*.json / round4-promo.json / hit-by-others.json as SKIP.
"""
import json, glob, sys

fresh_path, bank_path = sys.argv[1], sys.argv[2]
fresh = json.load(open(fresh_path, encoding='utf-8'))
try:
    old = json.load(open(bank_path, encoding='utf-8'))
except FileNotFoundError:
    old = []

hit, parked, oldu = set(), set(), set()
for f in glob.glob('harvest/r*.json') + ['harvest/round4-promo.json']:
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        for i in x.get('u', []) or []:
            if len(i) > 10:
                hit.add(i)
try:
    for x in json.load(open('harvest/hit-by-others.json', encoding='utf-8')):
        for i in x.get('u', []) or []:
            if len(i) > 10:
                parked.add(i)
except FileNotFoundError:
    pass
for x in old:
    for i in x.get('u', []) or []:
        oldu.add(i)

added = 0
for x in fresh:
    ids = [i for i in x.get('u', []) or [] if len(i) > 10]
    if any(i in oldu for i in ids):
        continue
    oldu.update(ids)
    tag = None
    if ids and ids[0] in hit:
        tag = 'SKIP already-promod: '
    elif ids and ids[0] in parked:
        tag = 'SKIP hit-by-other-acc: '
    if tag:
        x['t'] = tag + x.get('t', '')[:130]
    old.append(x)
    added += 1
json.dump(old, open(bank_path, 'w', encoding='utf-8', errors='replace'), ensure_ascii=False, indent=1)
print(f'{bank_path} total: {len(old)} added: {added}')
