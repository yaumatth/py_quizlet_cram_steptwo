# Documentation for `core' Subpackage


## `quiz_main` Module

### `class Quiz()`
This class takes no arguments and returns no values.

This class is the only object required to start and run quiz taking. 

Upon initializing an instance of this class: i) An instance of quiz is created, storing quiz settings, and ii) This instance of quiz is used by the user_control function (responsible for how user modifies quiz settings or answers quiz questions). Both of these allow quiz taking to occur.

### `class QA()`
This class takes no arguments and returns no values.

The purpose of this class is to provide a template data structure for storing questions/answers for a quiz. Specifically, this class holds, as attributes, questions, answers to that question, mark for question. Instances of QAs will be held inside an array, handled by the QA_constructor method in quiz_methods module. The array of QAs (and their corresponding held questions/answer attributes) will be iterated through to allow quiz-taking (showing QA.question, QA.answer) to occur.


### `quiz_create(theQuiz)`
This function receives a quiz object.

It will then call webscraping (depending on quiz object settings, e.g. cram or quizlet), of which scrapes for questions/answers.
In this function, questions/answers from webscraping will be processed in the manner described before (e.g. questions/answers stored in QA, array of QA created). Here, the created array of QAs are stored to the quiz object.

### `user_control (theQuiz)`
This class takes in a quiz object and returns no values.

The purpose of the class is to allow users to interact with the quiz, such as modifying quiz settings or answering questions. It does this through a series of loops and if-else conditions to detect user input. The appropriate action specified by user (e.g. start to start the quiz, exit to exit quiz) will be carried out by calling the appropriate functions from modules.

## `quiz_methods` Module

### `QA_constructor(QAdataframe, topic)`
This method takes in a dataframe and topic as arguments.

It takes in the dataframe of questions and answers built from webscraping. This dataframe is iterated through to store questions and answers into QA objects. Then the function will build an array of QAs which will be tied to the quiz in the quiz_create function.

### `take_the_quiz(quiz)`

This method takes in a quiz object and returns no value.

This function is responsible for showing questions and answers in the quiz. It does this through using a loop to iterate through the array of QA created by QA_constructor stored in the quiz object. It contains if-else control structures as well to allow hints or termination of quiz.

### `print_options(quiz)`
This method takes in quiz object and returns no value.

This function will be called before a quiz starts. It will print out a series of statement that shows users the current settings they are taking the quiz in (e.g. topic, language, question number)


### `results_plot(quiz)`
This method takes in quiz object as argument and returns no value.

This method will simply display the number of correct or incorrectly understood concepts for each question (stored as "mark"  in the QAs object) and import the matplotlib package to display plot of performance.


### `hints(word)`
This method takes in a string as argument and returns a modified string.

If string is a single word, it will only show random characters in the string (hiding others with underscores). If the string is a sentence of words, it will show random words in the sentence (hiding others with underscores). It does this by using random number generation for  number of characters (or words separated by spaces), and randomly converting some into underscores.
