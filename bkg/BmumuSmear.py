import ROOT,os,os,glob,math,os
from array import array
import numpy as np

def InvariantMass(muon1,muon2):
    Bmeson=[]
    Bmeson.append(muon1[0]+muon2[0])
    Bmeson.append(muon1[1]+muon2[1])
    Bmeson.append(muon1[2]+muon2[2])
    Bmeson.append(muon1[3]+muon2[3])
    Bmass=math.sqrt(abs(Bmeson[0]**2+Bmeson[1]**2+Bmeson[2]**2-Bmeson[3]**2))
    return Bmass
def perp(p):
    return math.sqrt(p[0]*p[0]+p[1]*p[1])
def Lxy(p,d):
    return (p[0]*d[0]+p[1]*d[1])/perp(p)

hx1=ROOT.TH1F("hx1","hx1",200,-2,2)
hy1=ROOT.TH1F("hy1","hy1",200,-2,2)
hx2=ROOT.TH1F("hx2","hx2",200,-2,2)
hy2=ROOT.TH1F("hy2","hy2",200,-2,2)
path="./bkgs/"
paths=glob.glob(path+"*root*")
rootpath="./bkgs/dat_Bmumu.root"
key=rootpath.split("_")[-1].split(".")[0]
outpath="./hists/"+key+".root"
f=ROOT.TFile(rootpath,"r")
print(paths,rootpath)
t=f.Get("BPHY13")
N=t.GetEntries()
for i in range(N):
    t.GetEntry(i)
    if t.jpsi_n==0 :
        muon_1=[t.mu_px[0],t.mu_px[0],t.mu_px[0],t.mu_e[0]]
        muon_2=[t.mu_px[1],t.mu_px[1],t.mu_px[1],t.mu_e[1]]
        muon_3=[t.mu_px[2],t.mu_px[2],t.mu_px[2],t.mu_e[2]]
        muon_4=[t.mu_px[3],t.mu_px[3],t.mu_px[3],t.mu_e[3]]
        if t.mu_charge[0]==t.mu_charge[1]:
            DeltaMass1=abs(InvariantMass(muon_1,muon_3)-InvariantMass(muon_2,muon_4))
            DeltaMass2=abs(InvariantMass(muon_1,muon_4)-InvariantMass(muon_2,muon_3))
            if DeltaMass1<DeltaMass2:
                P1=[t.mu_px[0]+t.mu_px[2],t.mu_py[0]+t.mu_py[2]]
                D1=[(t.mu_prod_x[0]+t.mu_prod_x[2])/2.0,(t.mu_prod_y[0]+t.mu_prod_y[2])/2.0]
                P2=[t.mu_px[1]+t.mu_px[3],t.mu_py[1]+t.mu_py[3]]
                D2=[(t.mu_prod_x[1]+t.mu_prod_x[3])/2.0,(t.mu_prod_y[1]+t.mu_prod_y[3])/2.0]
            else:
                P1=[t.mu_px[0]+t.mu_px[3],t.mu_py[0]+t.mu_py[3]]
                D1=[(t.mu_prod_x[0]+t.mu_prod_x[3])/2.0,(t.mu_prod_y[0]+t.mu_prod_y[3])/2.0]
                P2=[t.mu_px[1]+t.mu_px[2],t.mu_py[1]+t.mu_py[2]]
                D2=[(t.mu_prod_x[1]+t.mu_prod_x[2])/2.0,(t.mu_prod_y[1]+t.mu_prod_y[2])/2.0]
        elif t.mu_charge[0]==t.mu_charge[2]:
            DeltaMass1=abs(InvariantMass(muon_1,muon_2)-InvariantMass(muon_3,muon_4))
            DeltaMass2=abs(InvariantMass(muon_1,muon_4)-InvariantMass(muon_3,muon_2))
            if DeltaMass1<DeltaMass2:
                P1=[t.mu_px[0]+t.mu_px[1],t.mu_py[0]+t.mu_py[1]]
                D1=[(t.mu_prod_x[0]+t.mu_prod_x[1])/2.0,(t.mu_prod_y[0]+t.mu_prod_y[1])/2.0]
                P2=[t.mu_px[2]+t.mu_px[3],t.mu_py[2]+t.mu_py[3]]
                D2=[(t.mu_prod_x[2]+t.mu_prod_x[3])/2.0,(t.mu_prod_y[2]+t.mu_prod_y[3])/2.0]
            else:
                P1=[t.mu_px[0]+t.mu_px[3],t.mu_py[0]+t.mu_py[3]]
                D1=[(t.mu_prod_x[0]+t.mu_prod_x[3])/2.0,(t.mu_prod_y[0]+t.mu_prod_y[3])/2.0]
                P2=[t.mu_px[1]+t.mu_px[2],t.mu_py[1]+t.mu_py[2]]
                D2=[(t.mu_prod_x[1]+t.mu_prod_x[2])/2.0,(t.mu_prod_y[1]+t.mu_prod_y[2])/2.0]
        else :
            DeltaMass1=abs(InvariantMass(muon_1,muon_2)-InvariantMass(muon_4,muon_3))
            DeltaMass2=abs(InvariantMass(muon_1,muon_3)-InvariantMass(muon_4,muon_2))
            if DeltaMass1<DeltaMass2:  
                P1=[t.mu_px[0]+t.mu_px[1],t.mu_py[0]+t.mu_py[1]]
                D1=[(t.mu_prod_x[0]+t.mu_prod_x[1])/2.0,(t.mu_prod_y[0]+t.mu_prod_y[1])/2.0]
                P2=[t.mu_px[2]+t.mu_px[3],t.mu_py[2]+t.mu_py[3]]
                D2=[(t.mu_prod_x[2]+t.mu_prod_x[3])/2.0,(t.mu_prod_y[2]+t.mu_prod_y[3])/2.0]
            else:
                P1=[t.mu_px[0]+t.mu_px[2],t.mu_py[0]+t.mu_py[2]]
                D1=[(t.mu_prod_x[0]+t.mu_prod_x[2])/2.0,(t.mu_prod_y[0]+t.mu_prod_y[2])/2.0]
                P2=[t.mu_px[1]+t.mu_px[3],t.mu_py[1]+t.mu_py[3]]
                D2=[(t.mu_prod_x[1]+t.mu_prod_x[3])/2.0,(t.mu_prod_y[1]+t.mu_prod_y[3])/2.0]
        hx1.Fill(D1[0])
        hy1.Fill(D1[1])
        hx2.Fill(D2[0])
        hy2.Fill(D2[1])

rebin=2
hx1.Rebin(rebin)
hy1.Rebin(rebin)
hx2.Rebin(rebin)
hy2.Rebin(rebin)
x=0.2
rx1=ROOT.TFitResult()
ry1=ROOT.TFitResult()
rx2=ROOT.TFitResult()
ry2=ROOT.TFitResult()
rx1=hx1.Fit("gaus","s","",-x,x)
ry1=hy1.Fit("gaus","s","",-x,x)
rx2=hx2.Fit("gaus","s","",-x,x)                            
ry2=hy2.Fit("gaus","s","",-x,x)
print "X1=",rx1.Parameter(2)
print "Y1=",ry1.Parameter(2) 
print "X2=",rx2.Parameter(2)  
print "Y2=",ry2.Parameter(2)











