import re


def main(s):
    p = re.findall(r"\.do\s*(.*)\.end", s, re.DOTALL)[0]
    matches = re.findall(r"<%\s*loc\s*#(-?\d*)\s*==>\s*(\w+)\s*%>;", p)
    d = {}
    for match in matches:
        d[match[1]] = int(match[0])
    return d


s = '''.do <% loc #-384 ==> arus_949 %>; <% loc #2062==> risobe_877 %>; <%\n
loc#-5690 ==>rimale_334 %>; .end'''
print(main(s))
