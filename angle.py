import ROOT,glob,math,os
from array import array
import argparse
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
args = parser.parse_args()

path="./root/"
paths=glob.glob(path+"*root")
rootpath=paths[int(args.path)]
outpath=rootpath.replace("/root","/hist")
print(outpath)

h1=ROOT.TH1F("theta_x","theta_x",200,0,4)
h2=ROOT.TH1F("phi_1","phi_1",200,0,4)
h3=ROOT.TH1F("phi_2","phi_2",200,0,4)
h4=ROOT.TH1F("theta_phi_1","theta_phi_1",200,0,4)
h5=ROOT.TH1F("theta_phi_2","theta_phi_2",200,0,4)
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
    if t.match[0]==t.match[1]:
        muon_1.SetPxPyPzE(t.muon_1[0],t.muon_1[1],t.muon_1[2],t.muon_1[3])
        muon_2.SetPxPyPzE(t.muon_2[0],t.muon_2[1],t.muon_2[2],t.muon_2[3])
        muon_3.SetPxPyPzE(t.muon_3[0],t.muon_3[1],t.muon_3[2],t.muon_3[3])
        muon_4.SetPxPyPzE(t.muon_4[0],t.muon_4[1],t.muon_4[2],t.muon_4[3])
        if abs((muon_1+muon_2).Px()-t.jpsi_1[0])<=1.:
            jpsi_1.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
            jpsi_2.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
        else:
            jpsi_1.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
            jpsi_2.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
    elif t.match[0]==t.match[2]:
        muon_1.SetPxPyPzE(t.muon_1[0],t.muon_1[1],t.muon_1[2],t.muon_1[3])
        muon_3.SetPxPyPzE(t.muon_2[0],t.muon_2[1],t.muon_2[2],t.muon_2[3])
        muon_2.SetPxPyPzE(t.muon_3[0],t.muon_3[1],t.muon_3[2],t.muon_3[3])
        muon_4.SetPxPyPzE(t.muon_4[0],t.muon_4[1],t.muon_4[2],t.muon_4[3])
        if abs((muon_1+muon_2).Px()-t.jpsi_1[0])<=1.:
            jpsi_1.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
            jpsi_2.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
        else:
            jpsi_1.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
            jpsi_2.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
    else:
        muon_1.SetPxPyPzE(t.muon_1[0],t.muon_1[1],t.muon_1[2],t.muon_1[3])
        muon_3.SetPxPyPzE(t.muon_2[0],t.muon_2[1],t.muon_2[2],t.muon_2[3])
        muon_4.SetPxPyPzE(t.muon_3[0],t.muon_3[1],t.muon_3[2],t.muon_3[3])
        muon_2.SetPxPyPzE(t.muon_4[0],t.muon_4[1],t.muon_4[2],t.muon_4[3])
        if abs((muon_1+muon_2).Px()-t.jpsi_1[0])<=1.:
            jpsi_1.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
            jpsi_2.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
        else:
            jpsi_1.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
            jpsi_2.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
    x=jpsi_1+jpsi_2
    
    #Compute phi1,phi2
    p_muon_1=ROOT.Math.Plane3D.Point() 
    p_muon_1.SetXYZ(muon_1.Px(),muon_1.Py(),muon_1.Pz())
    p_muon_2=ROOT.Math.Plane3D.Point() 
    p_muon_2.SetXYZ(muon_2.Px(),muon_2.Py(),muon_2.Pz())
    p_muon_3=ROOT.Math.Plane3D.Point() 
    p_muon_3.SetXYZ(muon_3.Px(),muon_3.Py(),muon_3.Pz())
    p_muon_4=ROOT.Math.Plane3D.Point() 
    p_muon_4.SetXYZ(muon_4.Px(),muon_4.Py(),muon_4.Pz())
    p_jpsi_1=ROOT.Math.Plane3D.Point() 
    p_jpsi_1.SetXYZ(jpsi_1.Px(),jpsi_1.Py(),jpsi_1.Pz())
    p_jpsi_2=ROOT.Math.Plane3D.Point() 
    p_jpsi_2.SetXYZ(jpsi_2.Px(),jpsi_2.Py(),jpsi_2.Pz())
    p_zero=ROOT.Math.Plane3D.Point() 
    p_zero.SetXYZ(0.0,0.0,0.0)
    muon_plane_12=ROOT.Math.Plane3D(p_zero,p_muon_1,p_muon_2)
    muon_plane_34=ROOT.Math.Plane3D(p_zero,p_muon_3,p_muon_4)
    jpsi_plane_12=ROOT.Math.Plane3D(p_zero,p_jpsi_1,p_jpsi_2)
    muon_nvector_12=muon_plane_12.Normal()
    muon_nvector_34=muon_plane_34.Normal()
    jpsi_nvector_12=jpsi_plane_12.Normal()
    
    muon_nvector3_12=ROOT.TVector3()
    muon_nvector3_12.SetXYZ(muon_nvector_12.X(),muon_nvector_12.Y(),muon_nvector_12.Z())
    muon_nvector3_34=ROOT.TVector3()
    muon_nvector3_34.SetXYZ(muon_nvector_34.X(),muon_nvector_34.Y(),muon_nvector_34.Z())
    jpsi_nvector3_12=ROOT.TVector3()
    jpsi_nvector3_12.SetXYZ(jpsi_nvector_12.X(),jpsi_nvector_12.Y(),jpsi_nvector_12.Z())
    phi_1=jpsi_nvector3_12.Angle(muon_nvector3_12)
    phi_2=jpsi_nvector3_12.Angle(muon_nvector3_34)
        
    #Boost and compute theta_x
    boost=-(muon_1+muon_2+muon_3+muon_4).BoostVector()
    muon_1.Boost(boost)
    muon_2.Boost(boost)
    muon_3.Boost(boost)
    muon_4.Boost(boost)
    jpsi_1.Boost(boost)
    jpsi_2.Boost(boost)
    theta_x=x.Angle(jpsi_1.Vect())
    muon_RF=ROOT.TLorentzVector()
    muon_RF=muon_1+ muon_2+ muon_3 + muon_4
    
    #Boost and compute theta_phi_1
    boost_12=-(muon_1+muon_2).BoostVector()
    muon_1.Boost(boost_12)
    muon_2.Boost(boost_12)
    theta_phi_1=muon_1.Angle(jpsi_1.Vect())
    
    #Boost and compute theta_phi_2
    boost_34=-(muon_3+muon_4).BoostVector()
    muon_3.Boost(boost_34)
    muon_4.Boost(boost_34)
    theta_phi_2=muon_3.Angle(jpsi_2.Vect())
    
    h1.Fill(theta_x)
    h2.Fill(phi_1)
    h3.Fill(phi_2)
    h4.Fill(theta_phi_1)
    h5.Fill(theta_phi_2)
    
outFile = ROOT.TFile.Open(outpath,'UPDATE')
outFile.cd()
h1.Write(h1.GetName(),ROOT.TObject.kOverwrite)
h2.Write(h2.GetName(),ROOT.TObject.kOverwrite)
h3.Write(h3.GetName(),ROOT.TObject.kOverwrite)
h4.Write(h4.GetName(),ROOT.TObject.kOverwrite)
h5.Write(h5.GetName(),ROOT.TObject.kOverwrite)
outFile.Close()
f.Close()





