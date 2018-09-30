
import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
    
    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(44, 36, 29), 'Scalene', '44,36,29 should be scalene')
    
    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(5, 5, 4), 'Isosceles', '5,5,4 should be isosceles')

    def testInvalidInput(self): 
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput', '201,201,201 should be invalid')
        
    def testUpperLimit(self): 
        self.assertEqual(classify_triangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')
        
    def testLowerLimit(self): 
        self.assertEqual(classify_triangle(0, 0, 0),'NotATriangle', '0,0,0 is a vaild input, but not a triangle')

    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(200, 1, 1),'NotATriangle', '200,1,1, is not a valid triangle')
        
    def testASidesIsNotAnIntegers(self): 
        self.assertEqual(classify_triangle(1.1, 1, 1),'InvalidInput', '1.1 is not a integer')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

