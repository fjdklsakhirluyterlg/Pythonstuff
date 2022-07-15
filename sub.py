# Python3 program to implement 3-D Vectors.
from math import sqrt

# Definition of Vector class
class Vector:

  # Initialize 3D Coordinates of the Vector
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  # Method to calculate magnitude of a Vector
  def magnitude(self):

    return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

  # Method to add to Vector
  def __add__(self, V):

    return Vector(self.x + V.x, self.y + V.y, self.z + V.z)

  # Method to subtract 2 Vectors
  def __sub__(self, V):

    return Vector(self.x - V.x, self.y - V.y, self.z - V.z)

  # Method to calculate the dot product of two Vectors
  def __xor__(self, V):

    return self.x * V.x + self.y * V.y + self.z * V.z

  # Method to calculate the cross product of 2 Vectors
  def __mul__(self, V):

    return Vector(self.y * V.z - self.z * V.y,
          self.z * V.x - self.x * V.z,
          self.x * V.y - self.y * V.x)

  # Method to define the representation of the Vector
  def __repr__(self):

    out = str(self.x) + "i "

    if self.y >= 0:
      out += "+ "
    out += str(self.y) + "j "
    if self.z >= 0:
      out += "+ "
    out += str(self.z) + "k"

    return out


if __name__ == "__main__":

  vec1 = Vector(1, 2, 2)
  vec2 = Vector(3, 1, 2)

  # Magnitude of vector1
  print("Magnitude of vector1:", vec1.magnitude())

  # String representation of vector
  print("String representation of vector1: " + str(vec1))

  # Addition of two vectors
  print("Addition of vector1 and vector2: " + str(vec1 + vec2))

  # Subtraction of two vectors
  print("Subtraction of vector1 and vector2: " + str(vec1 - vec2))

  # Dot product of two vectors
  print("Dot Product of vector1 and vector2: " + str(vec1 ^ vec2))

  # Cross product of two vectors
  print("Cross Product of vector1 and vector2: " + str(vec1 * vec2))
