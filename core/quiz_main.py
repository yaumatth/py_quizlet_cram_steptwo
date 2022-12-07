class Quiz_quizlet():
	from py_quizlet_kahoot.network import webscraping
	from py_quizlet_kahoot.core import quiz_methods
	def __init__(self, topic, setNum = 1):
		self.topic = topic
		self.setNum = str(setNum)
		self.url = self.webscraping.url_quizlet(topic)
		try:
			self.__array = self.webscraping.webscrape_quizlet(self.url, self.setNum) #replace this to call QA object constructor... an array of QA objects should be stored here
		except:
			print("Sorry, no quizzes were found for:", self.topic)
		self.quiz_length = len(self.__array.index)
		self.QAs = self.quiz_methods.QA_constructor(self.__array, self.topic)

		
		
#class Quiz_kahoot():



class QA():
	def __init__(self, question, answer, topic):
		self.question = question
		self.answer = answer
		self.topic = topic
	
	#methods for setting quiz topic and `mark` (correct or incorrect)
