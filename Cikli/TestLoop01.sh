echo "Please define starting number"
read NUMBER01
echo "Please define end number"
read NUMBER02
echo "Please set loop speed"
read LOOPSPEED
CURRENTNUMBER=$NUMBER01
echo "Counting:"
while [ $CURRENTNUMBER -le $NUMBER02 ]
do
echo $CURRENTNUMBER
CURRENTNUMBER=`expr $CURRENTNUMBER + 1`
sleep $LOOPSPEED
done