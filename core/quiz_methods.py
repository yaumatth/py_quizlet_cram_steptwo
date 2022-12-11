def QA_constructor(QAdataframe, topic):
	import pandas as pd
	from py_quizlet_kahoot.core import quiz_main
	array = []
	for i in range(len(QAdataframe.index)):
		temp = quiz_main.QA(QAdataframe.loc[i, "questions"], QAdataframe.loc[i, "answers"], topic)
		array.append(temp)
		
	return array
	




def take_the_quiz(quiz):
	from py_quizlet_kahoot.core import quiz_main
	import time
	assert isinstance(quiz, quiz_main.Quiz)
	
	length = quiz.quiz_length
	array = quiz.QAs

	print_options(quiz)
	
	input("Press Enter to start quiz... ")
	
	for i in range(length):
		print("\nQuestion " + str(i+1) + ":")
		print(array[i].question)
		input("Press Enter to see answer... ")
		print("\nAnswer:")
		print(array[i].answer)
		time.sleep(2)
		print("Did you get this question right or wrong?")
		time.sleep(0.5)
		rightwrong = input("Type \'R\' for right, or \'W\' for wrong.").lower()
		while not ((rightwrong == "r") or (rightwrong == "w")):
			print("Sorry! That is not one of the allowed options.")
			rightwrong = input("Type \'R\' for right, or \'W\' for wrong.").lower()
		array[i].mark = rightwrong
	
	print("\nWell done! Quiz is finished.")
	
	#call plotting methods
	results_plot(quiz)
		
		
		

def print_options(quiz):
	import time
	print("You are now taking a quiz with the following options:")
	time.sleep(2)	
	print("Topic:", quiz.topic)
	time.sleep(0.5)	
	print("Site:", quiz.site)
	time.sleep(0.5)
	print("Set number:", quiz.setNum)
	time.sleep(0.5)
	print("Number of questions:", quiz.quiz_length)
	time.sleep(0.5)

	

def results_plot(quiz):
	import matplotlib.pyplot as plt
	
	length = quiz.quiz_length
	array = []
	for i in range(length):
		array.append(quiz.QAs[i].mark)
	
	plotting = [array.count('r'), array.count('w')]
	
	print("Right:", plotting[0])
	print("Wrong:", plotting[1])
	
	plt.pie(plotting, labels = ['Right', 'Wrong'])
	plt.show()
