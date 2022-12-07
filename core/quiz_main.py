class Quiz_quizlet():
	from py_quizlet_kahoot.network import webscraping
	def __init__(self, topic, setNum = 1):
		self.topic = topic
		self.setNum = str(setNum)
		self.url = self.webscraping.url_quizlet(topic)
		self.temp = self.webscraping.webscrape_quizlet(self.url, self.setNum) #replace this to call QA object constructor... an array of QA objects should be stored here

		
		
#class Quiz_kahoot():

