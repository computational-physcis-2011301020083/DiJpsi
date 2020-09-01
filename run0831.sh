path1="DPSMerge"
path2="bbJJMerge"
path3="BmumuMerge"
path4="JmumuMerge"

for i in 0 1 #2 
do 
echo $i
#:<<!

#DPS
#python readbbJJ.py --path $i --path1 $path1
python angle.py --path $i --path1 $path1
python kinematic.py --path $i --path1 $path1

#bbJJ 
#python readbbJJ.py --path $i --path1 $path2
python angle.py --path $i --path1 $path2
python kinematic.py --path $i --path1 $path2
#!

#Bmumu
#python readBmumu.py --path $i --path1 $path3
python angleBmumu.py --path $i --path1 $path3
python kinematicBmumu.py --path $i --path1 $path3
#!
#:<<!
#Jmumu
#python readJmumu.py --path $i --path1 $path4
python angleJmumu.py --path $i --path1 $path4
python kinematicJmumu.py --path $i --path1 $path4
#!

done



