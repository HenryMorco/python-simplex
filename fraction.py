class Fraction:

	@staticmethod
	def greatest_common_divisor(a, b):
		if b == 0:
			return abs(a)
		else:
			return Fraction.greatest_common_divisor(b, a % b)

	def __init__(self, num, den=1):
		if den == 0:
			raise ValueError("Denominator cannot be zero.")

		gcd = Fraction.greatest_common_divisor(num, den)
		num /= gcd
		den /= gcd
		
		if den < 0:
			num *= -1

		self.numerator = int(num)
		self.denominator = int(den)

	def __str__(self):
		if abs(self.denominator) == 1:
			return str(self.numerator)
		else:
			return "{0!s}/{1!s}".format(self.numerator, self.denominator)

	def __add__(self, other):
		return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)

	def __iadd__(self, other):
		self = self + other
		return self

	def __sub__(self, other):
		return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

	def __isub__(self, other):
		self = self - other
		return self

	def __mul__(self, other):
		return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

	def __imul__(self, other):
		self = self * other
		return self

	def __div__(self, other):
		if other.numerator == 0:
			raise ZeroDivisionError("division by zero fraction")
		return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

	def __idiv__(self, other):
		self = self / other
		return self

	def as_float(self):
		return float(self.numerator) / float(self.denominator)