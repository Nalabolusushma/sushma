#!/bin/bash
a='sushma'
b='suchi'
c='pandu'

echo 'a=sushma'
echo 'b=suchi'
echo 'c=pandu'
echo

read -p "Enter a name: " name

case $name in
    $a)
        echo "You entered sushma."
        ;;
    $b)
        echo "You entered suchi."
        ;;
    $c)
        echo "You entered pandu."
        ;;
    *)
        echo "No matching name."
        ;;
esac

--->

#!/bin/bash
read choices

case $choices in
    a)
        who
        ;;
    b)
        date
        ;;
    c)
        ls
        ;;
    *)
        echo "No matching - bye."
        ;;
esac

