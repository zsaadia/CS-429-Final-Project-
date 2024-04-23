import subprocess

# Define test cases
test_cases = [
    "scrapy crawl my_crawler -a seed_url='https://en.wikipedia.org/wiki/Information_retrieval' -a max_pages=100 -a max_depth=3",
    "scrapy crawl my_crawler -a seed_url='http://quotes.toscrape.com' -a max_pages=100 -a max_depth=40",
    "scrapy crawl my_crawler -a seed_url='https://moss.cs.iit.edu/' -a max_pages=60 -a max_depth=60"
]

# Execute each test case
for test_case in test_cases:
    subprocess.run(test_case, shell=True)
