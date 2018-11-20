class Student:

 comparisons = 0  # кількість операцій порівняння
 swaps = 0


 @staticmethod
 def comperisons_method():
        Student.comparisons +=1
        return Student.comparisons

 @staticmethod
 def swap_method():
     Student.swaps += 1
     return Student.swaps

 def __init__(self, name, surname, rate, height):
      self.name = name
      self.surname = surname
      self.rate = rate
      self.height = height

 def __str__(self):
   return "name: " + self.name + " rate: " + str(self.rate) + " height: " + str(self.height)