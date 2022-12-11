class Quiz():
	from py_quizlet_kahoot.network import webscraping
	from py_quizlet_kahoot.network import translation
	from . import quiz_methods
	
	#checking internet connection
	if translation.internet_checker():
		print("Internet connection confirmed.")
	else:
		raise Exception("Internet connection is required!")
		
	def __init__(self, topic = "animals", site = "Quizlet", setNum = 1, language = "english", results = 	"off"):
		self.languageDict = {"english": "en", "chinese": "zh-tw", "french": "fr"}
		self.topic = topic
		self.site = site.lower()
		self.setNum = str(setNum) #up to a max of 8
		self.language = self.languageDict[language]
		self.results = results.lower()
	def quiz_create(self):
		if self.site == "quizlet":
			self.url = self.webscraping.url_quizlet(self.topic)
			try:
				self.__array = self.webscraping.webscrape_quizlet(self.url, self.setNum) 
			except:
				print("Sorry, no quizzes were found for:", self.topic)
		elif self.site == "cram":
			self.url = self.webscraping.url_cram(self.topic)
			try:
				self.__array = self.webscraping.webscrape_cram(self.url, self.setNum) 
			except:
				print("Sorry, no quizzes were found for:", self.topic)
		else:
			raise Exception("Not a valid site name. Please enter either \'Quizlet\' or \'Cram\'. Default is \'Quizlet\'.")
		self.quiz_length = len(self.__array.index)
		self.QAs = self.quiz_methods.QA_constructor(self.__array, self.topic)
		#self.hint = hint
		#self.displayResults = displayResults

	
	
	



class QA():
	def __init__(self, question, answer, topic):
		self.question = question
		self.answer = answer
		self.topic = topic
		self.mark = None
	
	def set_mark(value):
	#0 for wrong, 1 for correct
		self.mark = value
	
	
	
	

