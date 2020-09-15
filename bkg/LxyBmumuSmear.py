import ROOT,os,os,glob,math
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

HX=1
O1=ROOT.TH1F("Lxy_1_OS","Lxy_1_OS",200,-HX,HX)
S1=ROOT.TH1F("Lxy_1_SS","Lxy_1_SS",200,-HX,HX)
O2=ROOT.TH1F("Lxy_2_OS","Lxy_2_OS",200,-HX,HX)
S2=ROOT.TH1F("Lxy_2_SS","Lxy_2_SS",200,-HX,HX)

path="./bkgs/"
paths=glob.glob(path+"*root*")
rootpath="./bkgs/dat_Bmumu.root"
key=rootpath.split("_")[-1].split(".")[0]
outpath="./hists/"+key+".root"
f=ROOT.TFile(rootpath,"r")
t=f.Get("BPHY13")
N=t.GetEntries()
print(N,rootpath)
X1= 0.276673896624
Y1= 0.270142921918
X2= 0.264299778337
Y2= 0.278848186233
grandom=ROOT.TRandom3(19930305)
for i in range(N):
    t.GetEntry(i)
    if t.jpsi_n==0:
        d1=[grandom.Gaus(0,X1),grandom.Gaus(0,Y1)]
        d2=[grandom.Gaus(0,X2),grandom.Gaus(0,Y2)]
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
        lxy1=(d1[0]*P1[0]+d1[1]*P1[1])/perp(P1)
        lxy2=(d2[0]*P2[0]+d2[1]*P2[1])/perp(P2)
        if sorted(t.mu_charge)==[-1,-1,1,1] :
            O1.Fill(lxy1)
            O2.Fill(lxy2)
        else :
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
#O1.GetXaxis().SetRangeUser(-8,8)
#O1.GetYaxis().SetRangeUser(0,0.25)
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
t.AddEntry(O1,"OS m_{#mu_{1}#mu_{2}}","l")
t.AddEntry(O2,"OS m_{#mu_{3}#mu_{4}}","lp")
t.AddEntry(S1,"SS m_{#mu_{1}#mu_{2}}","lp")
t.AddEntry(S2,"SS m_{#mu_{3}#mu_{4}}","lp")
t.SetBorderSize(0)
t.SetTextSize(0.04)
t.Draw()

c1.Draw()
name="./figures/LxySmear_"+key
c1.SaveAs(name+".pdf")
c1.SaveAs(name+".jpg")

