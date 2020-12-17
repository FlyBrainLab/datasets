# FlyBrainLab Datasets
This repository contains information regarding the FlyBrainLab Datasets (version, source, loading scripts, etc.)
Here, we provide a summary of the datasets available under NeuroArch database, and links to the preloaded database backup files that can be used to restored the databases.
Detailed instructions for loading these databases from scratch are provided in the individual folders and/or notebooks.

[FlyCircuit](#flycircuit) | [Hemibrain](#hemibrain) | [Larva L1EM](#larva-l1em) | [Medulla 7 Column](#medulla-7column)

## <a name="flycircuit"></a>[FlyCircuit Dataset](http://flycircuit.tw) [[1]](#ref-1)

|FlyCircuit Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|
|-----------|---------| --------| -------|-----|
| 1.2 | [3536a04](https://github.com/fruitflybrain/neuroarch/tree/3536a04478f77ac59fb55727ff0e3de66ccbf70c) | [flycircuit1.2_na_v1.0_backup.zip](https://drive.google.com/file/d/1JXtWt-2X66Mb5I271YRUiMuQx3I2b43s/view?usp=sharing) | [Link](https://github.com/FlyBrainLab/datasets/blob/main/flycircuit/v1.2/FlyCircuit_to_NeuroArch.ipynb) | 12/14/2020 |

## <a name="hemibrain"></a>[Hemibrain Dataset](https://www.janelia.org/project-team/flyem/hemibrain) [[2]](#ref-2)
Original data licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

|Hemibrain Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|
|-----------|---------| --------| -------|------|
| [1.1](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.1_neo4j_inputs.zip) | [3536a04](https://github.com/fruitflybrain/neuroarch/tree/3536a04478f77ac59fb55727ff0e3de66ccbf70c) | [hemibrain1.1_na_v1.0_backup.zip](https://drive.google.com/file/d/1Y63UpypJ-eMgOdX3bcSRO4Ct3DqmH6-X/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.1/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 12/14/2020 |

## <a name="larva-l1em"></a>[Larva L1EM](https://l1em.catmaid.virtualflybrain.org/) [[3]](#ref-3)
Original data licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

|L1EM Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|
|-----------|---------| --------| -------|------|
| [1.0](https://l1em.catmaid.virtualflybrain.org/) | [3536a04](https://github.com/fruitflybrain/neuroarch/tree/3536a04478f77ac59fb55727ff0e3de66ccbf70c) | [l1em1.0_na_v1.0_backup.zip](https://drive.google.com/file/d/1hYjA43poDjL8WtQ1AUBzYxKTaJ4In-GU/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/l1em/Load_Larva_L1EM.ipynb) | 12/14/2020 |

## <a name="medulla-7column"></a>[Medulla 7 Column Dataset](https://www.janelia.org/project-team/flyem/research/previous-connectomes-analyzed/seven-column-connectome-fib-sem) [[4]](#ref-medulla)
Original data licensed under [BSD 3](https://github.com/connectome-neuprint/neuPrint/blob/master/LICENSE.txt). Neuron Skeleton data from [ConnectomeHackathon2015](https://github.com/janelia-flyem/ConnectomeHackathon2015) and is licensed under the [Open Data Commons Attribution License](http://opendatacommons.org/licenses/by/1.0/).

|Medulla Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|
|-----------|---------| --------| -------|------|
| [fi25](https://github.com/connectome-neuprint/neuPrint/blob/master/fib25_neo4j_inputs.zip/) | [3484985](https://github.com/fruitflybrain/neuroarch/tree/34849855b8942bdcfebd9f8208c16875ef29a12f) | [medulla7column_fib25_na_v1.0_backup.zip]()| [Link](https://github.com/FlyBrainLab/datasets/blob/main/medulla/Medulla7column_NeuPrint_to_NeuroArch.ipynb) | 12/17/2020 |



## References
1. <a name="ref-1"></a> Ann-Shyn Chiang et al., Three-dimensional reconstruction of brain-wide wiring networks in Drosophila at single-cell resolution, Current Biology 2011, 21(1), pp.1-11. [DOI](https://doi.org/10.1016/j.cub.2010.11.056).
2. <a name="ref-2"></a> C. Shan Xu et al., A Connectome of the Adult Drosophila Central Brain. bioRxiv 2020.01.21.911859. [DOI](https://doi.org/10.1101/2020.01.21.911859).
3. <a name="ref-3"></a> Ohyama T. et al. A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
4. <a name="ref-medulla"></a> Takemura S. et al. Circuits and their variations in the fly medulla. Proceedings of the National Academy of Sciences. 2015, 112 (44) 13711-13716. [DOI](https://doi.org/10.1073/pnas.1509820112).
