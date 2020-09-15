import ROOT,os,os,glob,math,os
from array import array
import numpy as np

hx1=ROOT.TH1F("hx1","hx1",200,-2,2)
hy1=ROOT.TH1F("hy1","hy1",200,-2,2)
hx2=ROOT.TH1F("hx2","hx2",200,-2,2)
hy2=ROOT.TH1F("hy2","hy2",200,-2,2)
path="./bkgs/"
paths=glob.glob(path+"*root*")
rootpath="./bkgs/dat_Jmumu.root"
key=rootpath.split("_")[-1].split(".")[0]
outpath="./hists/"+key+".root"
f=ROOT.TFile(rootpath,"r")
print(paths,rootpath)
t=f.Get("BPHY13")
N=t.GetEntries()
for i in range(N):
  t.GetEntry(i)
  if t.jpsi_n==1:
        hx1.Fill(t.jpsi_decay_x[0])
        hy1.Fill(t.jpsi_decay_y[0])
        hx2.Fill((sum(t.mu_prod_x)-2*t.jpsi_decay_x[0])/2.0)
        hy2.Fill((sum(t.mu_prod_y)-2*t.jpsi_decay_y[0])/2.0)

rebin=1
hx1.Rebin(rebin)
hy1.Rebin(rebin)
hx2.Rebin(rebin)
hy2.Rebin(rebin)
x=0.05
rx1=ROOT.TFitResult()
ry1=ROOT.TFitResult()
rx2=ROOT.TFitResult()
ry2=ROOT.TFitResult()
rx1=hx1.Fit("gaus","s","",-x,x)
ry1=hy1.Fit("gaus","s","",-x,x)
rx2=hx2.Fit("gaus","s","",-x,x)                            
ry2=hy2.Fit("gaus","s","",-x,x)
print("x1,y1",rx1.Parameter(2),ry1.Parameter(2))
print("x2,y2",rx2.Parameter(2),ry2.Parameter(2))













