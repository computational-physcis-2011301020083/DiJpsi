import ROOT,glob,math,os
from array import array
import numpy as np

outpath="./Reduce/sig.root"
print(outpath)
file1 = ROOT.TFile(outpath, 'recreate')
tree = ROOT.TTree("nominal", "Muon ID and trigger")

Theta_x  = array('f',[0])
Phi_1  = array('f',[0])
Phi_2  = array('f',[0])
Theta_phi_1  = array('f',[0])
Theta_phi_2  = array('f',[0])

pt = array('f',[0,0,0,0])
isMuon = array('f',[0,0,0,0])
isTight = array('f',[0,0,0,0])
isMedium = array('f',[0,0,0,0])
isLoose = array('f',[0,0,0,0])
isVeryLoose = array('f',[0,0,0,0])
isHighPt = array('f',[0,0,0,0])
isLowPt = array('f',[0,0,0,0])

tree.Branch("theta_x",  Theta_x,  'theta_x/F')
tree.Branch("phi_1",  Phi_1,  'phi_1/F')
tree.Branch("phi_2", Phi_2, 'phi_2/F')
tree.Branch("theta_phi_1",  Theta_phi_1,  'theta_phi_1/F')
tree.Branch("theta_phi_2", Theta_phi_2, 'theta_phi_2/F')
tree.Branch("pt", pt ,  'pt[4]/F')
tree.Branch("isMuon", isMuon ,  'isMuon[4]/F')
tree.Branch("isTight", isTight ,  'isTight[4]/F')
tree.Branch("isMedium", isMedium ,  'isMedium[4]/F')
tree.Branch("isLoose", isLoose ,  'isLoose[4]/F')
tree.Branch("isVeryLoose", isVeryLoose ,  'isVeryLoose[4]/F')
tree.Branch("isHighPt", isHighPt ,  'isHighPt[4]/F')
tree.Branch("isLowPt", isLowPt ,  'isLowPt[4]/F')

rootpath="./signal/sig.root"
f=ROOT.TFile(rootpath,"r")
#hists=[]
t=f.Get("BPHY13")
N=t.GetEntries()
for i in range(N):
    t.GetEntry(i)
    
    muon_1_pt_ID=[t.muo_pt[0]/1000.0,t.muo_isMuon[0],t.muo_isTight[0],t.muo_isMedium[0],t.muo_isLoose[0],t.muo_isVeryLoose[0],t.muo_isHighPt[0],t.muo_isLowPt[0]]
    muon_2_pt_ID=[t.muo_pt[1]/1000.0,t.muo_isMuon[1],t.muo_isTight[1],t.muo_isMedium[1],t.muo_isLoose[1],t.muo_isVeryLoose[1],t.muo_isHighPt[1],t.muo_isLowPt[1]]
    muon_3_pt_ID=[t.muo_pt[2]/1000.0,t.muo_isMuon[2],t.muo_isTight[2],t.muo_isMedium[2],t.muo_isLoose[2],t.muo_isVeryLoose[2],t.muo_isHighPt[2],t.muo_isLowPt[2]]
    muon_4_pt_ID=[t.muo_pt[3]/1000.0,t.muo_isMuon[3],t.muo_isTight[3],t.muo_isMedium[3],t.muo_isLoose[3],t.muo_isVeryLoose[3],t.muo_isHighPt[3],t.muo_isLowPt[3]]
    muon_list=[muon_1_pt_ID,muon_2_pt_ID,muon_3_pt_ID,muon_4_pt_ID]
    #print(np.multiply(muon_list,1))
    muon_list=np.multiply(sorted(muon_list),1)
    #print(muon_list)
    pt[0]=muon_list[3][0]
    pt[1]=muon_list[2][0]
    pt[2]=muon_list[1][0]
    pt[3]=muon_list[0][0]
    isMuon[0]=muon_list[3][1]
    isMuon[1]=muon_list[2][1]
    isMuon[2]=muon_list[1][1]
    isMuon[3]=muon_list[0][1]
    isTight[0]=muon_list[3][2]
    isTight[1]=muon_list[2][2]
    isTight[2]=muon_list[1][2]
    isTight[3]=muon_list[0][2]
    isMedium[0]=muon_list[3][3]
    isMedium[1]=muon_list[2][3]
    isMedium[2]=muon_list[1][3]
    isMedium[3]=muon_list[0][3]
    isLoose[0]=muon_list[3][4]
    isLoose[1]=muon_list[2][4]
    isLoose[2]=muon_list[1][4]
    isLoose[3]=muon_list[0][4]
    isVeryLoose[0]=muon_list[3][5]
    isVeryLoose[1]=muon_list[2][5]
    isVeryLoose[2]=muon_list[1][5]
    isVeryLoose[3]=muon_list[0][5]
    isHighPt[0]=muon_list[3][6]
    isHighPt[1]=muon_list[2][6]
    isHighPt[2]=muon_list[1][6]
    isHighPt[3]=muon_list[0][6]
    isLowPt[0]=muon_list[3][7]
    isLowPt[1]=muon_list[2][7]
    isLowPt[2]=muon_list[1][7]
    isLowPt[3]=muon_list[0][7]
    
    muon_1=ROOT.TLorentzVector()
    muon_2=ROOT.TLorentzVector()
    muon_3=ROOT.TLorentzVector()
    muon_4=ROOT.TLorentzVector()
    jpsi_1=ROOT.TLorentzVector()
    jpsi_2=ROOT.TLorentzVector()
    x=ROOT.TLorentzVector()
    #muon_1.SetPtEtaPhiE(t.muo_rf_pt[0],t.muo_rf_eta[0],t.muo_rf_phi[0],t.muo_rf_E[0])
    #muon_2.SetPtEtaPhiE(t.muo_rf_pt[1],t.muo_rf_eta[1],t.muo_rf_phi[1],t.muo_rf_E[1])
    #muon_3.SetPtEtaPhiE(t.muo_rf_pt[2],t.muo_rf_eta[2],t.muo_rf_phi[2],t.muo_rf_E[2])
    #muon_4.SetPtEtaPhiE(t.muo_rf_pt[3],t.muo_rf_eta[3],t.muo_rf_phi[3],t.muo_rf_E[3])
    #jpsi_1.SetPxPyPzE(t.jpsi_1[0],t.jpsi_1[1],t.jpsi_1[2],t.jpsi_1[3])
    #jpsi_2.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
    #x.jpsi_2.SetPxPyPzE(t.jpsi_2[0],t.jpsi_2[1],t.jpsi_2[2],t.jpsi_2[3])
    muon_1.SetPtEtaPhiE(t.muo_pt[0],t.muo_eta[0],t.muo_phi[0],t.muo_E[0])
    muon_2.SetPtEtaPhiE(t.muo_pt[1],t.muo_eta[1],t.muo_phi[1],t.muo_E[1])
    muon_3.SetPtEtaPhiE(t.muo_pt[2],t.muo_eta[2],t.muo_phi[2],t.muo_E[2])
    muon_4.SetPtEtaPhiE(t.muo_pt[3],t.muo_eta[3],t.muo_phi[3],t.muo_E[3])
    jpsi_1=muon_1+muon_2
    jpsi_2=muon_3+muon_4
    x=muon_1+muon_2+muon_3+muon_4
    
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
    
    Theta_x[0]=theta_x
    Phi_1[0]=phi_1
    Phi_2[0]=phi_2
    Theta_phi_1[0]=theta_phi_1
    Theta_phi_2[0]=theta_phi_2
    
    
    
    tree.Fill()
file1.Write()
file1.Close()
f.Close()




