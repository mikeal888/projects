#!/usr/bin/python3.5

# Create majorana stars objects

import numpy as np
from math import factorial

def binom(n,k):		# Define binomial coeffs. Numpy and scipy don't have it any more.
	return(factorial(n)/(factorial(k)*factorial(n-k)))

class stars:

	def __init__(self, state):
		self.state = state/np.linalg.norm(state)	# Normalised state
		assert (type(self.state).__module__ == np.__name__), "Class requires numpy array"
		assert (self.state.ndim == 1), "State must be 1D vector"

	def dimension(self):	# print dimension of state
		return(np.shape(self.state)[0])

	def complex_roots(self):
		for i in range(self.dimension())