import random
import string

def test_append(lst):
    ret_val = []
    for w in lst:
        ret_val.append(w.lower( ))
    return ret_val

def test_map(lst):
    ret_val = map(str.lower, lst)
    return ret_val

def run_tests(n):
    for i in range(n):
        tst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1000))
        lst_tst = list(tst)
        test_append(lst_tst)
        test_map(lst_tst)

def main( ):
    run_tests(100000)

if __name__ == "__main__":
    main( )
