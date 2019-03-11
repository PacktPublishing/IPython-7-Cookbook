from io import StringIO
import random
import string

def concat1(lst, num_times):
    for i in range(num_times):
        ret = ""
        for w in lst:
            ret = ret + w
    return ret

def concat2(lst, num_times):
    for i in range(num_times):
        ret = ""
        for w in lst:
            ret += w
    return ret

def concat3(lst, num_times):
    for i in range(num_times):
        ret = "".join(lst)
    return ret

def concat4(lst, num_times):
    for i in range(num_times):
        ret = StringIO( )
        for w in lst:
            ret.write(w)
    return ret

def run_tests(num_times):
    tst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1000))
    lst_tst = list(tst)
    concat1(lst_tst, num_times)
    concat2(lst_tst, num_times)
    concat3(lst_tst, num_times)
    concat4(lst_tst, num_times)

def main( ):
    run_tests(100)


if __name__ == "__main__":
    main( )
