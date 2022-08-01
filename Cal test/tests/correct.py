import pytest
from app. calculator import Calculator
class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_multiply_correctly(self):
       assert self.calc.multiply(self, 7, 7) == 49

   def test_division_correctly(self):
       assert self.calc.division(self, 100, 10) == 10

   def test_subtraction_correctly(self):
       assert self.calc.subtraction(self, 10, 5) == 5

   def test_adding_correctly(self):
       assert self.calc.adding(self, 7, 7) == 14