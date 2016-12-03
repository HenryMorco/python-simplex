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

	def pivot(self, row, column):
		pivot_value = self.tab[row, column]
		if pivot_value == 0:
			raise ValueError('Cannot pivot when entry is zero.')
		if row == 0 or column == 0:
			raise ValueError('Cannot pivot from constant row or column.')

		self.tab[row] /= pivot_value
		for i in range(self.tab.shape[0]):
			if i != row:
				col_value = self.tab[i, column]
				self.tab[i] -= col_value * self.tab[row]

		self.basis[row - 1] = column - 1
		self.ugly_print()

	def enter_variable(self, var_index):
		entering_column = var_index + 1
		exiting_variable = None
		exiting_row = None
		exit_ratio = None
		for r in range(1, self.tab.shape[0]):
			if self.tab[r, entering_column] > 0:
				cand_ratio = self.tab[r, 0] / self.tab[r, entering_column]
				if exit_ratio is None or cand_ratio < exit_ratio:
					exiting_variable = self.basis[r - 1]
					exiting_row = r
					exit_ratio = cand_ratio
		
		if exiting_row is not None:
			self.pivot(exiting_row, entering_column)

	def exit_variable(self, basis_index):
		exiting_row = basis_index + 1
		entering_variable = None
		entering_column = None
		enter_ratio = None

		for c in range(1, self.tab.shape[1]):
			if self.tab[exiting_row, c]  < 0:
				cand_ratio = - self.tab[0, c] / self.tab[exiting_row, c]
				if enter_ratio is None or cand_ratio < enter_ratio:
					entering_variable = c - 1
					entering_column = c
					enter_ratio = cand_ratio

		if entering_column is not None:
			self.pivot(exiting_row, entering_column)

	def get_current_solution(self):
		solution = np.full(self.tab.shape[1], Fraction(0), dtype=Fraction)
		solution[0] = - self.tab[0, 0]
		for bi in range(len(self.basis)):
			solution[self.basis[bi] + 1] = self.tab[bi + 1, 0]
		return solution