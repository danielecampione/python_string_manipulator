import unittest
from string_manipulator_frame import StringManipulator

class TestStringManipulator(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(StringManipulator.upper("ciao"), "CIAO")

    def test_lower(self):
        self.assertEqual(StringManipulator.lower("CIAO"), "ciao")

    def test_capitalize(self):
        self.assertEqual(StringManipulator.capitalize("ciao"), "Ciao")

    def test_title(self):
        self.assertEqual(StringManipulator.title("ciao mondo"), "Ciao Mondo")

    def test_swapcase(self):
        self.assertEqual(StringManipulator.swapcase("Ciao Mondo"), "cIAO mONDO")

    def test_strip(self):
        self.assertEqual(StringManipulator.strip("  ciao  "), "ciao")

    def test_replace(self):
        self.assertEqual(StringManipulator.replace("ciao", 'a', 'X'), "ciXo")

    def test_split(self):
        self.assertEqual(StringManipulator.split("ciao mondo"), "['ciao', 'mondo']")

    def test_join(self):
        self.assertEqual(StringManipulator.join("ciao mondo"), "ciao-mondo")

    def test_count(self):
        self.assertEqual(StringManipulator.count("ciao", 'a'), "1")

    def test_find(self):
        self.assertEqual(StringManipulator.find("ciao mondo", "mondo"), "5")

    def test_startswith(self):
        self.assertEqual(StringManipulator.startswith("ciao mondo", "ciao"), "True")

    def test_endswith(self):
        self.assertEqual(StringManipulator.endswith("ciao mondo", "mondo"), "True")

    def test_isalpha(self):
        self.assertEqual(StringManipulator.isalpha("ciao"), "True")

    def test_isdigit(self):
        self.assertEqual(StringManipulator.isdigit("123"), "True")

    def test_isalnum(self):
        self.assertEqual(StringManipulator.isalnum("ciao123"), "True")

    def test_isspace(self):
        self.assertEqual(StringManipulator.isspace("   "), "True")

    def test_islower(self):
        self.assertEqual(StringManipulator.islower("ciao"), "True")

    def test_isupper(self):
        self.assertEqual(StringManipulator.isupper("CIAO"), "True")

    def test_istitle(self):
        self.assertEqual(StringManipulator.istitle("Ciao Mondo"), "True")

    def test_zfill(self):
        self.assertEqual(StringManipulator.zfill("42", 5), "00042")

    def test_translate(self):
        self.assertEqual(StringManipulator.translate("ciao"), "ciou")

    def test_re_sub(self):
        self.assertEqual(StringManipulator.re_sub("123abc456"), "NUMEROabcNUMERO")

    def test_format(self):
        self.assertEqual(StringManipulator.format("mondo"), "Ciao, mondo")

    def test_f_string(self):
        self.assertEqual(StringManipulator.f_string("mondo"), "Ciao, mondo")

    def test_encode(self):
        self.assertEqual(StringManipulator.encode("ciao"), b'ciao')

    def test_decode(self):
        self.assertEqual(StringManipulator.decode("ciao"), "ciao")

    def test_counter(self):
        self.assertEqual(StringManipulator.counter("ciao"), "Counter({'c': 1, 'i': 1, 'a': 1, 'o': 1})")

    def test_unicodedata(self):
        self.assertEqual(StringManipulator.unicodedata("a"), "LATIN SMALL LETTER A")

    def test_textwrap(self):
        self.assertEqual(StringManipulator.textwrap("ciao mondo", width=5), "ciao\nmondo")

    def test_template(self):
        self.assertEqual(StringManipulator.template("mondo"), "Ciao, mondo!")

    def test_reduce(self):
        self.assertEqual(StringManipulator.reduce("ciao mondo"), "ciao mondo")


if __name__ == "__main__":
    unittest.main()