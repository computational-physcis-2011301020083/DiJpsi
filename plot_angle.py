import ROOT,os,glob,math
import argparse
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
parser.add_argument("--path1", dest='path1',  default="", help="path1")
args = parser.parse_args()

pi=ROOT.TMath.Pi()
keypath=args.path
count=int(args.path1)
print(keypath)

path="./"+keypath+"Merge/"
paths=glob.glob(path+"*angle*root")
print(path,paths)
f1=ROOT.TFile(paths[0],"r")
f2=ROOT.TFile(paths[1],"r")
#Legend
if keypath=="bbJJ":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>5,pTHatMin=7"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>5,pTHatMin=7"
if keypath=="Bmumu":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>6,pTHatMin=8"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>6,pTHatMin=8"
if keypath=="Jmumu":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>6,pTHatMin=8"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>6,pTHatMin=8"
if keypath=="DPS":
    if "cut0" in paths[0]:
        cut1="pt(b/bbar)>0,pTHatMin=0"
        cut2="pt(b/bbar)>3.5,pTHatMin=3.5"
    else:
        cut2="pt(b/bbar)>0,pTHatMin=0"
        cut1="pt(b/bbar)>3.5,pTHatMin=3.5"
anglelist=[]
for i in f1.GetListOfKeys():
    #print(i.GetName())
    anglelist.append(i.GetName())
print(cut1,cut2,anglelist)
hist=anglelist[count]
print(hist)
h1=f1.Get(hist)
h2=f2.Get(hist)
rebin=4
h1.Rebin(rebin)
h2.Rebin(rebin)
h1.Scale(1/h1.Integral())
h2.Scale(1/h2.Integral())
h1.GetXaxis().SetRangeUser(0,pi)
h1.SetNameTitle("",keypath)
if count==0:
    h1.GetXaxis().SetTitle("#theta_{x}")
if count==1:
    h1.GetXaxis().SetTitle("#phi_{#mu1}")
if count==2:
    h1.GetXaxis().SetTitle("#phi_{#mu2}")
if count==3:
    h1.GetXaxis().SetTitle("#theta_{#phi1}")
if count==4:
    h1.GetXaxis().SetTitle("#theta_{#phi2}")
h1.GetYaxis().SetTitle("Evnets Frac.")
h1.SetLineColor(1)
h2.SetLineColor(2)
c1=ROOT.TCanvas("c1","c1",100,0,900,700)
c1.SetLeftMargin(0.12)
#c1.SetLogy()
ROOT.gStyle.SetOptStat(0)
h1.Draw("hist e")
h2.Draw("same hist e")
#t=ROOT.TLegend(0.7,0.75,0.9,0.85)
t=ROOT.TLegend(0.35,0.15,0.45,0.25)
t.AddEntry(h1,cut1,"l")
t.AddEntry(h2,cut2,"lp")
t.SetBorderSize(0)
t.SetTextSize(0.03)
t.Draw()
c1.Draw()
name=keypath+"_"+hist
print(name)
c1.SaveAs("figures0901/"+name+".jpg")
c1.SaveAs("figures0901/"+name+".pdf")


