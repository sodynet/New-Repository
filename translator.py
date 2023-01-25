https://api.us-east.language-translator.watson.cloud.ibm.com/instances/6bbda3b3-d572-45e1-8c54-22d6ed9e52c2
  def englishTofrench(frenchText):translator = Translator()out = translator.translator("english", dest="fr")print(out)
    ]def frenchToEnglish(frenchText):translator = Translator()out = translator.translator("french", dest-"en")print(out)
      import unittest

class TestExample(unittest.TestCase):

    def test_queries(self):
        self.assertEqual(q1(), q2())

if __name__ == '__main__':
    unittest.main()
