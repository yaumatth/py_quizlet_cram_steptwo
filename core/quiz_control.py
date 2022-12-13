def start():

	import py_quizlet_kahoot.core.quiz_main as main
	import py_quizlet_kahoot.core.quiz_methods as methods
	from IPython.display import clear_output
	theInput = ""

	#main loop
	while theInput.lower() != "exit":
	    clear_output(wait=True)  
	    theInput = input("You are about to start a quiz on " + theQuiz.topic + " from the site " + theQuiz.site
	                   + ".\nPlease choose from the following options: \n   Start (starts the quiz!)"
	                   + "\n   Settings (change settings)\n   Exit (quit)")
	    if theInput == "start":
	        theQuiz.quiz_create()
	        methods.take_the_quiz(theQuiz)
	    if theInput.lower() == "settings":
	        while theInput.lower() != "exit":
	            clear_output(wait=True)
	            theInput = input("What options do you want to change?. \n   Topic (Quiz topic on "
	                             + theQuiz.topic + ")\n   Language (" + theQuiz.language + ")\n   Site (" + theQuiz.site
	                             + ")\n   Set (question bank number " + theQuiz.setNum + ")\n   Back\n   Exit")
	            if theInput.lower() == "back":
	                break;
	            elif theInput.lower() == "language":
	                while theInput.lower() != "exit":
	                    theInput = input("Language options are  ")
	                    if theInput == "back":
	                        break;
	            elif theInput.lower() == "topic":
	                theInput = input("Enter topic you want to be quizzed on: ")
	                theQuiz.topic = theInput
	            elif theInput.lower() == "site":
	                theInput = input("Enter site you want questions from (Quizlet or Cram):")
	                while theInput not in ["quizlet", "cram"]:
	                    theInput = input("Please enter Quizlet or Cram")
	                if theInput.lower() == "quizlet":
	                    theQuiz.site = "quizlet"
	                elif theInput.lower() == "cram":
	                    theQuiz.site = "cram"
	            elif theInput.lower() == "set":
	                theInput = input("Please choose a question bank from 1 to 8:")
	                while theInput not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
	                    theInput = input("Please only specify question bank values from 1 to 8")
	                theQuiz.setNum = theInput
