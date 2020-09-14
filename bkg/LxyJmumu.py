import ROOT,os,glob,math
from array import array
import numpy as np

def perp(p):
    return math.sqrt(p[0]*p[0]+p[1]*p[1])

O1=ROOT.TH1F("Lxy_1_OS","Lxy_1_OS",200,-10,10)
S1=ROOT.TH1F("Lxy_1_SS","Lxy_1_SS",200,-10,10)
O2=ROOT.TH1F("Lxy_2_OS","Lxy_2_OS",200,-10,10)
S2=ROOT.TH1F("Lxy_2_SS","Lxy_2_SS",200,-10,10)

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
    p1=[t.jpsi_px[0],t.jpsi_py[0]]
    p2=[sum(t.mu_px)-t.jpsi_px[0],sum(t.mu_py)-t.jpsi_py[0]]
    if sorted(t.mu_charge)==[-1,-1,1,1] :
        #lxy1=math.sqrt(t.jpsi_decay_x[0]**2+t.jpsi_decay_y[0]**2)
        x2=(sum(t.mu_prod_x)-2*t.jpsi_decay_x[0])/2.0
        y2=(sum(t.mu_prod_y)-2*t.jpsi_decay_y[0])/2.0
        #lxy2=math.sqrt(x2**2+y2**2)
        lxy1=(t.jpsi_decay_x[0]*p1[0]+t.jpsi_decay_y[0]*p1[1])/perp(p1)
        lxy2=(x2*p2[0]+y2*p2[1])/perp(p2)
        O1.Fill(lxy1)
        O2.Fill(lxy2)
    else :
        #lxy1=math.sqrt(t.jpsi_decay_x[0]**2+t.jpsi_decay_y[0]**2)
        x2=(sum(t.mu_prod_x)-2*t.jpsi_decay_x[0])/2.0
        y2=(sum(t.mu_prod_y)-2*t.jpsi_decay_y[0])/2.0
        #lxy2=math.sqrt(x2**2+y2**2)
        lxy1=(t.jpsi_decay_x[0]*p1[0]+t.jpsi_decay_y[0]*p1[1])/perp(p1)            
        lxy2=(x2*p2[0]+y2*p2[1])/perp(p2)
        S1.Fill(lxy1)
        S2.Fill(lxy2)

rebin=2
O1.Rebin(rebin)
O2.Rebin(rebin)
S1.Rebin(rebin)
S2.Rebin(rebin)
O1.Scale(1/O1.Integral())
O2.Scale(1/O2.Integral())
S1.Scale(1/S1.Integral())
S2.Scale(1/S2.Integral())
O1.GetXaxis().SetRangeUser(-8,8)
O1.GetYaxis().SetRangeUser(0,0.2)
O1.SetNameTitle("",key)
O1.GetXaxis().SetTitle("L_{xy}")
O1.GetYaxis().SetTitle("Evnets Frac.")
O1.SetLineColor(2)
O2.SetLineColor(1)
S1.SetLineColor(3)
S2.SetLineColor(4)

c1=ROOT.TCanvas("c1","c1",100,0,900,700)
#c1.SetLogy()
ROOT.gStyle.SetOptStat(0)
O1.Draw("hist e")
O2.Draw("same hist e")
S1.Draw("same hist e")
S2.Draw("same hist e")
t=ROOT.TLegend(0.7,0.6,0.9,0.8)
t.AddEntry(O1,"OS J/#psi","l")
t.AddEntry(O2,"OS m_{#mu_{3}#mu_{4}}","lp")
t.AddEntry(S1,"SS J/#psi","lp")
t.AddEntry(S2,"SS m_{#mu_{3}#mu_{4}}","lp")
t.SetBorderSize(0)
t.SetTextSize(0.04)
t.Draw()
c1.Draw()
name="./figures/Lxy_"+key
c1.SaveAs(name+".pdf")
c1.SaveAs(name+".jpg")

