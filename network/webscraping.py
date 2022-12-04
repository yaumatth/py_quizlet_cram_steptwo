######look into using SELENIUM

import requests
from bs4 import BeautifulSoup
import re
import json

#url = 'https://quizlet.com/search?query=cell-bio&type=sets&useOriginal='
url = 'https://quizlet.com/748827014/bio-the-cell-flash-cards'


header = requests.utils.default_headers()['User-Agent']
headers = {'User-Agent': header}

r = requests.get(url, headers=headers)

soup = str(BeautifulSoup(r.text, 'html.parser'))

print(soup)

#quiz = re.findall('SetPreviewCard', soup)
#print(quiz)
