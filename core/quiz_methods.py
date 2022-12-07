def QA_constructor(QAdataframe, topic):
	import pandas as pd
	from py_quizlet_kahoot.core import quiz_main
	array = []
	for i in range(len(QAdataframe.index)):
		temp = quiz_main.QA(QAdataframe.loc[i, "questions"], QAdataframe.loc[i, "answers"], topic)
		array.append(temp)
		
	return array
