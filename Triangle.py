'''
name = Oscar Tavara
'''

def classify_triangle(angle_a, angle_b, angle_c):
    """"classifies a triangle"""
    triangle = 'Isosceles'
    if angle_a > 200 or angle_b > 200 or angle_c > 200:
        triangle = 'InvalidInput'
    elif angle_a < 0 or angle_b < 0 or angle_c < 0:
        triangle = 'InvalidInput'
    elif not(isinstance(angle_a, int) and isinstance(angle_b, int) and isinstance(angle_c, int)):
        triangle = 'InvalidInput'
    elif ((angle_a >= (angle_b + angle_c)) or
          (angle_b >= (angle_a + angle_c)) or
          (angle_c >= (angle_a + angle_b))):
        triangle = 'NotATriangle'
    elif angle_a == angle_b and angle_b == angle_c:
        triangle = 'Equilateral'
    elif ((((angle_a ** 2) + (angle_b ** 2)) == (angle_c ** 2)) or
          (((angle_b ** 2) + (angle_c ** 2)) == (angle_a ** 2)) or
          (((angle_a ** 2) + (angle_c ** 2)) == (angle_b ** 2))):
        triangle = 'Right'
    elif ((angle_a not in (angle_b, angle_c)) and (angle_b != angle_c)):
        triangle = 'Scalene'
    return triangle
