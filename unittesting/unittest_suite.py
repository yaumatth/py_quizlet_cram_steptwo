import unittest

#import all test classes
try:
    from unittesting import translation_testing
except:
    import translation_testing

try:
    from unittesting import webscraping_testing
except:
    import webscraping_testing


#run everything
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    #here is where you add your tests
    suite.addTest(unittest.makeSuite(translation_testing.translation))
    suite.addTest(unittest.makeSuite(translation_testing.testing_speed_warning))
    suite.addTest(unittest.makeSuite(webscraping_testing.url_builders))
    suite.addTest(unittest.makeSuite(webscraping_testing.webscraping_funcs))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
