# thanks to http://www.rosettacode.org/wiki/Fast_Fourier_transform#Python
from cmath import exp, pi
 
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

def run_tests(n):
    for i in range(n):
        fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])

def main( ):
    run_tests(10000)

if __name__ == "__main__":
    # execute only if run as a script
    main()


