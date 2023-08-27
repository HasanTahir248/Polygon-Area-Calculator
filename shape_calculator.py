class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
  
  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return (((self.width ** 2 + self.height ** 2) ** .5))

  def get_picture(self):
    if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
    pic = '*' * self.width + '\n'
    pics = pic * self.height
    return pics

  def get_amount_inside(self, ob):
    return self.get_area() // ob.get_area()

class Square(Rectangle):
  def __init__(self, length):
    self.length = length
    super().__init__(length, length)

  def __str__(self):
        return f'Square(side={self.width})'

  def set_side(self, length):
    self.width = length
    self.height = length

