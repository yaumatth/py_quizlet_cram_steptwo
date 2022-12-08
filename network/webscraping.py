def url_quizlet(topic):
	assert type(topic) == str, "Error: topic must be a string."
	topicF = topic.replace(" ", "-")
	url = "https://quizlet.com/search?query=" + topicF + "&type=sets&page=1&creator=teacher" #&useOriginal=
	return url


#def url_kahoot(topic):
	



def webscrape_quizlet(url, setNum=1):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import time
    import pandas as pd

    #options
    setNum = str(setNum)

    from py_quizlet_kahoot.network import translation
    translation.speed_warning()

    ###search page
    driver = webdriver.Firefox()
    driver.get(url)

    try:
        cardset = WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SearchResultsPage-result' and @data-page-depth='" + setNum + "']//*[@class='AssemblyLink AssemblyLink--medium AssemblyLink--title']")))
        
        cardseturl = None
        cardseturl = cardset[0].get_attribute('href')

        driver.quit()
    except NoSuchElementException:
        driver.quit()
        print("No quizzes found for user topic.")
        return 
        
    except:
        driver.quit()
        print("Request timed out.")
        return 


    ###card set page
    driver = webdriver.Firefox()
    driver.get(cardseturl)

    time.sleep(2)
    html = driver.find_element('tag name', 'html')
    html.send_keys(Keys.PAGE_DOWN)


    cardlist = WebDriverWait(driver, 45).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SetPageTerms-term' and @aria-label='Term']//*[@class='TermText notranslate lang-en']")))

    alltext = []
    for i in range(len(cardlist)): 
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
    
    print("Done.")

    return QAdataframe

    #can delete later
    #attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', cardset[0])
    #print(attrs)


def webscrape_kahoot(url, setNum=1):
    from selenium import webdriver