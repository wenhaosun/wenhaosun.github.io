---
description: >
  MSE Open House
hide_description: true
---
# UM MSE Open House 2020

Welcome to the University of Michigan Materials Science and Engineering Open House!

Please copy the relevant section of the code into Spyder, and follow along with the presentation. 


## Part 1: Convex Hulls for Stability Analysis
~~~~
from pymatgen import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter

#This initializes the REST adaptor. Put your own API key in.
MPR = MPRester("2d5wyVmhDCpPMAkq")
 
#Entries are the basic unit for thermodynamic and other analyses in pymatgen.
#This gets all entries belonging to the Ca-C-O system.
entries = MPR.get_entries_in_chemsys(['Mn', 'N'])

#With entries, you can do many sophisticated analyses, 
#like creating phase diagrams.
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.show() 
~~~~

## Part 2: Ionic Substitution
~~~~
from pymatgen import MPRester
from pymatgen.core.structure import Structure
from pymatgen.core.periodic_table import Element
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.core.composition import Composition

#This initializes the REST adaptor. Put your own API key in.
MPR = MPRester("2d5wyVmhDCpPMAkq")
 
#Entries are the basic unit for thermodynamic and other analyses in pymatgen.
#This gets all entries belonging to the Ca-C-O system.
structure=MPR.get_structure_by_material_id('mp-12906')
print(structure)

structure.replace_species({Element('Sr'):Element('Ru')})
print(structure)

#The Ba3CrN3 compound has a DFT-calculated energy of 
NewCompound=ComputedEntry(Composition('Sr3RuN3'),-86.1719 )
entries = MPR.get_entries_in_chemsys(['Sr', 'Ru', 'N'])
entries.append(NewCompound)
#With entries, you can do many sophisticated analyses, 
#like creating phase diagrams.
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.show() 
~~~~

## Part 3: Making a Map

Download the Data File here: [TernaryNitridesEnergy.csv][TernaryNitridesData]
Move it to your Spyder Folder:
1. In Chrome, press Ctrl+J to open Download Director
2. For the downloaded file, click on Show in Folder
3. Highlight the file, Copy with Ctrl+C
4. In your Spyder directory, press Open (yes, open)
5. In the window, paste the downloaded CSV file.

~~~~
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.DataFrame.from_csv('TernaryNitridesEnergy.csv')

cmap=sns.light_palette("Blue", reverse=True,as_cmap=True)
sns.set_style("whitegrid")

plt.subplots(figsize=(20,20))
g=sns.heatmap(df, cmap=cmap)
#g=sns.clustermap(df,cmap=cmap,figsize=(20,20))

plt.show()
~~~~

## The Final Version of the Map
[Interactive Ternary Nitrides Map][ternarymap]


[ternarymap]: /TernaryNitridesMap.html
[TernaryNitridesData]: /TernaryNitridesEnergy.csv
