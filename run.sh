#python3 read.py
for i in 0 1 # 2 3 4  
do
echo $i
#python3 readDPS.py --path $i
#python3 readbbJJ.py --path $i
#python readBmumu.py --path $i
#python angle.py --path $i
#python angleBmumu.py --path $i
#python kinematic.py --path $i
python kinematicBmumu.py --path $i
done




