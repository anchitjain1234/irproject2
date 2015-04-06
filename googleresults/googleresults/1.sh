rm gtest.json
rm ytest.json
scrapy crawl google -o gtest.json -a query="jaguar"
scrapy crawl yahoo -o ytest.json -a query="jaguar"

