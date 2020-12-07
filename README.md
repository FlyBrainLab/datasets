# FlyBrainLab Datasets
This repository contains information regarding the FlyBrainLab Datasets (version, source, loading scripts, etc.)

[FlyCircuit](#flycircuit) | [Hemibrain](#hemibrain) | [Larva L1EM](#larva-l1em)

## FlyCircuit
_Coming Soon_

## Hemibrain
_Coming Soon_

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
| 1501    | 30350 neuron pairs | 131 MB   | [CC-BY-SA_4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)| [[1]](#ref-1)


## References
1. <a name="ref-1"></a> Ohyama T, et al. A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
