# Hilbert

An infinite dimensional vector module.
```python
>>> from hilbert import Hilbert
>>> Hilbert.random(3), Hilbert(1)
(-0.43247976992238885, 0.8620100981834762, -0.2643857772982335), (0, 1)
```
The vectors are
- immutable,
- zero indexed &
- infinite dimensional
(set coefficients are saved in an tuple that grows dynamically;
all coefficients outside of that are zero).

## Usage

Vectors can be initialised to specific coefficients given by an iterable,
with an index for a basis vector or created randomly:
```python
>>> u, v, w = Hilbert((1, 2, 3)), Hilbert(1), Hilbert.random(3)
>>> u, v, w
(1, 2, 3), (0, 1), (-0.2542424276430939, 0.02971336799386176, -0.9666839730483834)
```
Their `length` is the length of the underlying coefficient tuple
and should correspond to coefficients that have been set on purpose.
They can be indexed, iterated over and compared:
```python
>>> len(u), u[1], tuple(c for c in u), u==v
(3, 2, (1, 2, 3), False)
```
They can be shifted:
```python
>>> u>>1, u<<1
(0, 1, 2, 3), (2, 3)
```
Norms and dot products are implemented with the built-in functions:
```python
>>> abs(u), u@v
3.7416573867739413, 2
```
Vector space operations, like they would be correct on paper, are implemented:
```python
>>> u+v, u-v, 2*u, u/2
(1, 3, 3), (1, 1, 3), (2, 4, 6), (0.5, 1.0, 1.5)
```

## Decision

- Module name `hilbert`: `vector`, `hyper` & `hypervector`
are already taken on PyPI.

## License (MIT)

MIT License

Copyright (c) 2023 Sebastian Gössl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
