# FlyBrainLab Datasets
This repository contains information regarding the FlyBrainLab Datasets (version, source, loading scripts, etc.)

[FlyCircuit](#flycircuit) | [Hemibrain](#hemibrain) | [Larva L1EM](#larva-l1em)

## FlyCircuit
The FlyCircuit Database is provided by the NTHU Team. See [[1]](#ref-1) for details.

## Hemibrain
The Hemibrain Dataset was extracted from Hemibrain [v1.0.1 and v1.1](https://www.janelia.org/project-team/flyem/hemibrain). See [[2]](#ref-2) for details. Original data licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Larva L1EM
Connectomics data from the Larva L1EM Central Nervous System is provided publically by CATMAID database served on [Virtual Fly Brain](https://l1em.catmaid.virtualflybrain.org). 

### Set Up
Refer to `l1em/Load_Larva_L1EM.ipynb` for information on loading the dataset into a locally running OrientDB database instance.
Alternatively, you can also refer to `l1em/Load_Larva_L1EM.py` and the command line interface defined therein.

Before you move forward, you will need to download the SWC files and place it in `l1em` folder (with path `l1em/swc`).
The dataset can be downloaded from [here](TODO)

### Dataset Info

|# Neurons|# Connections| Total File Size | License | Publication |
| --------|-------------| --------------- | ------- | ----------- |
| 1501    | 30350 neuron pairs | 131 MB   | [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)| [[3]](#ref-3)


## References
1. <a name="ref-1"></a> Ann-Shyn Chiang et al., Three-dimensional reconstruction of brain-wide wiring networks in Drosophila at single-cell resolution, Current Biology 2011, 21(1), pp.1-11. [DOI](https://doi.org/10.1016/j.cub.2010.11.056).
2. <a name="ref-2"></a> C. Shan Xu et al., A Connectome of the Adult Drosophila Central Brain. bioRxiv 2020.01.21.911859. [DOI](https://doi.org/10.1101/2020.01.21.911859).
3. <a name="ref-3"></a> Ohyama T, et al. A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
