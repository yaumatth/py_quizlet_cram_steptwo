################
# webscraping module
import network.webscraping as ws
###############

#url_quizlet
#url_cram
#webscrape_quizlet
#webscrape_cram
#dataframe_builder
class NAME(unittest.TestCase): # test class
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")

    def test_url_quizlet(self): # test case
        self.assertEqual(ws.url_quizlet('teacher'), 'https://quizlet.com/search?query=teacher&type=sets&page=1&creator=teacher')
        self.assertEqual(ws.url_quizlet('cell bio'), 'https://quizlet.com/search?query=cell-bio&type=sets&page=1&creator=teacher')
        self.assertEqual(func, ans)
        self.assertEqual(func, ans)
    def test_NAME(self): # test case
        self.assertEqual(func, ans)
        self.assertEqual(func, ans)
        self.assertEqual(func, ans)
        self.assertEqual(func, ans)
unittest.main(argv=[''], verbosity=2, exit=False)
