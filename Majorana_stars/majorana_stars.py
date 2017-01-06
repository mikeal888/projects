#!/usr/bin/python3.5

# Create Majorana stars objects for any dimensional state
# The Majorana stars for a spin system can be found by converting the linear algebra into a complex polynomial. The roots of this complex polynomial yield the coordinates of each Majorana star on the Bloch sphere.  
# z = tan(theta/2)exp(phi) where theta and phi correspond to the polar and azimuthal angles of the Bloch sphere respectively. 

import numpy as np
from math import factorial
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


# Define binomial coeffs. Numpy and scipy don't have it any more.
def binom(n,k):		
	return(factorial(n)/(factorial(k)*factorial(n-k)))

class stars:

	def __init__(self, state):
		self.state = state/np.linalg.norm(state)	# Normalised state
		assert (type(self.state).__module__ == np.__name__), "Class requires numpy array"
		assert (self.state.ndim == 1), "State must be 1D vector"

	# Print dimension of state	
	def dimension(self):
		return(np.shape(self.state)[0])

	# Find complex roots of majorana polynomial defining each star
	def complex_roots(self):
		coeffs = []
		for i in range(self.dimension()):
			# Obtain complex coefficients
			coeffs.append(self.state[i]*(binom(self.dimension()-1,i))**0.5)

		# Find roots of complex polynomial
		roots = np.roots(coeffs)
		return(roots)

	# Get azimuthal coordinates of stars on Bloch sphere
	def azimuthal(self):
		return(np.angle(self.complex_roots()))

	# Get polar coordinates of stars on Bloch sphere
	def polar(self):
		return(2*np.arctan(np.abs(self.complex_roots())))

	# Get the spherical coordinates of each majorana star
	def coordinates(self):
		coorlist = []
		for index, (phi, theta) in enumerate(zip(self.azimuthal(), self.polar())):
			coor = np.array([np.cos(phi)*np.sin(theta),np.sin(phi)*np.sin(theta),np.cos(theta)])

			coorlist.append(coor)

		return(coorlist)

# Matplot lib does not have 3d arrows make arrow class
# This 3d arrow object stars from the origin

class Arrow3D(FancyArrowPatch):
    def __init__(self, coors, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = [0, coors[0]], [0,coors[1]], [0,coors[2]]

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


def stars_plot(vector):
	
	# Create Majorana stars plot
	assert (vector.__class__.__name__ == 'stars'), "Input must be 'stars' object"
	
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(111, projection='3d') 
	axes = plt.gca()

	# Set axis limit
	ax.set_xlim([-1,1])
	ax.set_ylim([-1,1])
	ax.set_zlim([-1,1])

	# Axes labels
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	# Plot stars
	star1 = Arrow3D(vector.coordinates()[0], mutation_scale=20, lw=3, arrowstyle='-|>',color='r')
	star2 = Arrow3D(vector.coordinates()[1], mutation_scale=20, lw=3, arrowstyle='-|>',color='r')

	# Make sphere
	u = np.linspace(0, 2 * np.pi, 100)
	v = np.linspace(0, np.pi, 100)
	x = 1 * np.outer(np.cos(u), np.sin(v))
	y = 1 * np.outer(np.sin(u), np.sin(v))
	z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
	ax.plot_surface(x, y, z, rstride =5,
	    cstride = 5, color ='gray', alpha=0.1)

	ax.add_artist(star1)
	ax.add_artist(star2)
	plt.draw()
	plt.show()


if __name__ == '__main__':
	
	y = stars((1,1,1+1j))

	stars_plot(y)
