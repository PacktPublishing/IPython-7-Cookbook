# modified from https://rosettacode.org/wiki/Julia_set#Python to remove the code that displayed the set
# we are only interested with the efficiency of the calculations, not the I/O

"""
Solution from:
https://codereview.stackexchange.com/questions/210271/generating-julia-set
"""
from functools import partial
from numbers import Complex
from typing import Callable
 
import numpy as np
 
 
def douady_hubbard_polynomial(z: Complex,
                              c: Complex) -> Complex:
    """
    Monic and centered quadratic complex polynomial
    https://en.wikipedia.org/wiki/Complex_quadratic_polynomial#Map
    """
    return z ** 2 + c
 
 
def julia_set(mapping: Callable[[Complex], Complex],
              *,
              min_coordinate: Complex,
              max_coordinate: Complex,
              width: int,
              height: int,
              iterations_count: int = 256,
              threshold: float = 2.) -> np.ndarray:
    """
    As described in https://en.wikipedia.org/wiki/Julia_set
    :param mapping: function defining Julia set
    :param min_coordinate: bottom-left complex plane coordinate
    :param max_coordinate: upper-right complex plane coordinate
    :param height: pixels in vertical axis
    :param width: pixels in horizontal axis
    :param iterations_count: number of iterations
    :param threshold: if the magnitude of z becomes greater
    than the threshold we assume that it will diverge to infinity
    :return: 2D pixels array of intensities
    """
    im, re = np.ogrid[min_coordinate.imag: max_coordinate.imag: height * 1j,
                      min_coordinate.real: max_coordinate.real: width * 1j]
    z = (re + 1j * im).flatten()
 
    live, = np.indices(z.shape)  # indexes of pixels that have not escaped
    iterations = np.empty_like(z, dtype=int)
 
    for i in range(iterations_count):
        z_live = z[live] = mapping(z[live])
        escaped = abs(z_live) > threshold
        iterations[live[escaped]] = i
        live = live[~escaped]
        if live.size == 0:
            break
    else:
        iterations[live] = iterations_count
 
    return iterations.reshape((height, width))
 
 
def single_julia_calc( ):
    mapping = partial(douady_hubbard_polynomial,
                      c=-0.7 + 0.27015j)  # type: Callable[[Complex], Complex]
 
    image = julia_set(mapping,
                      min_coordinate=-1.5 - 1j,
                      max_coordinate=1.5 + 1j,
                      width=800,
                      height=600)
def run_tests(n):
    for i in range(n):
        single_julia_calc( )

def main( ):
    run_tests(10)

if __name__ == "__main__":
    main( )
