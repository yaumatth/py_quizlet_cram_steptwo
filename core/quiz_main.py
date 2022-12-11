class Quiz():
	from py_quizlet_kahoot.network import webscraping
	from py_quizlet_kahoot.core import quiz_methods
	def __init__(self, topic, site = "Quizlet", setNum = 1):
		#matts options
		self.topic = topic
		self.site = site.lower()
		self.setNum = str(setNum) #up to a max of 8
		if self.site == "quizlet":
			self.url = self.webscraping.url_quizlet(topic)
			try:
				self.__array = self.webscraping.webscrape_quizlet(self.url, self.setNum) 
			except:
				print("Sorry, no quizzes were found for:", self.topic)
		elif self.site == "cram":
			print("cram methods will go here")
		
		else:
			raise Exception("Not a valid site name. Please enter either \'Quizlet\' or \'Cram\'. Default is \'Quizlet\'.")
		self.quiz_length = len(self.__array.index)
		self.QAs = self.quiz_methods.QA_constructor(self.__array, self.topic)

		
		
#class Quiz_kahoot():



class QA():
	def __init__(self, question, answer, topic):
		self.question = question
		self.answer = answer
		self.topic = topic
		self.mark = None
	
	def set_mark(value):
	#0 for wrong, 1 for correct
		self.mark = value
	
	
	
	

