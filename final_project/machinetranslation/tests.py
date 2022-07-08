import unittest
from translator import english_to_French,french_to_English

class TestTranslator_f2E(unittest.TestCase):
    def TestCasef2E(self):
        self.assertNotEqual(french_to_English('null'),'')
        self.assertNotEqual(french_to_English('Bonjour'),'Hello')

class TestTranslator_e2F(unittest.TestCase):
    def TestCasee2F(self):
        self.assertNotEqual(english_to_French('null'),'')
        self.assertNotEqual(english_to_French('Hello'),'Bonjour')

unittest.main()