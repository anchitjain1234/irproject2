import re
l="<span class=\" fz-15px fw-m fc-12th wr-bw\">www.<b><b>jaguar</b></b>.com/index.html</span>"
p = re.compile(ur'<[^>]*>')
t=re.sub(p,"", l)
t= "http://"+t
p = re.compile(ur'(.*)index.html')
gp=re.search(p, t)
if gp:
    t = gp.group(1)
print t