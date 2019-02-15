#!/bin/tcsh
set arr = (3 82 12 44 7 12 33 2)
 
@ spot = 1
@ sz = $#arr
@ swapped = 1
 
while( $swapped )
    @ swapped = 0
    foreach i($arr)
        if($spot == $sz) then
            @ spot = 1
            continue
        endif
 
        @ next_spot = $spot + 1
        set a = $arr[$spot]
        set b = $arr[$next_spot]
         
        if($a < $b) then
            set temp = $arr[$next_spot]
            @ arr[$next_spot] = $arr[$spot]
            @ arr[$spot] = $temp
            @ swapped = 1
        endif
        @ spot = $spot + 1
    end
end
 
echo $arr
