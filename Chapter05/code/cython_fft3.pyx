from cmath import exp, pi
    def fft_cython(x):
        cdef int N, k
        N = len(x)
        if N <= 1:
            return x
        even = fft_cython(x[0::2])
        odd = fft_cython(x[1::2])
        T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
        return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]
    def run_cython_tests(n):
        for i in range(n):
            fft_cython([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])