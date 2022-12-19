########
#NOTE FOR TA:
#there is only one set case here, as there is only testable function in thie module. To compensate for this, I added an extra test case to 'webscraping_testing.py'


import unittest


#translate
class translation(unittest.TestCase): # test class
    import pandas as pd

    #trying to import package
    import sys
    import os
    import re
    packagepath = os.path.abspath(__file__)
    packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
    if not packagepath in sys.path:
        sys.path.append(packagepath)

    from network import translation



    #set up and tear down
    def setUp(self):
        import pandas as pd
        #print("setup")
        self.en = {'questions':['pencil', 'snake'], 'answers':['hammer', 'nail']}
        self.fr = {'questions':['crayon', 'serpent'], 'answers':['marteau', 'clou']}
        self.ch = {'questions':['蠟筆', '蛇'], 'answers':['錘子', '指甲']}
        self.df_en = pd.DataFrame(self.en)
        self.df_fr = pd.DataFrame(self.fr)
        self.df_ch = pd.DataFrame(self.ch)

    def tearDown(self):
        #print("teardown")
        del self.en
        del self.fr
        del self.ch
        del self.df_en
        del self.df_fr
        del self.df_ch

    #translate function
    def test_translate(self): # test case
        self.assertEqual(None, self.pd.testing.assert_frame_equal(self.translation.translate(self.df_en, 'en'), self.df_en))
        self.assertEqual(None, self.pd.testing.assert_frame_equal(self.translation.translate(self.df_en, 'fr'), self.df_fr))
        self.assertEqual(None, self.pd.testing.assert_frame_equal(self.translation.translate(self.df_en, 'zh-tw'), self.df_ch))
unittest.main(argv=[''], verbosity=2, exit=False)
