#!/bin/bash
for i in 1 2 3 4
do
        echo "list is $i"
done

or

#!/bin/bash
for i in run jump sit back
do
        echo "list is $i"
done

--->to create a 5 files
#!/bin/bash
for i in {1..5}
do
        touch "list is $i"
done

--->
#!/bin/bash
i=1
for day in mon tue wed thur fri
do
        echo "days are $((i++)) : $day"
done