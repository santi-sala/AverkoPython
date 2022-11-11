class Complex():
	#Attributes of the class, not just of the instance
	imaginary = "x * x + 1 = 0"

	#Constructors and its attributes
	def __init__(self, a, b):		
		self.a = a
		self.b = b
	
	def getComplexNumber(self):
		return 'A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is imaginary unit.'
	
	def getImaginary(self):
		return (f"The imaginary unit is: {Complex.imaginary}")

	def getRealNumbers(self):
		return self.a * self.b

	def set_a(self, number):
		self.a = number

	def set_b(self, number):
		self.a = number
		

myNumber = Complex(1, 2)
print(myNumber.a)
print(myNumber.b)
print(myNumber.imaginary)
print(myNumber.getComplexNumber())
print(myNumber.getImaginary())
print(myNumber.getRealNumbers())
myNumber.set_a(5)
myNumber.set_a(20)
print(myNumber.getRealNumbers())
print(myNumber.a)


		
