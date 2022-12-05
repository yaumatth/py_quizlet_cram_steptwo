from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#options
setNum = str(4)
url = "https://quizlet.com/search?query=cell-bio&type=sets&useOriginal="


###search page
driver = webdriver.Firefox()
driver.get(url)

cardset = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SearchResultsPage-result' and @data-page-depth='" + setNum + "']//*[@class='AssemblyLink AssemblyLink--medium AssemblyLink--title']")))
cardseturl = cardset[0].get_attribute('href')

driver.quit()


###card set page
driver = webdriver.Firefox()
driver.get(cardseturl)

time.sleep(2)
html = driver.find_element('tag name', 'html')
html.send_keys(Keys.PAGE_DOWN)


cardlist = WebDriverWait(driver, 45).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SetPageTerms-term' and @aria-label='Term']//*[@class='TermText notranslate lang-en']")))

alltext = []
for i in range(len(cardlist)): #replace 3 with len(cardlist)
    alltext.append(cardlist[i].text)

driver.quit()

if (len(alltext)%2 == 1):
    alltext = alltext[:-1]


#creating dataframe for export
questions = []
answers = []
for j in range(len(alltext)):
    if (j%2 == 0):
        questions.append(alltext[j])
    else:
        answers.append(alltext[j])

QAdataframe = pd.DataFrame({'questions': questions, 'answers': answers})

print(QAdataframe.tail(20))

#can delete later
#attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', cardset[0])
#print(attrs)
