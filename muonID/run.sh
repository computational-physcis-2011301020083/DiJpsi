#python muonIDROOT.py
python angleHistID.py

#:<<!
for j in $(seq 0 4)
do
	echo $j
	python plotID.py --path $j
done
#!

