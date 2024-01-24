--> we use string "=" 
#!/bin/bash
 
a="CloudBuilders"
 
if[ $a = "CloudBuilders" ]
then
    echo "The name is correct"
else
    echo "Please give the correct name"
fi
 
 --> it is used to take output in the execution
#!/bin/bash
 
echo "Please enter your name"
read name
 
if [ $name = "CloudBuilders" ]
then
    echo "The name is correct"
else
    echo "Please give the correct name"
fi
 
 
--> pass the arguments 
#!/bin/bash
 
NUMBER=$1
 
if [ $NUMBER -gt 10 ]
 
then
    echo "$NUMBER is greater than 10"
 
else
    echo "$NUMBER is not greater than 10"
fi
 
 
#!/bin/bash
 
#echo "Please enter your name"
#read name
name=CloudBuilders
if [ $name = "CloudBuilders" ]
then
    echo "The name is correct"
else
    echo "Please give the correct name"
fi

-->add the numbers giving the arguments
#!/bin/bash
number1=$1
number2=$2
sum =$$((number1+number2))
echo "the sum is $sum"
 

--> for numbers we use "-eq" and elif statement
#!/bin/bash
 
NUMBER=100
 
if [ $NUMBER -eq 10 ]; then

    echo "NUMBER is greater than 10"

elif [ $NUMBER -gt 10 ]; then

    echo "NUMBER is equal to 10"

else

    echo "NUMBER is not greater than 10"

fi


--> file exist or not
#!/bin/bash
if [ -e /home/ubuntu/firstshell/sum.sh ]
then
        echo "file exit"
else
        echo "file is not exist"
fi
