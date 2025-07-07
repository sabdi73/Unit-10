"""
Program Name: lab 10
Author: said abdi
Purpose: unit 10 lab
Date: 07/02/2025
"""

def adjust_rotation(degrees):
 try:
  degrees = float(degrees)
  adjusted = degrees % 360
 if adjusted < 0:
 return adjusted
ValueError("it has to be a numeric value")
