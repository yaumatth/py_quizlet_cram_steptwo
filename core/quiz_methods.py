import random 
from IPython.display import clear_output


def QA_constructor(QAdataframe, topic):
	import pandas as pd
	from . import quiz_main
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
	
	
	theInput = "hoho"
	for i in range(quiz.quiz_length):         
		print("Question " + str(i + 1) + " of " + str(quiz.quiz_length) + ": " + quiz.QAs[i].question + 
		"\nPress enter for the answer, hint for hints, or exit to exit")
		while theInput not in ["", "exit"]:
			theInput = input()
			if theInput == "hint":
				print(hints(quiz.QAs[i].answer))
		if theInput == "":
			print("Answer:")
			print(quiz.QAs[i].answer) 
			if quiz.results == "on":
				rightwrong = input("Did you understand this concept? (Y/N).").lower()
				while not ((rightwrong == "y") or (rightwrong == "n")):
					rightwrong = input("Please specify Y or N.").lower()
				array[i].mark = rightwrong
				theInput = "placeHolder"
				clear_output(wait=True)                
			else:
				theInput = input()
				if theInput != "exit":
					clear_output(wait=True)  
					theInput = "placeHolder"
				elif theInput == "exit":
					break
		elif theInput == "exit":
			break

	#print("\nWell done! Quiz is finished.")

	#call plotting methods
	#if quiz.displayResults.lower() == "on":
	#	results_plot(quiz)




def print_options(quiz):
	import time
	print("You are about to start the quiz with the following options...:")
	time.sleep(2)	
	print("Your topic:", quiz.topic)
	time.sleep(1)	
	print("With questions from:", quiz.site)
	time.sleep(1)
	print("Using question bank number:", quiz.setNum)
	time.sleep(1)
	print("Total number of questions:", quiz.quiz_length)
	time.sleep(1)
	print("Good luck!")
	


def results_plot(quiz):
	import matplotlib.pyplot as plt

	length = quiz.quiz_length
	array = []
	for i in range(length):
		array.append(quiz.QAs[i].mark)

	plotting = [array.count('r'), array.count('w')]

	print("Right:", plotting[0])
	print("Wrong:", plotting[1])
	print("Grade:", round(plotting[0]/length * 100), "%")

	plt.pie(plotting, labels = ['Right', 'Wrong'])
	plt.show()


def hints(word):
	hintAnswer = []
	if len(word.split(" ")) != 1:
		randomLister = []
		splitSentence = word.split(" ")
		for i in range(len(splitSentence)):
			randHint = random.randint(0, len(splitSentence))
			randomLister.append(randHint)
		for j in range(len(splitSentence)):
			appendWord = splitSentence[j]
			if j in randomLister:
				hintAnswer.append(appendWord)
			if j not in randomLister:
				theWord = splitSentence[j]
				for k in range(len(theWord)):
					theWord = theWord.replace(theWord[k], "_")
				hintAnswer.append(theWord)
	elif len(word.split(" ")) == 1:
		randList = []
		theWord = word
		for l in range(len(theWord)):
			randHint = random.randint(0, len(theWord))
			randList.append(randHint)
		for m in range(len(theWord)):
			if m not in randList:
				theWord = theWord.replace(theWord[m], "_")
		hintAnswer.append(theWord)
	return " ".join(hintAnswer)
        