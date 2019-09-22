from unittest import TestCase
from pathtrans import convert_windows_to_unix, convert_unix_to_windows


class TestCounting(TestCase):
    def test(self):
        self.check(r'C:\x', r'/c/x')
        self.check(r'C:\y', r'/c/y')
        self.check(r'D:\y', r'/d/y')
        self.check(r'X:\abc', r'/x/abc')
        self.check(r'A:\a\b\c', r'/a/a/b/c')
        self.check(r'A:\a x\b', r'/a/a x/b')

    def check(self, winpath, unixpath):
        self.assertEqual(unixpath, convert_windows_to_unix(winpath))
        self.assertEqual(winpath, convert_unix_to_windows(unixpath))
