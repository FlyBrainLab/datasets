# FlyBrainLab Datasets
This repository contains information regarding the FlyBrainLab Datasets (version, source, loading scripts, etc.)
Here, we provide a summary of the datasets available under NeuroArch database, and links to the preloaded database backup files that can be used to restored the databases.
Detailed instructions for loading these databases from scratch are provided in the individual folders and/or notebooks.

[FlyCircuit](#flycircuit) | [Hemibrain](#hemibrain) | [Larva L1EM](#larva-l1em) | [Medulla 7 Column](#medulla-7column)

## <a name="flycircuit"></a>[FlyCircuit Dataset](http://flycircuit.tw) [[1]](#ref-1)

|FlyCircuit Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|-----|------|
| 1.2 | [dec5b7e](https://github.com/fruitflybrain/neuroarch/tree/dec5b7e76a283f0677dc7454496b684125f2b8ea) | [flycircuit1.2_na_v2.0_backup.zip](https://drive.google.com/file/d/1WjKAvYazxE-shmvzo_B1OC-7zvAbfMW4/view?usp=sharing) | [Link](https://github.com/FlyBrainLab/datasets/blob/main/flycircuit/v1.2/FlyCircuit_to_NeuroArch.ipynb) | 06/09/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/flycircuit/v1.2/README.md) |[Link](https://neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):
```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/flycircuit admin admin; restore database /path/to/flycircuit1.2_na_v1.0_backup.zip"
```

## <a name="hemibrain"></a>[Hemibrain Dataset](https://www.janelia.org/project-team/flyem/hemibrain) [[2]](#ref-2)
Original data licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

|Hemibrain Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|-------|
| [1.0.1](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.0.1_neo4j_inputs.zip) | [73d6b81](https://github.com/fruitflybrain/neuroarch/tree/73d6b81439b870d5b5c1de73df4f20283045b7fa) | [hemibrain1.0.1_na_v1.0_backup.zip](https://drive.google.com/file/d/1x6MQJB_4OaWJR6d6O3WFCSeJWG58FsPT/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.0.1/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 01/27/2021 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.0.1/README.md)| [Link](https://hemibrain101.neuronlp.fruitflybrain.org)|
| [1.1](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.1_neo4j_inputs.zip) | [73d6b81](https://github.com/fruitflybrain/neuroarch/tree/73d6b81439b870d5b5c1de73df4f20283045b7fa) | [hemibrain1.1_na_v1.0_backup.zip](https://drive.google.com/file/d/1Y63UpypJ-eMgOdX3bcSRO4Ct3DqmH6-X/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.1/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 01/27/2021 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.1/README.md)| [Link](https://hemibrain.neuronlp.fruitflybrain.org)|
| [1.2](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.2_neo4j_inputs.zip) | [dec5b7e](https://github.com/fruitflybrain/neuroarch/tree/dec5b7e76a283f0677dc7454496b684125f2b8ea) | [hemibrain1.2_na_v2.0_backup.zip](https://drive.google.com/file/d/1jLTNkvIyJhGv3xZZAClzY1R8neLCsh8H/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.2/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 06/09/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.2/README.md)| [Link](https://hemibrain12.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):
```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/hemibrain admin admin; restore database /path/to/hemibrain1.1_na_v1.0_backup.zip"
```

## <a name="larva-l1em"></a>[Larva L1EM](https://l1em.catmaid.virtualflybrain.org/) [[3]](#ref-3)
Original data licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

|L1EM Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [1.0](https://l1em.catmaid.virtualflybrain.org/) | [dec5b7e](https://github.com/fruitflybrain/neuroarch/tree/dec5b7e76a283f0677dc7454496b684125f2b8ea) | [l1em1.0_na_v2.0_backup.zip](https://drive.google.com/file/d/1tcORsE8QVxwuCRQviVsoN11Mjs3Dq_24/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/l1em/Load_Larva_L1EM.ipynb) | 06/09/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/l1em/README.md)| [Link](https://larva.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):
```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/l1em admin admin; restore database /path/to/l1em1.0_na_v1.0_backup.zip"
```

## <a name="medulla-7column"></a>[Medulla 7 Column Dataset](https://www.janelia.org/project-team/flyem/research/previous-connectomes-analyzed/seven-column-connectome-fib-sem) [[4]](#ref-medulla)
Original data licensed under [BSD 3](https://github.com/connectome-neuprint/neuPrint/blob/master/LICENSE.txt). Neuron Skeleton data from [ConnectomeHackathon2015](https://github.com/janelia-flyem/ConnectomeHackathon2015) and is licensed under the [Open Data Commons Attribution License](http://opendatacommons.org/licenses/by/1.0/).

|Medulla Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [fib25](https://github.com/connectome-neuprint/neuPrint/blob/master/fib25_neo4j_inputs.zip/) | [dec5b7e](https://github.com/fruitflybrain/neuroarch/tree/dec5b7e76a283f0677dc7454496b684125f2b8ea) | [medulla7column_fib25_na_v2.0_backup.zip](https://drive.google.com/file/d/1S5dupAC_uFzgBKDqL5OdUXWBQKZPXvvz/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/medulla/Medulla7column_Neuprint_to_NeuroArch.ipynb) | 06/09/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/medulla/README.md)| [Link](https://medulla.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):
```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/medulla admin admin; restore database /path/to/medulla7column_fib25_na_v1.0_backup.zip"
```


## References
1. <a name="ref-1"></a> Ann-Shyn Chiang et al., Three-dimensional reconstruction of brain-wide wiring networks in Drosophila at single-cell resolution, Current Biology 2011, 21(1), pp.1-11. [DOI](https://doi.org/10.1016/j.cub.2010.11.056).
2. <a name="ref-2"></a> Louis K. Scheffer et al., A connectome and analysis of the adult *Drosophila* central brain. eLife 2020;9:e57443. [DOI](https://doi.org/10.7554/eLife.57443).
3. <a name="ref-3"></a> Ohyama T. et al. A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
4. <a name="ref-medulla"></a> Takemura S. et al. Synaptic circuits and their variations in the fly medulla. Proceedings of the National Academy of Sciences. 2015, 112 (44) 13711-13716. [DOI](https://doi.org/10.1073/pnas.1509820112).
