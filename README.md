# py-quizlet-cram
A package for taking Quizlet and Cram quizzes in Python.

# Introduction

The purpose of this package is to enable users to take online quizzes from [Quizlet](https://quizlet.com/) and [Cram](https://www.cram.com/) in Jupyter Notebook. Quizzes are web scraped from these websites based on the provided topic and card set number. Questions and answers are shown interatively, with the user selecting whether they got each question right or wrong. A pie chart showing the quiz results is plotted upon quiz completion.

**Please note the list of dependencies in the `dependencies.txt` file.**

If at any time the webscraping functions timeout or fail, close the browser that was automatically opened, and run the command again. This usually fixes any issues.

A video demonstrating the use of this package can be found at [this link]().


# Creating a Quiz() object

In order to create a quiz object, the user should assign Quiz() to a variable.

> `quiz1 = Quiz()`

Upon creating a `Quiz()`, the first function called is


## `internet_checker`

Since this package requires an internet connection, it does not make sense to try to create the `Quiz()` object without internet access. This function checks whether or not the user has an internet connection, and will abort `Quiz()` creation if they do not.

## `speed_warning`

Before beginning to webscrape the quiz, an internet speed warning is printed. This warning tells the user that "Functions requiring internet connection may take a while. Please do not interact with your device until the process is finished". This ensures a smooth quiz creation without any interuptions.


## `options_setter`

text

After the options are set, the quiz is created via network functions.


## `quiz_create`

text


### `url_cram` and `url_quizlet`

In order to webscrape the questions, an appropriate search URL must be constructed. These functions take in the topic as a string, replace the spaces with dashes (Quizlet) or addition signs (Cram) and concatenate them with the default search URL.

This URL is then passed to the webscraping functions.


### `webscrape_quizlet` and `webscrape_cram`

These functions take the URL from the previous functions and query the appropriate website using 'Selenium' headless browsing package (anti-robot server properties prevented traditional webscraping techniques). Once the page has finished loading, the function finds the link to the appropriate card set (based on `setNum`). This may take several moments, as the loading of the ads makes the process much slower (this is especially true for Cram quizzes).

Next, this link is used to open a second browser that is specific to the desired cardset. The function then finds all the questions and answers to the cards, and assigns them to separate arrays.

Lastly, the `dataframe_builder` function is called, which puts the two arrays of questions and answers into a single pandas dataframe, which is returned and assigned to the `Quiz()` attribute `__array`.


### `QA_constructor`

The final step of quiz creation is to assign each question-answer pair in the `.__array` attribute to a separate `QA()` object. Each `QA()` object contains a single question, answer, quiz topic, and a `mark` attribute that stores an `r` if the user answered the question correct, or a `w` if the user answered the question incorrectly. After the `QA_constructor` creates the appropriate number of `QA()` objects, it assigns them to an array which is then stored inside the `Quiz()` attribute `.QAs`.


## translatefunction

text



# Taking a Quiz

Once a quiz has been created, it can be taken using the `take_the_quiz()` function. This function should be called on a `Quiz()` object without storing the output in a variable, as shown here:

> `take_the_quiz(quiz1)`

## `print_options`

Upon calling `take_the_quiz()` on a `Quiz()` object, the first function to run is `print_options`. This function prints the options of the quiz that is about to be taken.

## Main Loop

The main loop of the `take_the_quiz()` function does the following steps:

1. Print the question, then wait for user to hit Enter key.
2. Print the hint, if hint option is on.
3. Print the answer.
4. Ask the user if they got the question correct or incorrect. This input is used later by `results_plot`.
5. Return to step 1. if there are more questions.
6. Once all questions have been asked, print "Well done! Quiz is finished".
7. If `displayResults` is on, `results_plot` is called.


## hintoptions

text


## `results_plot`

If on, this function prints the \# of questions answered correctly, \# of questions answered incorrectly, a percentage grade, and a pie chart showing the results.
