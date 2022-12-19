import unittest
from TestQuizCoreOne import TestMain
from TestQuizCoreTwo import TestMethods

def MySuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestMethods))
    suite.addTest(unittest.makeSuite(TestMain))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


MySuite()
