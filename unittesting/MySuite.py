import unittest

try:
    from unittesting import TestQuizCoreOne
except:
    import TestQuizCoreOne

try:
    from unittesting import TestQuizCoreTwo
except:
    import TestQuizCoreTwo


def MySuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestQuizCoreTwo.TestMethods))
    suite.addTest(unittest.makeSuite(TestQuizCoreOne.TestMain))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


MySuite()
