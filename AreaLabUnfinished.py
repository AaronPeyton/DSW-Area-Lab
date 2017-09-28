import math
import unittest

def circleArea(radius): #no return type nor parameter type
    return radius**2.0 * math.pi

def rectArea(base, height):
	return base * height

def trapArea(base1, base2, height):
	return height * (base1 + base2) / 2.0

def triArea(base,height):
    return base * height / 2.0

def sqArea(sideLength):
    return sideLength**2.0

""" tests for previously written functions"""
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25*math.pi, 'testCircleArea')
    def testRectArea(self):
        self.assertEqual(rectArea(4,5), 4*5, 'testRectArea')
    def testTrapArea(self):
        self.assertEqual(trapArea(4,5,6), 6 * (4 + 5) / 2, 'testTrapArea')
    def testTriArea(self):
        self.assertEqual(triArea(3,3), 4.5, 'testTriArea')
    def testSqArea(self):
        self.assertEqual(sqArea(2), 4, 'testSqArea')
