import unittest

#import all test classes
try:
    from unittesting import translation_testing
    from unittesting import quiz_main_testing
    from unittesting import quiz_methods_testing
except:
    import translation_testing
#from TestModule2 import TestSub

#run everything
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    #here is where you add your tests
    suite.addTest(unittest.makeSuite(translation_testing.translation))
    #suite.addTest(unittest.makeSuite(TestSub))
    suite.addTest(unittest.makeSuite(quiz_main_testing.TestMain))
    suite.addTest(unittest.makeSuite(quiz_methods_testing.TestMethods))    

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
