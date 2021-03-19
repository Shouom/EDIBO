echo "Turpināt? y/n" >>
y=1
yes=1
n=0
no=0
read YesNo
YesNo=
while [ $YesNo -eq 1 ]
do
echo "Ievadi temperatūru:"
read temperature
echo $temperature >> temperature.log
echo "Turpināt? y/n"
read YesNo
echo $YesNo >> temperature.log
done