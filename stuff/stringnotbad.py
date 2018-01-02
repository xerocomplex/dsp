def not_bad(s):
    if 'not' in s[:s.find('bad')+3]:
        sub = s[s.find('not'):s.find('bad')+3]
        if sub in s:
            return s.replace(sub, 'good')
    else:
        return s
