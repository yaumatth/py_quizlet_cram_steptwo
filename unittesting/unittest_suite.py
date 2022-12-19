import unittest

#import all test classes
import translation_testing
#from TestModule2 import TestSub

#run everything
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    #here is where you add your tests
    suite.addTest(unittest.makeSuite(translation_testing.translation))
    #suite.addTest(unittest.makeSuite(TestSub))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
