import re
p = re.compile(ur'(.*)index.html')
test_str = u"http://www.jaguarusa.com/"

gp=re.search(p, test_str)
print gp