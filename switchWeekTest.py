from challenges import switchWeek
import unittest
class switchWeekTest(unittest.TestCase):
    def test_challenge1(self):
        sw = switchWeek.switchWeek()
        damages = ["FRONT END", "FRONT END", "REAR END", "blah"]
        for dd in damages:
             sw.switch(dd)
        # print(sw.switch("FRONT END"))
        #
        # print(sw.switch("FRONT END"))
        # print(sw.switch("FRONT END"))
        # print(sw.switch("FRONT END"))
        # print(sw.switch("blah"))
if __name__ == '__main__':
    unittest.main()

