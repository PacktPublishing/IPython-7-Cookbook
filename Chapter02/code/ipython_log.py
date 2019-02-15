# IPython log file

get_ipython().run_line_magic('run', 'ipython_log.py')
get_ipython().run_line_magic('logon', '')
get_ipython().run_line_magic('logstart', '')
x = 5
get_ipython().run_line_magic('logoff', '')
x = 7
get_ipython().run_line_magic('magic', '')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', 'IPythonCookbook/chap2')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('run', 'qsort2.py')
get_ipython().run_line_magic('run', '-t qsort2.py')
get_ipython().run_line_magic('debug', 'qsort2.py')
get_ipython().run_line_magic('prun', 'qsort2.py')
get_ipython().run_line_magic('pycat', 'qsort2.py')
get_ipython().run_line_magic('pinfo', 'quicksort')
get_ipython().run_line_magic('load', 'qsort2.py')
# %load qsort2.py
import numpy as np

# thanks to https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def main( ):
    a = np.random.randint(0, 300, 17)
    print(a)
    print(quickSort(a))

if __name__ == "__main__":
    main( )
get_ipython().run_line_magic('pinfo', 'quickSort')
get_ipython().run_line_magic('pinfo', 'quickSort')
get_ipython().run_line_magic('lsmagic', '')
get_ipython().run_line_magic('system', 'time')
get_ipython().run_line_magic('system', 'date')
get_ipython().run_line_magic('who', '')
get_ipython().run_cell_magic('html', '', '<h1>hello world!</h1>\n\n')
get_ipython().run_cell_magic('perl', '', 'use strict;\nuse warnings;\n\nprint "Hello world\\n";\n\n')
get_ipython().run_cell_magic('perl', '', 'use strict;\nuse warnings;\n\nprint "Hello world\\n";\n\n')
get_ipython().run_cell_magic('ruby', '', 'def merge_sort(m)\n  return m if m.length <= 1\n \n  middle = m.length / 2\n  left = merge_sort(m[0...middle])\n  right = merge_sort(m[middle..-1])\n  merge(left, right)\nend\n \ndef merge(left, right)\n  result = []\n  until left.empty? || right.empty?\n    result << (left.first<=right.first ? left.shift : right.shift)\n  end\n  result + left + right\nend\n \nary = [7,6,5,9,8,4,3,1,2,0]\np merge_sort(ary)\n\n')
get_ipython().run_cell_magic('bash', '', 'echo "hello world"\n\n')
get_ipython().run_cell_magic('bash', '', 'echo "Enter your name: "\nread nm\necho "Hello " $nm\n\n')
Tom
get_ipython().run_cell_magic('bash', '', 'arr = (10 8 20 100 12) \n  \nfor ((i = 0; i<5; i++)) \ndo\n      \n    for((j = i; j<5; j++)) \n    do\n      \n        if ((${arr[i]} > ${arr[$((j))]})) \n        then\n            temp = ${arr[$j]} \n            arr[$j] = ${arr[$((i))]}   \n            arr[$((i))] = $temp \n        fi\n    done\ndone\n\necho ${arr[*]} \n\n')
get_ipython().run_cell_magic('bash', '', 'arr = (10 8 20 100 12) \n  \necho "Array in original order"\necho ${arr[*]} \n  \n# Performing Bubble sort  \nfor ((i = 0; i<5; i++)) \ndo\n      \n    for((j = i; j<5-i-1; j++)) \n    do\n      \n        if ((${arr[j]} > ${arr[$((j+1))]})) \n        then\n            # swap \n            temp = ${arr[$j]} \n            arr[$j] = ${arr[$((j+1))]}   \n            arr[$((j+1))] = $temp \n        fi\n    done\ndone\n  \necho "Array in sorted order :"\necho ${arr[*]} \n\n')
get_ipython().run_cell_magic('bash', '', 'arr = (10 8 20 100 12)\n\n')
get_ipython().run_cell_magic('bash', '', 'DECLARE -a arr\n\n')
get_ipython().run_cell_magic('bash', '', 'declare -a arr\n\n')
get_ipython().run_cell_magic('bash', '', 'declare -a arr\narr = (10 8 20 100 12) \n  \nfor ((i = 0; i<5; i++)) \ndo\n      \n    for((j = i; j<5; j++)) \n    do\n      \n        if ((${arr[i]} > ${arr[$((j))]})) \n        then\n            temp = ${arr[$j]} \n            arr[$j] = ${arr[$((i))]}   \n            arr[$((i))] = $temp \n        fi\n    done\ndone\n\necho ${arr[*]} \n\n')
get_ipython().run_cell_magic('bash', '', 'declare -a arr\na = (1 2 3)\n\n')
get_ipython().run_cell_magic('bash', '', 'declare -a arr\na = [1 2 3]\n\n\n')
get_ipython().run_cell_magic('bash', '', 'arrp0] = 1\n\n')
get_ipython().run_cell_magic('bash', '', 'arr[0] = 1\n\n\n')
get_ipython().run_cell_magic('bash', '', '#!bin/bash\narr = (0 1 3)\n\n')
get_ipython().run_cell_magic('bash', '', 'declare -a arr\narr=(10 8 20 100 12) \n  \nfor ((i=0; i<5; i++)) \ndo\n      \n    for((j=i; j<5; j++)) \n    do\n      \n        if ((${arr[i]} > ${arr[$((j))]})) \n        then\n            temp=${arr[$j]} \n            arr[$j]=${arr[$((i))]}   \n            arr[$((i))]=$temp \n        fi\n    done\ndone\n\necho ${arr[*]} \n\n')
get_ipython().run_cell_magic('script', 'java /users/PWIT0407/wit0096/Sudoku1bak/Sudoku1/src/main/Main.java', '\n')
get_ipython().run_cell_magic('bash', '', 'echo "Enter your name: "\nread nm\necho "Hello " $nm\n\nTom\n\n')
get_ipython().run_cell_magic('bash', '', 'echo "Enter your name: "\nread nm\necho "Hello " $nm\n\n')
Tom
get_ipython().run_cell_magic('script', 'tcsh', "set arr = (3 82 12 44 7 12 33 2)\n \n@ spot = 1\n \n# size of the array\n@ sz = $#arr\n \n@ swapped = 1\n \nwhile( $swapped )\n    @ swapped = 0\n    foreach i($arr)\n        # check whether we're at the last index or not\n        if($spot == $sz) then\n            @ spot = 1\n            continue\n        endif\n \n        @ next_spot = $spot + 1\n        set a = $arr[$spot]\n        set b = $arr[$next_spot]\n         \n        if($a < $b) then\n            # swap it\n            set temp = $arr[$next_spot]\n            @ arr[$next_spot] = $arr[$spot]\n            @ arr[$spot] = $temp\n            @ swapped = 1\n        endif\n        @ spot = $spot + 1\n    end\nend\n \necho $arr\n\n")
get_ipython().run_cell_magic('script', 'tcsh', "set arr = (3 82 12 44 7 12 33 2)\n \n@ spot = 1\n \n# size of the array\n@ sz = $#arr\n \n@ swapped = 1\n \nwhile( $swapped )\n    @ swapped = 0\n    foreach i($arr)\n        # check whether we're at the last index or not\n        if($spot == $sz) then\n            @ spot = 1\n            continue\n        endif\n \n        @ next_spot = $spot + 1\n        set a = $arr[$spot]\n        set b = $arr[$next_spot]\n         \n        if($a < $b) then\n            # swap it\n            set temp = $arr[$next_spot]\n            @ arr[$next_spot] = $arr[$spot]\n            @ arr[$spot] = $temp\n            @ swapped = 1\n        endif\n        @ spot = $spot + 1\n    end\nend\n \necho $arr\n\n")
get_ipython().run_cell_magic('script', 'tcsh', 'set arr = (3 82 12 44 7 12 33 2)\n \n@ spot = 1\n@ sz = $#arr\n@ swapped = 1\n \nwhile( $swapped )\n    @ swapped = 0\n    foreach i($arr)\n        if($spot == $sz) then\n            @ spot = 1\n            continue\n        endif\n \n        @ next_spot = $spot + 1\n        set a = $arr[$spot]\n        set b = $arr[$next_spot]\n         \n        if($a < $b) then\n            set temp = $arr[$next_spot]\n            @ arr[$next_spot] = $arr[$spot]\n            @ arr[$spot] = $temp\n            @ swapped = 1\n        endif\n        @ spot = $spot + 1\n    end\nend\n \necho $arr\n\n')
exit()
