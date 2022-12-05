from selenium import webdriver
driver = webdriver.Firefox()

###search page
url = "https://quizlet.com/search?query=cell-bio&type=all"

driver.get(url)

cardset = driver.find_element('xpath', '//a[@class="AssemblyLink AssemblyLink--medium AssemblyLink--title"]')
cardseturl = cardset.get_attribute('href')
driver.quit()


###card set page
driver = webdriver.Firefox()
driver.get(cardseturl)

driver.quit()

#can delete later
#attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', ids)
#print(attrs)
