'''
Created on Jun 29, 2013
@author: Wenhao Sun
'''

import fractions
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.core.surface import get_symmetrically_distinct_miller_indices
import operator
import numpy as np
import numpy.linalg as npl
from numpy import pi


class get_sym_fam():
    def __init__(self,bulkstruct):
        self.bulkstruct=bulkstruct
        
    def get_equivalent_miller_indices(self,mindex):
        basis=np.array(self.bulkstruct.lattice.matrix)
    
        A,X=self.get2vectsinplane(basis,mindex)
        v1=A[0]
        v2=A[1]
        
        millerindex=self.getmillerfrom2v(basis, v1, v2)
        
        if np.array_equal(millerindex,mindex*-1):
            v2=A[0]
            v1=A[1]
        C=[]
        latt = self.bulkstruct.lattice
        symmops = SpacegroupAnalyzer(self.bulkstruct, 0.01).get_symmetry_operations(True)
        for op in symmops:
            for site in self.bulkstruct:
                newv1 = op.apply_rotation_only(v1)
                newv2 = op.apply_rotation_only(v2)
                millerindex=np.array(self.getmillerfrom2v(basis, newv1, newv2,errfrac=False))
                if any(millerindex==None):
                    continue
                exists=False
                for Ccheck in C:
                    c=0
                    for ind in range(0,3):
                        if Ccheck[ind]==millerindex[ind]:
                            c+=1
                    if c==3:
                        exists=True                    
                if exists==False:
                    C.append(millerindex)    
        
        retC=np.zeros((len(C),3))
        for Cx in range(0,len(C)):
            retC[Cx]=C[Cx]
        a=retC
        ind=np.lexsort((a[:,2],a[:,1],a[:,0]))
        ind_rounded=np.round(a[ind])
        return ind_rounded
    
    def get2vectsinplane(self,basis, maxindex):
        #% The two returned vectors are in cartesian coordinates
        if len(maxindex) != 3:
            raise('Error need 3 elements in your maxindex')
    
        zeroind=np.where(np.abs(maxindex)<0.001)[0]
        numzero = len(zeroind)
        
        h = float(maxindex[0])
        k = float(maxindex[1])
        l = float(maxindex[2])
       
        if numzero == 0:
            hd=fractions.Fraction(1/float(h)).limit_denominator(12).denominator
            kd=fractions.Fraction(1/float(k)).limit_denominator(12).denominator
            ld=fractions.Fraction(1/float(l)).limit_denominator(12).denominator
            lst=[hd,kd,ld]
            multfact=1
            for ii in lst:
                multfact=multfact*ii / fractions.gcd(multfact,ii)

            p1=np.array([multfact/h,0,0])
            p2=np.array([0,multfact/k,0])
            p3=np.array([0,0,multfact/l])
            
            P=np.array([p1,p2,p3])
            for aa in range(0,3):
                v1=P[np.mod(aa+1,3),:]-P[np.mod(aa,3),:]
                v2=P[np.mod(aa+2,3),:]-P[np.mod(aa,3),:]
                T=self.ang(v1,v2);
                if T<=pi/2:
                    twovects=np.array([v1,v2]);
                    break;
            
        elif numzero==1:
            ind=list()
            P=list()
            for jj in range(0,3):
                if jj==zeroind:
                    p1=np.array([0, 0, 0])
                    p1[jj]=1
                    v1=p1
                else:
                    ind.append(jj)
                    P.append(maxindex[jj])
            
            ad=fractions.Fraction(1/float(P[0])).limit_denominator(12).denominator
            bd=fractions.Fraction(1/float(P[1])).limit_denominator(12).denominator
            
            
            lst=[ad,bd]
            multfact=1
            for ii in lst:
                multfact=multfact*ii / fractions.gcd(multfact,ii)
                
            points=np.zeros((2,3));
            for mm in range(0,2):
                pointtemp=np.array([0, 0, 0])
                pointtemp[ind[mm]]=multfact/P[mm]
                points[mm,:]=pointtemp
            v2=points[1]-points[0]
            
            
            twovects=np.array([v1,v2])
            P=np.array([p1, points[0],points[1]])
            
        elif numzero==2:
            maxindex=maxindex/npl.norm(maxindex);
            b = []
            for i in maxindex:
                b.append(abs(float(i)))
            maxindex=b        
            if maxindex == [1, 0, 0]:
                twovects=np.array([[0, 0, 1],[0, 1, 0]])
            elif maxindex==[0, 1, 0]:
                twovects=np.array([[1, 0, 0],[0, 0, 1]])
            elif maxindex==[0, 0, 1]:
                twovects=np.array([[1, 0, 0],[0, 1, 0]])

            P=np.array([twovects[0], twovects[1], [0, 0,0]]);
            
        twovects[0]=twovects[0]/fractions.gcd(fractions.gcd(twovects[0,0], twovects[0,1]),twovects[0,2])
        twovects[1]=twovects[1]/fractions.gcd(fractions.gcd(twovects[1,0], twovects[1,1]),twovects[1,2])
        twovects=np.dot(twovects,basis);
        for v in twovects:
            for x in v:
                if x > 10:
                    pass
                    
        return twovects,P
    
    def _representsint(self,s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
        
    def getmillerfrom2v(self,basis,v1,v2,errfrac=True):
        
        TM=np.eye(3,3)
        millerv1=np.dot(TM,np.transpose(v1))
        millerv2=np.dot(TM,np.transpose(v2))
        
        if self.ang(millerv1,millerv2,True)<1E-2:
            return None
        
        millerv1=np.dot(npl.inv(np.transpose(basis)),millerv1)
        millerv2=np.dot(npl.inv(np.transpose(basis)),millerv2)
        
        millerindex=np.transpose(np.cross(millerv1,millerv2))
        if np.isnan(millerindex).any():
                print(millerindex)
                print(v1,millerv1)
                print(v2,millerv2)
                raise('Error')
        
        md=np.zeros((3,1))
        for ni in range(0,3):
            md[ni]=fractions.Fraction(millerindex[ni]).limit_denominator(12).denominator
        
        MLCM=1
        for ii in md:
            MLCM=MLCM*ii / fractions.gcd(MLCM,ii)
        
        millerindex=millerindex*MLCM;
        roundedmillerindex=np.array([ round(elem,1) for elem in millerindex])
        diffmill=roundedmillerindex-millerindex
        if npl.norm(diffmill)>0.005:
            if errfrac==True:
                raise SystemError('Error: Miller Index is Fractional')
            else:
                return None
        
        for elem in range(0,3):
            if roundedmillerindex[elem]==-0:
                roundedmillerindex[elem]=0
        
        millerindex=roundedmillerindex
        MGCD=np.abs(fractions.gcd(fractions.gcd(millerindex[0],millerindex[1]),millerindex[2]))
        
        if MGCD==0:
            raise("Zero in the Miller greatest common denominator")
            print(millerindex)
            print(millerv1, millerv2)
            return None
        
        millerindex=millerindex/MGCD
        return millerindex    
    
    def ang(self, v1, v2,acute=False):
        if npl.norm(v1)==0 or npl.norm(v2)==0:
            raise('One of your vectors has length zero')
        x=np.dot(v1,v2)/(npl.norm(v1)*npl.norm(v2))
        a= np.float('%.12f' %x)
        angle=np.arccos(a)
        if acute==True:
            if angle>pi/2:
                angle=pi-angle
        return angle
    