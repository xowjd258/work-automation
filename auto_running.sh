python3 start_mail.py
STARTTIME=$(date +%s)
make
./darknet classifier valid cfg/imagenet50k.data cfg/resnet50.cfg weight/resnet50.weights > result1
ENDTIME=$(date +%s)
echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..." > result_time1
python3 mail.py
