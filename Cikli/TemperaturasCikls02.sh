echo "Turpināt? yes/y/1 vai no/n/0"
y=1
yes=1
n=0
no=
read YesNoString
YesNoString=1
while [ $YesNoString -eq "yes" -o $YesNoString -eq "y" -o $YesNoString -eq "1"]
do
echo "Ievadi temperatūru:"
read temperature
echo $temperature >> temperature.log
echo "Turpināt? yes/y/1 vai no/n/0"
read YesNoString
echo $YesNoString >> temperature.log
done