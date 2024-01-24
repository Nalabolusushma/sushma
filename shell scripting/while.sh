#!/bin/bash
while true
do
        echo "my nameis sushma"
done

-->
#!/bin/bash
while [[ $answer != "yes" ]]
do
read -p "please enter your name" answer
done

-->
#!/bin/bash
i=1
while [[ $i -lt 10 ]]
do
        echo $((i))
        ((i++))
done

-->
#!/bin/bash
read -p "enter yor number" number
i=1
while [[ $i -lt 10 ]]
do
        echo $((i*number))
        ((i++))
done
#!/bin/bash
 
count=0
num=10
 
while [ $count -lt 10 ]
do
  echo "$num to stop this process $1"
  sleep 1
  echo
  num=`expr $num - 1`
count=`expr $count + 1`
done
sleep 5
echo "$1 is stopped"
echo


