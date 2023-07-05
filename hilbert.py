import numpy as np
from itertools import zip_longest, starmap
import operator



class Hilbert:
    """An infinite dimensional vector class."""
    
    def __init__(self, coef):
        """Creates a new vector with the given coefficients
                or a basis vector when an integer index is given."""
        if isinstance(coef, int):
            self.coef = Hilbert.basis_tuple(coef)
        else:
            self.coef = tuple(c for c in coef)
    
    @staticmethod
    def basis_tuple(i, n=0):
        """Returns the i-th basis vector as a tuple in n dimensional space
                (or i dimensional if left to 0)."""
        return i*(0,) + (1,) + (n-i-1)*(0,)
    
    @staticmethod
    def random(n, normed=True):
        """Returns an, if not turned of, n dimensional random vector
                where the coefficients are drawn from a normal distribution."""
        coef = np.random.normal(size=n)
        if normed:
            coef /= np.linalg.norm(coef)
        return Hilbert(coef)
    
    
    
    #sequence/container stuff
    def __len__(self):
        return len(self.coef)
    
    def __getitem__(self, key):
        try:
            return self.coef[key]
        except IndexError:
            return 0
    
    def __iter__(self):
        return iter(self.coef)
    
    def __eq__(self, other):
        return self.coef == other.coef
    
    
    def __lshift__(self, other):
        return Hilbert(self[1:])
    
    def __rshift__(self, other):
        return Hilbert((0,) + self.coef)
    
    
    
    #Banach space & Hilbert space stuff
    def __abs__(self):
        return np.linalg.norm(self)
    
    def __matmul__(self, other):
        #https://docs.python.org/3/library/itertools.html
        return sum(starmap(operator.mul, zip(self, other)))
    
    
    
    #Vector space operations
    @staticmethod
    def map_zip(f, v, w):
        """Applies f(v, w) elementwise if possible,
                otherwise elementwise in the first argument."""
        try: #second argument iterable
            return Hilbert(f(a, b) for a, b in zip(v, w))
        except TypeError: #second argument scalar
            return Hilbert(f(c, w) for c in v)
    
    @staticmethod
    def map_zip_longest(f, v, w):
        """Applies f(v, w) elementwise if possible,
                otherwise elementwise in the first argument."""
        try: #second argument iterable
            return Hilbert(f(a, b) for a, b in zip_longest(v, w, fillvalue=0))
        except TypeError: #second argument scalar
            return Hilbert(f(c, w) for c in v)
    
    #implement vector space operations like they would be correct on paper:
    #v+w, v-w, av, va, v/a
    def __add__(self, other):
        return Hilbert.map_zip_longest(operator.add, self, other)
    
    def __sub__(self, other):
        return Hilbert.map_zip_longest(operator.sub, self, other)
    
    def __mul__(self, other):
        return Hilbert.map_zip(operator.mul, self, other)
    __rmul__ = __mul__
    
    def __truediv__(self, other):
        return Hilbert.map_zip(operator.truediv, self, other)
    
    
    
    def __str__(self):
        return str(self.coef)
