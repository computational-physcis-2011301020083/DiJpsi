for i in $(seq 0 2)
do
echo $i
#python triggerROOT.py --path $i
python angleHist.py --path $i
done
