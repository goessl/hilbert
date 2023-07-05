from hilbert import Hilbert
import numpy as np



if __name__ == '__main__':
    v = Hilbert((1, 2, 3, 4, 5))
    
    assert len(v) == 5
    assert v[2] == 3
    assert v[999] == 0
    assert v<<1 == Hilbert((2, 3, 4, 5))
    assert v>>1 == Hilbert((0, 1, 2, 3, 4, 5))
    
    assert np.isclose(abs(v), np.sqrt(55))
    assert v+Hilbert((3, 2, 1)) == Hilbert((4, 4, 4, 4, 5))
    assert v-Hilbert((3, 2, 1)) == Hilbert((-2, 0, 2, 4, 5))
    assert 2*v == v*2 == Hilbert((2, 4, 6, 8, 10))
    assert v/2 == Hilbert((0.5, 1.0, 1.5, 2, 2.5))
