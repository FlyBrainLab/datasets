# Larva L1EM
Connectomics data from the Larva L1EM Central Nervous System is provided publically by CATMAID database served on [Virtual Fly Brain](https://l1em.catmaid.virtualflybrain.org).

### Set Up
Refer to `l1em/Load_Larva_L1EM.ipynb` for information on loading the dataset into a locally running OrientDB database instance.
Alternatively, you can also refer to `l1em/Load_Larva_L1EM.py` and the command line interface defined therein.

Before you move forward, you will need to download the SWC files and place it in `l1em` folder (with path `l1em/swc`).
The dataset can be downloaded from [here](https://drive.google.com/file/d/1FFiyz_FFlHnykgTQ8xQz867R823Nj3E3/view?usp=sharing).

### Dataset Info

|# Neurons|# Connections| Total File Size | License | Publication |
| --------|-------------| --------------- | ------- | ----------- |
| 1051    | 30350 neuron pairs | 131 MB   | [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)| [[3]](#ref-1)


## Release Notes

06/17/2022: UPdate database schema to NeuroArch 0.4.1

06/09/2022: Update to Neuroarch 0.4.0

01/19/2021: Fixes and Updates
- Corrections on postsynaptic site positions
- Added some tags for AL and MB.

12/14/2020: Initial Release
- Included 1,051 neurons and 30,350 connections.


## References
1. <a name="ref-1"></a> Ohyama T, et al. A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
