def foo( ):
    pass

def run_tests(n):
    for i in range(n):
        foo( )

def main( ):
    run_tests(100000)

if __name__ == "__main__":
    main( )
