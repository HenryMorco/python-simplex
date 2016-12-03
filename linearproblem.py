from fractions import Fraction
from enum import Enum
from simplextableau import SimplexTableau

Objective = Enum('Objective', 'max min')
Ineq = Enum('Ineq', 'ge le eq')

class LinearProblem:
	"""For now assume a standard form linear problem, i.e. all constraints are equalities and all variables are nonneg"""
	def __init__(self, var_names, objective, constraints):
		self.names = var_names
		self.objective = objective
		self.constraints = constraints
		self.is_standard = False
		self.basis = None

	def standardize(self, basis):
		# basis must be set here, arg for now but should be automatic
		self.is_standard = True
		self.basis = basis

	def make_tableau(self):
		""" Assumes in standard form: max, all equalities."""
		# Add validation if basis is valid
		return SimplexTableau(self.names, self.objective[1], [con[1] for con in self.constraints], self.basis)