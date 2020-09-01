for i in bbJJ Bmumu Jmumu DPS
do
echo $i
for j in 0 1 2 3 4 
do
python plot_angle.py --path $i --path1 $j
done
done
