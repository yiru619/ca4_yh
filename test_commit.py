#10273765

import unittest

from simple_4 import *

# test
class MyTest(unittest,TestCase):
    def testreadfile(self):
        self.assertEqual(read_file('test_changes_python.txt'), ['r1551925 | Thomas | 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015) | 1 line', 'Changed paths:', 'A /cloud/personal/client-international/android/branches/android-15.2-solutions/clients/client/res/drawable-xxxhdpi (from /cloud/personal/client-international/android/branches/android-15.2-solutions/clients/client/res/drawablw-xxxhdpi:1551688)', 'D /cloud/personal/client-international/android/branches/android-15.2-solutions/clients/client/res/drawablw-xxxhdpi', 'A /cloud/personal/client-international/android/branches/android-15.2-solutions/clients/client-bt/res/drawable-xxxhdpi (from /cloud/personal/client-international/android/branches/android-15.2-solutions/clients/client-bt/res/drawablw-xxxhdpi:1551922)', 'D /cloud/personal/client-international/android/branches/android-15.2-solutions/clients/client-bt/res/drawablw-xxxhdpi', ''])


    def testgetauthor(self):
        self.assertEqual(get_stat_keyword(commits,'author'),'Thomas')

    def testgetlines(self):
        self.assertEqual(get_stat_keyword(commits, '1'),'348')

   

if __name__ == '__main__':
    unittest.main()