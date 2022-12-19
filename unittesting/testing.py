import sys
import os
packagepath = os.path.abspath(__file__)

import re

packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)

print(packagepath)

if not packagepath in sys.path:
    sys.path.append(packagepath)

from network import translation

print(dir(translation))

#print(translation.translate("testing", 'fr'))


import pandas as pd
en = {'questions':['pencil', 'snake'], 'answers':['hammer', 'nail']}
df_en = pd.DataFrame(en)
temp = translation.translate(df_en, 'en')
en = {'questions':['WRONG', 'snake'], 'answers':['hammer', 'nail']}
df_en = pd.DataFrame(en)

print(pd.testing.assert_frame_equal(temp, df_en))

