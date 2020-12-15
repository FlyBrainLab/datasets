# FlyBrainLab Datasets
This repository contains information regarding the FlyBrainLab Datasets (version, source, loading scripts, etc.)
Here, we provide a summary of the datasets available under NeuroArch database, and links to the preloaded database backup files that can be used to restored the databases.
Detailed instructions for loading these databases from scratch are provided in the individual folders and/or notebooks.

[FlyCircuit](#flycircuit) | [Hemibrain](#hemibrain) | [Larva L1EM](#larva-l1em)

## <a name="flycircuit"></a>[FlyCircuit Dataset](http://flycircuit.tw) [[1]](#ref-1)

|FlyCircuit Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|
|-----------|---------| --------| -------|-----|
| 1.2 | [3536a04](https://github.com/fruitflybrain/neuroarch/tree/3536a04478f77ac59fb55727ff0e3de66ccbf70c) | [flycircuit1.2_na_v1.0_backup.zip](https://drive.google.com/file/d/1JXtWt-2X66Mb5I271YRUiMuQx3I2b43s/view?usp=sharing) | [Link](https://github.com/FlyBrainLab/datasets/blob/main/flycircuit/v1.2/FlyCircuit_to_NeuroArch.ipynb) | 12/14/2020 |

## <a name="hemibrain"></a>[Hemibrain Dataset](https://www.janelia.org/project-team/flyem/hemibrain) [[2]](#ref-2)
Original data licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

|Hemibrain Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|
|-----------|---------| --------| -------|------|
| [1.1](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.1_neo4j_inputs.zip) | [3536a04](https://github.com/fruitflybrain/neuroarch/tree/3536a04478f77ac59fb55727ff0e3de66ccbf70c) | [hemibrain1.1_na_v1.0_backup.zip](https://drive.google.com/file/d/1Y63UpypJ-eMgOdX3bcSRO4Ct3DqmH6-X/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.1/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 12/14/2020 |

## Larva L1EM
Connectomics data from the Larva L1EM Central Nervous System is provided publically by CATMAID database served on [Virtual Fly Brain](https://l1em.catmaid.virtualflybrain.org). 

### Set Up
Refer to `l1em/Load_Larva_L1EM.ipynb` for information on loading the dataset into a locally running OrientDB database instance.
Alternatively, you can also refer to `l1em/Load_Larva_L1EM.py` and the command line interface defined therein.

Before you move forward, you will need to download the SWC files and place it in `l1em` folder (with path `l1em/swc`).
The dataset can be downloaded from [here](https://drive.google.com/file/d/1FFiyz_FFlHnykgTQ8xQz867R823Nj3E3/view?usp=sharing).

### Dataset Info

|# Neurons|# Connections| Total File Size | License | Publication |
| --------|-------------| --------------- | ------- | ----------- |
| 1501    | 30350 neuron pairs | 131 MB   | [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)| [[3]](#ref-3)


## References
1. <a name="ref-1"></a> Ann-Shyn Chiang et al., Three-dimensional reconstruction of brain-wide wiring networks in Drosophila at single-cell resolution, Current Biology 2011, 21(1), pp.1-11. [DOI](https://doi.org/10.1016/j.cub.2010.11.056).
2. <a name="ref-2"></a> C. Shan Xu et al., A Connectome of the Adult Drosophila Central Brain. bioRxiv 2020.01.21.911859. [DOI](https://doi.org/10.1101/2020.01.21.911859).
3. <a name="ref-3"></a> Ohyama T, et al. A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
