import ROOT,glob,math,os
from array import array

h1=ROOT.TH1F("theta_x","theta_x",200,0,4)
h2=ROOT.TH1F("phi_1","phi_1",200,0,4)
h3=ROOT.TH1F("phi_2","phi_2",200,0,4)
h4=ROOT.TH1F("theta_phi_1","theta_phi_1",200,0,4)
h5=ROOT.TH1F("theta_phi_2","theta_phi_2",200,0,4)

i1=ROOT.TH1F("theta_x_a1","theta_x_a1",200,0,4)
i2=ROOT.TH1F("phi_1_a1","phi_1_a1",200,0,4)
i3=ROOT.TH1F("phi_2_a1","phi_2_a1",200,0,4)
i4=ROOT.TH1F("theta_phi_1_a1","theta_phi_1_a1",200,0,4)
i5=ROOT.TH1F("theta_phi_2_a1","theta_phi_2_a1",200,0,4)



outpath="./Reduce/hist.root"

rootpath="./Reduce/sig.root"
f=ROOT.TFile(rootpath,"r")
t=f.Get("nominal")
N=t.GetEntries()
for i in range(N):
    t.GetEntry(i)
    h1.Fill(t.theta_x)
    h2.Fill(t.phi_1)
    h3.Fill(t.phi_2)
    h4.Fill(t.theta_phi_1)
    h5.Fill(t.theta_phi_2)
    b0= (t.pt[0]<=3.0 and t.isVeryLoose[0]==1) or (t.pt[0]<=5.0 and t.pt[0]>3.0 and t.isLowPt [0]==1) or (t.pt[0]>5.0 and t.isMedium[0]==1)
    b1= (t.pt[1]<=3.0 and t.isVeryLoose[1]==1) or (t.pt[1]<=5.0 and t.pt[1]>3.0 and t.isLowPt [1]==1) or (t.pt[1]>5.0 and t.isMedium[1]==1)
    b2= (t.pt[2]<=3.0 and t.isVeryLoose[2]==1) or (t.pt[2]<=5.0 and t.pt[2]>3.0 and t.isLowPt [2]==1) or (t.pt[2]>5.0 and t.isMedium[2]==1)
    b3= (t.pt[3]<=3.0 and t.isVeryLoose[3]==1) or (t.pt[3]<=5.0 and t.pt[3]>3.0 and t.isLowPt [3]==1) or (t.pt[3]>5.0 and t.isMedium[3]==1)
    if b0 and b1 and b2 and b3:
        i1.Fill(t.theta_x)
        i2.Fill(t.phi_1)
        i3.Fill(t.phi_2)
        i4.Fill(t.theta_phi_1)
        i5.Fill(t.theta_phi_2)


outFile = ROOT.TFile.Open(outpath,'UPDATE')
outFile.cd()
h1.Write(h1.GetName(),ROOT.TObject.kOverwrite)
h2.Write(h2.GetName(),ROOT.TObject.kOverwrite)
h3.Write(h3.GetName(),ROOT.TObject.kOverwrite)
h4.Write(h4.GetName(),ROOT.TObject.kOverwrite)
h5.Write(h5.GetName(),ROOT.TObject.kOverwrite)
i1.Write(i1.GetName(),ROOT.TObject.kOverwrite)
i2.Write(i2.GetName(),ROOT.TObject.kOverwrite)
i3.Write(i3.GetName(),ROOT.TObject.kOverwrite)
i4.Write(i4.GetName(),ROOT.TObject.kOverwrite)
i5.Write(i5.GetName(),ROOT.TObject.kOverwrite)


outFile.Close()
f.Close()

