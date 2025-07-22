class Student:
  #everything that goes inside of this, everything that's indented like this goes inside out student class
  #basically what we can do inside student class is basically we can define a bunch of attributes about students
  #I can use strings, numbers and boolean in order to map out what a student should be and what a student should have.

#initialized function helps to basically map out what a student should have
  def __init__(self, name, major, gpa, is_on_probation): #these student, gpa etc are just values we passed in 
    
    #we assign value to actual attributes  of the object 
    self.name = name #the name of the student object is eual to the name we passed in.
    self.major = major #self is referring to actual information.
    self.gpa = gpa
    self.is_on_probation = is_on_probation
#so now that this class is defined, I am going to use inside my oython file.

  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False
  
