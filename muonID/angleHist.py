import ROOT,glob,math,os
from array import array

h1=ROOT.TH1F("theta_x","theta_x",200,0,4)
h2=ROOT.TH1F("phi_1","phi_1",200,0,4)
h3=ROOT.TH1F("phi_2","phi_2",200,0,4)
h4=ROOT.TH1F("theta_phi_1","theta_phi_1",200,0,4)
h5=ROOT.TH1F("theta_phi_2","theta_phi_2",200,0,4)

#a1:loose a2:very loose a3:low pt
i1=ROOT.TH1F("theta_x_a1","theta_x_a1",200,0,4)
i2=ROOT.TH1F("phi_1_a1","phi_1_a1",200,0,4)
i3=ROOT.TH1F("phi_2_a1","phi_2_a1",200,0,4)
i4=ROOT.TH1F("theta_phi_1_a1","theta_phi_1_a1",200,0,4)
i5=ROOT.TH1F("theta_phi_2_a1","theta_phi_2_a1",200,0,4)

j1=ROOT.TH1F("theta_x_a2","theta_x_a2",200,0,4)
j2=ROOT.TH1F("phi_1_a2","phi_1_a2",200,0,4)
j3=ROOT.TH1F("phi_2_a2","phi_2_a2",200,0,4)
j4=ROOT.TH1F("theta_phi_1_a2","theta_phi_1_a2",200,0,4)
j5=ROOT.TH1F("theta_phi_2_a2","theta_phi_2_a2",200,0,4)

k1=ROOT.TH1F("theta_x_a3","theta_x_a3",200,0,4)
k2=ROOT.TH1F("phi_1_a3","phi_1_a3",200,0,4)
k3=ROOT.TH1F("phi_2_a3","phi_2_a3",200,0,4)
k4=ROOT.TH1F("theta_phi_1_a3","theta_phi_1_a3",200,0,4)
k5=ROOT.TH1F("theta_phi_2_a3","theta_phi_2_a3",200,0,4)


outpath="./Reduce/hist.root"
print(outpath)
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
    if t.isMedium[0]==1 and t.isMedium[1]==1 and t.isLoose[2]==1 and t.isLoose[3]==1 :
        i1.Fill(t.theta_x)
        i2.Fill(t.phi_1)
        i3.Fill(t.phi_2)
        i4.Fill(t.theta_phi_1)
        i5.Fill(t.theta_phi_2)
    if t.isMedium[0]==1 and t.isMedium[1]==1 and t.isVeryLoose[2]==1 and t.isVeryLoose[3]==1 :
        j1.Fill(t.theta_x)
        j2.Fill(t.phi_1)
        j3.Fill(t.phi_2)
        j4.Fill(t.theta_phi_1)
        j5.Fill(t.theta_phi_2)
    if t.isMedium[0]==1 and t.isMedium[1]==1 and t.isLowPt[2]==1 and t.isLowPt[3]==1 :
        k1.Fill(t.theta_x)
        k2.Fill(t.phi_1)
        k3.Fill(t.phi_2)
        k4.Fill(t.theta_phi_1)
        k5.Fill(t.theta_phi_2)

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
j1.Write(j1.GetName(),ROOT.TObject.kOverwrite)
j2.Write(j2.GetName(),ROOT.TObject.kOverwrite)
j3.Write(j3.GetName(),ROOT.TObject.kOverwrite)
j4.Write(j4.GetName(),ROOT.TObject.kOverwrite)
j5.Write(j5.GetName(),ROOT.TObject.kOverwrite)
k1.Write(k1.GetName(),ROOT.TObject.kOverwrite)
k2.Write(k2.GetName(),ROOT.TObject.kOverwrite)
k3.Write(k3.GetName(),ROOT.TObject.kOverwrite)
k4.Write(k4.GetName(),ROOT.TObject.kOverwrite)
k5.Write(k5.GetName(),ROOT.TObject.kOverwrite)

outFile.Close()
f.Close()



