import numpy as np
from fractions import Fraction

RJUST = 5

class SimplexTableau:
	def __init__(self, var_names, obj_vector, constraints, basis):
		self.var_names = var_names
		self.tab = np.empty([1 + len(constraints), 1 + len(var_names)], dtype=Fraction)
		self.tab[0,0] = Fraction(0)
		self.tab[0,1:] = obj_vector
		for i in range(1, len(constraints) + 1):
			self.tab[i] = constraints[i - 1]
		self.basis = basis
		self.ugly_print()

	def ugly_print(self):
		r, c = self.tab.shape
		print '(%d x %d)' % (r, c)
		print "".rjust(RJUST), "BSC".rjust(RJUST),
		for j in range(c - 1):
			print self.var_names[j].rjust(RJUST),
		print
		for i in range(r):
			if i > 0:
				print self.var_names[self.basis[i-1]].rjust(RJUST),
			else:
				print "c".rjust(RJUST),
			for j in range(c):
				print str(self.tab[i, j]).rjust(RJUST),
			print
		print