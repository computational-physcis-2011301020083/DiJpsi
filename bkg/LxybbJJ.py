import ROOT,os,glob,math
from array import array
import numpy as np

def perp(p):
    return math.sqrt(p[0]*p[0]+p[1]*p[1])

O1=ROOT.TH1F("Lxy_1_OS","Lxy_1_OS",200,-10,10)
O2=ROOT.TH1F("Lxy_2_OS","Lxy_2_OS",200,-10,10)

path="./bkgs/"
paths=glob.glob(path+"*root*")
rootpath="./bkgs/dat_bbJJ.root"
key=rootpath.split("_")[-1].split(".")[0]
outpath="./hists/"+key+".root"
f=ROOT.TFile(rootpath,"r")
print(paths,rootpath)
t=f.Get("BPHY13")
N=t.GetEntries()
for i in range(N):
  t.GetEntry(i)
  if t.jpsi_n==2 and sorted(t.mu_charge)==[-1,-1,1,1] :
        p1=[t.jpsi_px[0],t.jpsi_py[0]]
        p2=[t.jpsi_px[1],t.jpsi_py[1]]
        #lxy1=math.sqrt(t.jpsi_decay_x[0]**2+t.jpsi_decay_y[0]**2)
        #lxy2=math.sqrt(t.jpsi_decay_x[1]**2+t.jpsi_decay_y[1]**2)
        lxy1=(t.jpsi_decay_x[0]*p1[0]+t.jpsi_decay_y[0]*p1[1])/perp(p1)
        lxy2=(t.jpsi_decay_x[1]*p2[0]+t.jpsi_decay_y[1]*p2[1])/perp(p2)
        O1.Fill(lxy1)
        O2.Fill(lxy2)

rebin=2
O1.Rebin(rebin)
O2.Rebin(rebin)
O1.Scale(1/O1.Integral())
O2.Scale(1/O2.Integral())
O1.GetXaxis().SetRangeUser(-8,8)
O1.GetYaxis().SetRangeUser(0,0.2)
O1.SetNameTitle("",key)
O1.GetXaxis().SetTitle("L_{xy}")
O1.GetYaxis().SetTitle("Evnets Frac.")
O1.SetLineColor(2)
O2.SetLineColor(1)

c1=ROOT.TCanvas("c1","c1",100,0,900,700)
#c1.SetLogy()
ROOT.gStyle.SetOptStat(0)
O1.Draw("hist e")
O2.Draw("same hist e")
t=ROOT.TLegend(0.7,0.6,0.9,0.8)
t.AddEntry(O1,"OS 1st J/#psi","l")
t.AddEntry(O2,"OS 2st J/#psi","lp")
t.SetBorderSize(0)
t.SetTextSize(0.04)
t.Draw()
c1.Draw()
name="./figures/Lxy_"+key
c1.SaveAs(name+".pdf")
c1.SaveAs(name+".jpg")

