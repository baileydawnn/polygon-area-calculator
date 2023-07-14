from math import sqrt 

class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width
  
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area
  
  def get_perimeter(self):
    perimeter = self.width * 2 + self.height * 2
    return perimeter
    
  def get_diagonal(self):
    diagonal = sqrt(self.width**2 + self.height**2)
    return diagonal


  def get_picture(self):
    if self.width <= 50 and self.height <= 50:
      shape = ""
      for i in range(self.height):
        shape += "*" * self.width + "\n"
      return shape
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    if isinstance(shape, Rectangle):
        return self.get_area() // shape.get_area()
    else:
        return "Invalid shape"
  

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    self.side = side
    
  def __str__(self):
    return f"Square(side={self.side})"

  def set_side(self, side):
    self.side = side
    self.set_width(side)
    self.set_height(side)
