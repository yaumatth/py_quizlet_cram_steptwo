# Documentation for `network` subpackage

Some of these are quite similar to the [README.md](../README.md) file in the parent folder.


## `webscraping.py` Module


### `url_cram` and `url_quizlet`

These functions take in a topic argument as a string, and return a web URL as a string.

In order to webscrape the questions, an appropriate search URL must be constructed. These functions take in the topic as a string, replace the spaces with dashes (Quizlet) or addition signs (Cram) and concatenate them with the default search URL. This URL is then passed to the webscraping functions.


### `webscrape_quizlet` and `webscrape_cram`

These functions receive a web URL and a `setNum`, and return a pandas dataframe (of questions and answers).

These functions take the URL from the previous functions and query the appropriate website using 'Selenium' headless browsing package (anti-robot server properties prevented traditional webscraping techniques). Once the page has finished loading, the function finds the link to the appropriate card set (based on `setNum`). This may take several moments, as the loading of the ads makes the process much slower (this is especially true for Cram quizzes).

Next, this link is used to open a second browser that is specific to the desired cardset. The function then finds all the questions and answers to the cards, and assigns them to separate arrays.

Lastly, the `dataframe_builder` function is called (see below).


### `dataframe_builder`

This function receives two arrays, and returns a pandas dataframe.

This function first imports `pandas` so that dataframe operations can be completed. It then puts the two arrays of questions and answers (previously created by the webscraping functions) into a single pandas dataframe, which is returned and assigned to the `Quiz()` attribute `.__array`.




## `translation` Module


### `internet_checker`

This function does not take any arguments. It returns `True` if there is an internet connection, and returns `False` if there is no internet connection.

Since this package requires an internet connection, it does not make sense to try to create the `Quiz()` object without internet access. This function checks whether or not the user has an internet connection, and will abort `Quiz()` creation if they do not.


### `speed_warning`

This function does not take any arguments or return anything. It only prints.

Before beginning to webscrape the quiz, an internet speed warning is printed. This warning tells the user that "Functions requiring internet connection may take a while. Please do not interact with your device until the process is finished". This ensures a smooth quiz creation without any interuptions.


### `translate`

This function takes in a 2 column pandas dataframe labelled \'questions\' and \'answers\' and returns the same dataframe with translated text. It also takes in the language to translate to. This function returns a translated 2 column pandas dataframe.

Before the `.__array` of questions and answers are sorted into `QA()` objects, if the user selected a language other than English, the array is passed to `translate`. This function uses the convinient `googletrans` package to iteratively translate each cell in the question answer dataframe stored in `.__array` (overwriting contents with new text).

Please note that a specific version of `googletrans` is needed. For some reason, only the `3.1.0a0` version works.
