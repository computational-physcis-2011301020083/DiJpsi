for i in $(seq 0 4)
do
echo $i
python plot_mc16d.py --path $i
python plot_mc16e.py --path $i
for j in $(seq 1 4)
do
python plot_mc16a.py --path $i --path1 $j
done
done
