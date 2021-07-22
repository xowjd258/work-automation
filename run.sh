maxidx=49
iter=0

while [ $iter -lt $maxidx ]
do
python3 start_mail.py
python3 b_auto_fix.py
STARTTIME=$(date +%s)
make
./darknet classifier valid cfg/imagenet50k.data cfg/resnet50.cfg weight/resnet50.weights > result_$iter
ENDTIME=$(date +%s)
echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..." > result_time_$iter
python3 mail.py
iter=$(expr $iter + 1)
done
