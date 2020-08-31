import ROOT,glob,math,os
from array import array
import argparse
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
parser.add_argument("--path1", dest='path1',  default="", help="path1")
args = parser.parse_args()


pi=ROOT.TMath.Pi()
path="./"+args.path1+"/"
paths=glob.glob(path+"*data*root")
rootpath=paths[int(args.path)]
outpath=rootpath.replace("data","km")
print(outpath)

hx=ROOT.TH1F("x_mass","x_mass",200,0,20)
hp1=ROOT.TH1F("muon_1_pt","muon_1_pt",200,0,50)
hp2=ROOT.TH1F("muon_2_pt","muon_2_pt",200,0,50)
hp3=ROOT.TH1F("muon_3_pt","muon_3_pt",200,0,50)
hp4=ROOT.TH1F("muon_4_pt","muon_4_pt",200,0,50)
hp5=ROOT.TH1F("jpsi_1_pt","jpsi_1_pt",200,0,80)
hp6=ROOT.TH1F("jpsi_2_pt","jpsi_2_pt",200,0,80)
he1=ROOT.TH1F("muon_1_eta","muon_1_eta",200,-pi,pi)
he2=ROOT.TH1F("muon_2_eta","muon_2_eta",200,-pi,pi)
he3=ROOT.TH1F("muon_3_eta","muon_3_eta",200,-pi,pi)
he4=ROOT.TH1F("muon_4_eta","muon_4_eta",200,-pi,pi)
he5=ROOT.TH1F("jpsi_1_eta","jpsi_1_eta",200,-pi,pi)
he6=ROOT.TH1F("jpsi_2_eta","jpsi_2_eta",200,-pi,pi)

f=ROOT.TFile(rootpath,"r")
t=f.Get("nominal")
N=t.GetEntries()
for i in range(N):
    t.GetEntry(i)
    #Match
    muon_1=ROOT.TLorentzVector()
    muon_2=ROOT.TLorentzVector()
    muon_3=ROOT.TLorentzVector()
    muon_4=ROOT.TLorentzVector()
    jpsi_1=ROOT.TLorentzVector()
    jpsi_2=ROOT.TLorentzVector()
    muon_1.SetPxPyPzE(t.muon_1[0],t.muon_1[1],t.muon_1[2],t.muon_1[3])
    muon_2.SetPxPyPzE(t.muon_2[0],t.muon_2[1],t.muon_2[2],t.muon_2[3])
    muon_3.SetPxPyPzE(t.muon_3[0],t.muon_3[1],t.muon_3[2],t.muon_3[3])
    muon_4.SetPxPyPzE(t.muon_4[0],t.muon_4[1],t.muon_4[2],t.muon_4[3])
    jpsi_1.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
    jpsi_2.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
    
    muon_1_pt_eta=[muon_1.Pt()/1000.0,muon_1.Eta()]
    muon_2_pt_eta=[muon_2.Pt()/1000.0,muon_2.Eta()]
    muon_3_pt_eta=[muon_3.Pt()/1000.0,muon_3.Eta()]
    muon_4_pt_eta=[muon_4.Pt()/1000.0,muon_4.Eta()]
    jpsi_1_pt_eta=[jpsi_1.Pt()/1000.0,jpsi_1.Eta()]
    jpsi_2_pt_eta=[jpsi_2.Pt()/1000.0,jpsi_2.Eta()]
    muon_list=[muon_1_pt_eta,muon_2_pt_eta,muon_3_pt_eta,muon_4_pt_eta]
    muon_list=sorted(muon_list)
    muon_1_pt=muon_list[3][0]
    muon_2_pt=muon_list[2][0]
    muon_3_pt=muon_list[1][0]
    muon_4_pt=muon_list[0][0]
    muon_1_eta=muon_list[3][1]
    muon_2_eta=muon_list[2][1]
    muon_3_eta=muon_list[1][1]
    muon_4_eta=muon_list[0][1]
    jpsi_list=[jpsi_1_pt_eta,jpsi_2_pt_eta]
    jpsi_list=sorted(jpsi_list)
    jpsi_1_pt=jpsi_list[1][0]
    jpsi_2_pt=jpsi_list[0][0]
    jpsi_1_eta=jpsi_list[1][1]
    jpsi_2_eta=jpsi_list[0][1]


    x_mass=(jpsi_1+jpsi_2).M()/1000.0

    hp1.Fill(muon_1_pt)
    hp2.Fill(muon_2_pt)
    hp3.Fill(muon_3_pt)
    hp4.Fill(muon_4_pt)
    hp5.Fill(jpsi_1_pt)
    hp6.Fill(jpsi_2_pt)
    he1.Fill(muon_1_eta)
    he2.Fill(muon_2_eta)
    he3.Fill(muon_3_eta)
    he4.Fill(muon_4_eta)
    he5.Fill(jpsi_1_eta)
    he6.Fill(jpsi_2_eta)
    hx.Fill(x_mass)

outFile = ROOT.TFile.Open(outpath,'UPDATE')
outFile.cd()
hx.Write(hx.GetName(),ROOT.TObject.kOverwrite)
hp1.Write(hp1.GetName(),ROOT.TObject.kOverwrite)
hp2.Write(hp2.GetName(),ROOT.TObject.kOverwrite)
hp3.Write(hp3.GetName(),ROOT.TObject.kOverwrite)
hp4.Write(hp4.GetName(),ROOT.TObject.kOverwrite)
hp5.Write(hp5.GetName(),ROOT.TObject.kOverwrite)
hp6.Write(hp6.GetName(),ROOT.TObject.kOverwrite)
he1.Write(he1.GetName(),ROOT.TObject.kOverwrite)
he2.Write(he2.GetName(),ROOT.TObject.kOverwrite)
he3.Write(he3.GetName(),ROOT.TObject.kOverwrite)
he4.Write(he4.GetName(),ROOT.TObject.kOverwrite)
he5.Write(he5.GetName(),ROOT.TObject.kOverwrite)
he6.Write(he6.GetName(),ROOT.TObject.kOverwrite)
outFile.Close()
f.Close()














