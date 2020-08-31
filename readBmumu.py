import ROOT,glob,math,os
from array import array
import argparse
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
parser.add_argument("--path1", dest='path1',  default="", help="path1")
args = parser.parse_args()

path="./"+args.path1+"/"
paths=glob.glob(path+"*txt")
fpath=paths[int(args.path)]
outpath=path+fpath.split("/")[-2]+"_"+fpath.split("/")[-1].split(".")[0]+".root"
print(outpath)

file1 = ROOT.TFile(outpath, 'recreate')
tree = ROOT.TTree("nominal", "Truth info for Bmumu")
event  = array('f',[0])
charge  = array('f',[0,0,0,0])
muon_1= array('f',[0,0,0,0])
muon_2= array('f',[0,0,0,0])
muon_3= array('f',[0,0,0,0])
muon_4= array('f',[0,0,0,0])
tree.Branch("event",  event,  'event/F')
tree.Branch("charge",  charge,  'charge[4]/F')
tree.Branch("muon_1",  muon_1,  'muon_1[4]/F')
tree.Branch("muon_2", muon_2, 'muon_2[4]/F')
tree.Branch("muon_3",  muon_3,  'muon_3[4]/F')
tree.Branch("muon_4", muon_4, 'muon_4[4]/F')
f=open(fpath,"r")
lines=f.readlines()
L=int(len(lines)/5)
for j in range(L):
        count=j*5
        e=float(lines[count].split(" ")[1])
        m1=[float(k) for k in lines[count+1].split(" ")]
        m2=[float(k) for k in lines[count+2].split(" ")]
        m3=[float(k) for k in lines[count+3].split(" ")]
        m4=[float(k) for k in lines[count+4].split(" ")]
        event[0]=e
        muon_1[0]=m1[0]
        muon_2[0]=m2[0]
        muon_3[0]=m3[0]
        muon_4[0]=m4[0]
        muon_1[1]=m1[1]
        muon_2[1]=m2[1]
        muon_3[1]=m3[1]
        muon_4[1]=m4[1]
        muon_1[2]=m1[2]
        muon_2[2]=m2[2]
        muon_3[2]=m3[2]
        muon_4[2]=m4[2]
        muon_1[3]=m1[3]
        muon_2[3]=m2[3]
        muon_3[3]=m3[3]
        muon_4[3]=m4[3]
        charge[0]=m1[4]
        charge[1]=m2[4]
        charge[2]=m3[4]
        charge[3]=m4[4]
        tree.Fill()
file1.Write()
file1.Close()







