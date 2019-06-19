---
layout: project
title: 'Efficient creation and convergence of surface slabs'
date: 1 Nov 2013
image: /assets/img/projects/surface_slabs.png
screenshot: /assets/img/projects/surface_slabs.png
links:
  - title: Link to Surface Science
    url: https://www.sciencedirect.com/science/article/pii/S003960281300160X
caption: Surface Science, 2013
description: >
   We present an algorithm to create surface slabs of any orientation from any crystal structure. 
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

The supercell slab is the structural model used in first-principles simulations to determine thermodynamic, kinetic, and electronic properties of surfaces and interfaces. We present a general algorithm to reorient bulk unit cells using basis and covariant transformations — the first step for constructing surface slabs of any Miller index from bulk unit cells of any Bravais lattice. We further review and discuss subtleties of surface slab creation relevant for performing efficient and accurate calculations of surface properties. We also demonstrate that the nonconvergence of surface energy with respect to slab thickness can be mitigated if the bulk reference energy is calculated from a surface-oriented bulk unit cell, which eliminates Brillouin zone integration errors between the slab and the bulk. Using Pt(111) and Si(111) surfaces as examples, this technique converges the surface energy with respect to slab thickness requiring only one bulk and one relatively thin slab calculation, with moderate k-point densities. This process is about an order of magnitude more efficient than popular surface energy convergence techniques involving multiple slab calculations.

[Link to Surface Science Article](https://www.sciencedirect.com/science/article/pii/S003960281300160X)

[Link to follow up article](https://www.nature.com/articles/sdata201680#auth-4) by Richard Tran et al. on the Surface Energies of Elemental Crystals

