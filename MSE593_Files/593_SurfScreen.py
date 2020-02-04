from pymatgen.core.structure import Structure
from pymatgen.core.surface import miller_index_from_sites,get_symmetrically_distinct_miller_indices
from get_sym_fam import get_sym_fam  
from itertools import combinations
from pymatgen import MPRester
import numpy as np
import numpy.linalg as npl

def surfscreen(structure,MI_lib,r=5):
    MI_List=[]
    for site in structure:
        nearbysites=structure.get_neighbors(site,r)
        perm=combinations(nearbysites, 2)
        
        for two_sites in perm:
            three_coords=[site.coords]
            for X in two_sites:
                three_coords.append(X[0].coords)
                
            MI=miller_index_from_sites(structure.lattice.matrix, three_coords)
            if any(np.abs(MI) > 4):
                continue
            if np.isnan(MI).any():
                continue
            MI_rounded=np.round(MI)
            if npl.norm(MI_rounded-MI)>0.01:
                continue
            MI_List.append(MI_rounded)
    
    PlotDict={}
    for index in MI_List:
        for key in MI_lib.keys():
            if any((index == x).all() for x in MI_lib[key]):
                if key not in PlotDict.keys():
                    PlotDict[key]=0
                PlotDict[key]+=1
                print(index, MI_lib[key])
    
    import matplotlib.pyplot as plt
    
    plt.bar(PlotDict.keys(), PlotDict.values(), color='g')
    plt.show()

    
def MillerIndexLibrary(structure):
    MI_lib={}
    UniqueIndices=get_symmetrically_distinct_miller_indices(structure, max_index=4)
    for Index in UniqueIndices:
        MI_lib[str(Index)]=get_sym_fam(structure).get_equivalent_miller_indices(Index)
    return MI_lib
    
            
MPR = MPRester("2d5wyVmhDCpPMAkq")
S=MPR.get_structure_by_material_id('mp-1143', conventional_unit_cell='True')
print(S)
MI_lib=MillerIndexLibrary(S)
print(MI_lib)
surfscreen(S, MI_lib)