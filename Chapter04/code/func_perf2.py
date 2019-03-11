def foo(x):
    pass

def run_tests(n):
    for i in range(n):
        foo(i)

def main( ):
    run_tests(100000)

if __name__ == "__main__":
    main( )
