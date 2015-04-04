import re
l="/search?q=jaguar&num=41&lr=&hl=en&ie=UTF-8&prmd=ivns&source=univ&tbm=nws&tbo=u&sa=X&ei=qx8gVZjVNMHiuQTx1YC4AQ&ved=0CLQBEKgC"
p = re.compile(ur'^[s|i]')
print re.search(p, l).group()
