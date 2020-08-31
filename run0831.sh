#path1="bbJJMerge"
path1="BmumuMerge"
for i in 0 1 #2 
do 
echo $i
:<<!
python readbbJJ.py --path $i --path1 $path1
python angle.py --path $i --path1 $path1
python kinematic.py --path $i --path1 $path1
!

python readBmumu.py --path $i --path1 $path1
python angleBmumu.py --path $i --path1 $path1
python kinematicBmumu.py --path $i --path1 $path1

done



