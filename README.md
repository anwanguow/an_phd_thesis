The code and data related to my PhD thesis
==============

Figures
-----------------
Each figure in this thesis can be found in the "Figures" directory. The majority of the figures were drawn in Keynote and converted to PDF format, while some were generated using Python code.

Publication Related to this Thesis
-----------------
Chapter 4 ([PhysRevB.111.054116](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.111.054116)): https://github.com/anwanguow/graph_phase_transition;

Chapter 5 ([PhysRevE.111.064302](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.111.064302)): https://github.com/anwanguow/GP_structural;

Chapter 6 ([PhysRevE.111.045306](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.111.045306)): https://github.com/anwanguow/PH_structural.

Dataset Generation
-----------------
To be continued...

Core Algorithms
-----------------
### Cut Distance

To be continued...

### Modified Voronoi Method

To be continued...

### Persistent Homology

#### PH Descriptors

To be continued...

Example in Chapter 5
-----------------
In Section 5.2.5.3 of my PhD thesis, I calculated the Type C/D descriptors for each particle sample and constructed a feature matrix by concatenation, followed by PCA analysis, with the results shown in the following figure.

<img src="Figures/Chapter_5_PRE_Network/FIG_7.png" alt="fig1" width="400">

Referring to the method used by Lei Wang in [Phys. Rev. B 94, 195105](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.94.195105), where the matrix of configurations of the Ising model at different temperatures were concatenated and analyzed by PCA, it was found that this approach is highly effective for phase classification and detecting the critical point of the second-order phase transition in the Ising model. However, when I applied the same method to predict the mobility trend in a multi-particle system in my thesis, the method outputs nothing meaningful.

The implementation details of the core methods and the corresponding results are provided in [Implementation.md](Examples/Implementation.md) and the generated [Implementation.pdf](Examples/Implementation.pdf) in "Example" directory.

Besides, it can also be consulted in repo: https://github.com/anwanguow/pca_ising.

Contact
-----------------
An Wang: amturing@outlook.com 
