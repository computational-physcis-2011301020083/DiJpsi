import ROOT,os,glob,math
import argparse
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
parser.add_argument("--path1", dest='path1',  default="", help="path1")
args = parser.parse_args()

key=args.path
pi=ROOT.TMath.Pi()
path="./"+key+"Merge/"
paths=glob.glob(path+key+"*km*root")
f1=ROOT.TFile(paths[0],"r")
f2=ROOT.TFile(paths[1],"r")
#Legend
if key=="DPS":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>3.5,pTHatMin=3.5"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>3.5,pTHatMin=3.5"
if key=="bbJJ":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>5,pTHatMin=7"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>5,pTHatMin=7"
if key=="Bmumu":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>6,pTHatMin=8"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>6,pTHatMin=8"
if key=="Jmumu":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>6,pTHatMin=8"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>6,pTHatMin=8"
anglelist=[]
for i in f1.GetListOfKeys():
    anglelist.append(i.GetName())
#print(cut1,cut2,anglelist,len(anglelist))
count=int(args.path1)
hist=anglelist[count]
#print(hist)
h1=f1.Get(hist)
h2=f2.Get(hist)

if hist=="x_mass":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,16)
    h1.GetXaxis().SetTitle("m_{#mu^{+}#mu^{-}#mu^{+}#mu^{-}}[GeV]")
    t=ROOT.TLegend(0.4,0.7,0.5,0.8)
if hist=="muon_1_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,30)
    h1.GetXaxis().SetTitle("1st #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_2_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,20)
    h1.GetXaxis().SetTitle("2nd #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_3_pt":
    rebin=2
    h1.GetXaxis().SetRangeUser(0,15)
    h1.GetXaxis().SetTitle("3rd #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_4_pt":
    rebin=1
    h1.GetXaxis().SetRangeUser(0,10)
    h1.GetXaxis().SetTitle("4st #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="jpsi_1_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,60)
    h1.GetXaxis().SetTitle("1st J/#psi p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="jpsi_2_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,40)
    h1.GetXaxis().SetTitle("2nd J/#psi p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_1_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("1st #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="muon_2_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("2nd #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="muon_3_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("3rd #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="muon_4_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("4st #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="jpsi_1_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("1st J/#psi #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="jpsi_2_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("2nd J/#psi #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
    
h1.Rebin(rebin)
h2.Rebin(rebin)
h1.Scale(1/h1.Integral())
h2.Scale(1/h2.Integral())
h1.SetNameTitle("",key)

if hist=="x_mass":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,16)
    h1.GetXaxis().SetTitle("m_{#mu^{+}#mu^{-}#mu^{+}#mu^{-}}[GeV]")
    t=ROOT.TLegend(0.4,0.7,0.5,0.8)
if hist=="muon_1_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,30)
    h1.GetXaxis().SetTitle("1st #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_2_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,20)
    h1.GetXaxis().SetTitle("2nd #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_3_pt":
    rebin=2
    h1.GetXaxis().SetRangeUser(0,15)
    h1.GetXaxis().SetTitle("3rd #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_4_pt":
    rebin=1
    h1.GetXaxis().SetRangeUser(0,10)
    h1.GetXaxis().SetTitle("4st #mu p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="jpsi_1_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,60)
    h1.GetXaxis().SetTitle("1st J/#psi p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="jpsi_2_pt":
    rebin=3
    h1.GetXaxis().SetRangeUser(0,40)
    h1.GetXaxis().SetTitle("2nd J/#psi p_{T}[GeV]")
    t=ROOT.TLegend(0.5,0.75,0.6,0.85)
if hist=="muon_1_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("1st #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="muon_2_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("2nd #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="muon_3_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("3rd #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="muon_4_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("4st #mu #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="jpsi_1_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("1st J/#psi #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)
if hist=="jpsi_2_eta":
    rebin=3
    h1.GetXaxis().SetRangeUser(-pi,pi)
    h1.GetXaxis().SetTitle("2nd J/#psi #eta")
    t=ROOT.TLegend(0.35,0.15,0.45,0.25)

h1.GetYaxis().SetTitle("Evnets Frac.")
h1.SetLineColor(2)
h2.SetLineColor(1)
c1=ROOT.TCanvas("c1","c1",100,0,900,700)
c1.SetLeftMargin(0.12)
ROOT.gStyle.SetOptStat(0)
h1.Draw("hist e")
h2.Draw("same hist e")
t.AddEntry(h1,cut1,"l")
t.AddEntry(h2,cut2,"lp")
t.SetBorderSize(0)
t.SetTextSize(0.03)
t.Draw()
c1.Draw()
name=key+"_"+hist
c1.SaveAs("figures0901/"+name+".jpg")
c1.SaveAs("figures0901/"+name+".pdf")














