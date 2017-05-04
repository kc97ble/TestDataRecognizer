import unittest

from app.spec import Spec
from app.testcase import TestCase


class CheckSpec(unittest.TestCase):
    def setUp(self):
        self.spec1 = Spec(".in", ".out", '$')
        self.spec2 = Spec("input.", "ans.", '^')

    def test_match(self):
        assert self.spec1.match(TestCase("1.in", "1.out")) is True
        assert self.spec2.match(TestCase("input.105", "ans.105")) is True
        assert self.spec2.match(TestCase("input.105", "ans.105 ")) is False
        assert self.spec2.match(TestCase("ans.103", "input.103")) is False

    def test_vowel_score(self):
        assert self.spec1.vowel_score() == 3
        assert self.spec2.vowel_score() == 1
