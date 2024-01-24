#!/bin/bash
ping -c3 8.8.8.8
if [ $? -eq 0 ]
then
        echo ok
else
        echo not ok
fi
--->
#!/bin/bash
host=8.8.8.8
ping -c3 $host
if [ $? -eq 0 ]
then
        echo $host is ok
else
        echo $host is not ok
fi
