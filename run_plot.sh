for i in bbJJ Bmumu Jmumu DPS
do
echo $i
for j in $(seq 0 12) 
do
echo $j
python plot_km.py --path $i --path1 $j	
#python plot_angle.py --path $i --path1 $j
done
done
