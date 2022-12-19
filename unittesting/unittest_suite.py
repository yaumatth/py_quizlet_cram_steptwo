import unittest

#importing stuff
import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

#import all test classes
<<<<<<< HEAD
from unittesting import translation_testing
from unittesting import webscraping_testing
from unittesting import TestQuizCoreOne
from unittesting import TestQuizCoreTwo

=======
try:
    from unittesting import translation_testing
    from unittesting import quiz_main_testing
    from unittesting import quiz_methods_testing
except:
    import translation_testing
#from TestModule2 import TestSub
>>>>>>> 8dc871098bde24c68c881dd2e5cf94cb4a1788ee

#run everything
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    #here is where you add your tests
    suite.addTest(unittest.makeSuite(translation_testing.translation))
<<<<<<< HEAD
    suite.addTest(unittest.makeSuite(translation_testing.testing_speed_warning))
    suite.addTest(unittest.makeSuite(webscraping_testing.url_builders))
    suite.addTest(unittest.makeSuite(TestQuizCoreTwo.TestMethods))
    suite.addTest(unittest.makeSuite(TestQuizCoreOne.TestMain))
    suite.addTest(unittest.makeSuite(webscraping_testing.webscraping_funcs))
=======
    #suite.addTest(unittest.makeSuite(TestSub))
    suite.addTest(unittest.makeSuite(quiz_main_testing.TestMain))
    suite.addTest(unittest.makeSuite(quiz_methods_testing.TestMethods))    
>>>>>>> 8dc871098bde24c68c881dd2e5cf94cb4a1788ee

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
