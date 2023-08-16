# FlyBrainLab Datasets
This repository contains information regarding the FlyBrainLab Datasets (version, source, loading scripts, etc.)
Here, we provide a summary of the datasets available under NeuroArch database, and links to the preloaded database backup files that can be used to restored the databases.
Detailed instructions for loading these databases from scratch are provided in the individual folders and/or notebooks.

[FlyCircuit](#flycircuit) | [Hemibrain](#hemibrain) | [Larva L1EM](#larva-l1em) | [Medulla 7 Column](#medulla-7column) | [MANC](#MANC) | [FlyWire](#FlyWire) | [FIB19 Optic Lobe](FIB19)

## <a name="flycircuit"></a>[FlyCircuit Dataset](http://flycircuit.tw) [[1]](#ref-1)

|FlyCircuit Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|-----|------|
| 1.2 | [0414129](https://github.com/fruitflybrain/neuroarch/tree/041412911379a5d36ea0c9ca5cb1e7931c596ab5) | [flycircuit1.2_na_v2.0.1_backup.zip](https://drive.google.com/file/d/1_T-aAqGXh-spuFCWomnEzYnw6WyWUSjq/view?usp=sharing) | [Link](https://github.com/FlyBrainLab/datasets/blob/main/flycircuit/v1.2/FlyCircuit_to_NeuroArch.ipynb) | 06/17/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/flycircuit/v1.2/README.md) |[Link](https://neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/flycircuit admin admin; restore database /path/to/flycircuit1.2_na_v2.0.1_backup.zip"
```

## <a name="hemibrain"></a>[Hemibrain Dataset](https://www.janelia.org/project-team/flyem/hemibrain) [[2]](#ref-2)
Original data licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

|Hemibrain Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|-------|
| [1.0.1](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.0.1_neo4j_inputs.zip) | [73d6b81](https://github.com/fruitflybrain/neuroarch/tree/73d6b81439b870d5b5c1de73df4f20283045b7fa) | [hemibrain1.0.1_na_v1.0_backup.zip](https://drive.google.com/file/d/1x6MQJB_4OaWJR6d6O3WFCSeJWG58FsPT/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.0.1/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 01/27/2021 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.0.1/README.md)| [Link](https://hemibrain101.neuronlp.fruitflybrain.org)|
| [1.1](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.1_neo4j_inputs.zip) | [73d6b81](https://github.com/fruitflybrain/neuroarch/tree/73d6b81439b870d5b5c1de73df4f20283045b7fa) | [hemibrain1.1_na_v1.0_backup.zip](https://drive.google.com/file/d/1Y63UpypJ-eMgOdX3bcSRO4Ct3DqmH6-X/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.1/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 01/27/2021 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.1/README.md)| [Link](https://hemibrain.neuronlp.fruitflybrain.org)|
| [1.2](https://storage.cloud.google.com/hemibrain-release/neuprint/hemibrain_v1.2_neo4j_inputs.zip) | [0414129](https://github.com/fruitflybrain/neuroarch/tree/041412911379a5d36ea0c9ca5cb1e7931c596ab5) | [hemibrain1.2_na_v2.0.1_backup.zip](https://drive.google.com/file/d/1ytVmmLrYqKARw9-0tVGJvQzCIzCLUtaN/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.2/Hemibrain_Neuprint_to_NeuroArch.ipynb) | 06/17/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/hemibrain/v1.2/README.md)| [Link](https://hemibrain12.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/hemibrain admin admin; restore database /path/to/hemibrain1.2_na_v2.0.1_backup.zip"
```

## <a name="larva-l1em"></a>[Larva L1EM](https://l1em.catmaid.virtualflybrain.org/) [[3]](#ref-3)
Original data licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

|L1EM Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [1.0](https://l1em.catmaid.virtualflybrain.org/) | [0414129](https://github.com/fruitflybrain/neuroarch/tree/041412911379a5d36ea0c9ca5cb1e7931c596ab5) | [l1em1.0_na_v2.0.1_backup.zip](https://drive.google.com/file/d/1juF2aSp5g-c9S3U3RD9_ydSsDpHaHuLC/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/l1em/Load_Larva_L1EM.ipynb) | 06/17/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/l1em/README.md)| [Link](https://larva.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/l1em admin admin; restore database /path/to/l1em1.0_na_v2.0.1_backup.zip"
```

## <a name="medulla-7column"></a>[Medulla 7 Column Dataset](https://www.janelia.org/project-team/flyem/research/previous-connectomes-analyzed/seven-column-connectome-fib-sem) [[4]](#ref-medulla)
Original data licensed under [BSD 3](https://github.com/connectome-neuprint/neuPrint/blob/master/LICENSE.txt). Neuron Skeleton data from [ConnectomeHackathon2015](https://github.com/janelia-flyem/ConnectomeHackathon2015) and is licensed under the [Open Data Commons Attribution License](http://opendatacommons.org/licenses/by/1.0/).

|Medulla Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [fib25](https://github.com/connectome-neuprint/neuPrint/blob/master/fib25_neo4j_inputs.zip/) | [0414129](https://github.com/fruitflybrain/neuroarch/tree/041412911379a5d36ea0c9ca5cb1e7931c596ab5) | [medulla7column_fib25_na_v2.0.2_backup.zip](https://drive.google.com/file/d/1yc929e0fRIcWER5fL1y_z707cNEbV-ti/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/medulla/Medulla7column_Neuprint_to_NeuroArch.ipynb) | 07/06/2022 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/medulla/README.md)| [Link](https://medulla.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/medulla admin admin; restore database /path/to/medulla7column_fib25_na_v2.0.2_backup.zip"
```

## <a name="MANC"></a>[Male Adult Nerv Cord Dataset](https://www.janelia.org/project-team/flyem/manc-connectome) [[5]](#ref-manc)
Original data licensed under [CC-BY](https://creativecommons.org/licenses/by/4.0/).

|MANC Ver.| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [1.0](https://storage.googleapis.com/flyem-manc-exports/v1.0/neuprint_manc_v1.0/neuprint_manc_v1.0_csv.tar.gz) | [1126f43](https://github.com/fruitflybrain/neuroarch/tree/1126f4382b4d1c14dbf0509947b4e9a2da9b2c45) | [manc1.0_na_v1.0.0_backup.zip](https://drive.google.com/file/d/15MgSmFMFl_vUtS32rVpb0E7HKpJAQe8v/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/manc/v1.0/MANC_Neuprint_to_NeuroArch.ipynb) | 08/16/2023 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/manc/v1.0/README.md)| [Link](https://manc.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/manc admin admin; restore database /path/to/manc1.0_na_v1.0.0_backup.zip"
```

## <a name="FlyWire"></a>[FlyWire Dataset](https://flywire.ai) [[6]](#ref-flywire)
Original data licensed under [CC-BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).

|FlyWire Snapshot| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [630](https://codex.flywire.ai/api/download) | [1126f43](https://github.com/fruitflybrain/neuroarch/tree/1126f4382b4d1c14dbf0509947b4e9a2da9b2c45) | [flywire630_na_v1.0.0_backup.zip](https://drive.google.com/file/d/1S_6qRe7lBIC8vzZvsFAM59ScaMVwx7as/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/flywire/snapshot630/FlyWire_to_NeuroArch.ipynb) | 08/16/2023 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/flywire/snapshot630/README.md)| [Link](https://flywire.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/flywire admin admin; restore database /path/to/flywire630_na_v1.0.0_backup.zip"
```

## <a name="FIB19"></a>[FIB19 Optic Lobe Dataset](https://flywire.ai) [[7]](#ref-fib19)
Original data licensed under [CC-BY](https://creativecommons.org/licenses/by/4.0/).

|FlyWire Snapshot| NeuroArch Ver.| Download Link |Loading Script|Last Update|NeuroNLP|
|-----------|---------| --------| -------|------|--------|
| [1.0](https://neuprint.janelia.org/?dataset=fib19%3Av1.0&qt=findneurons) | [1126f43](https://github.com/fruitflybrain/neuroarch/tree/1126f4382b4d1c14dbf0509947b4e9a2da9b2c45) | [fib19_1.0_na_v1.0.0_backup.zip](https://drive.google.com/file/d/11TJlrASgf6HlhLNrnoAZ8trd8cbcToOM/view?usp=sharing)| [Link](https://github.com/FlyBrainLab/datasets/blob/main/fib19/v1.0/FIB19_to_NeuroArch.ipynb) | 08/16/2023 [Release Notes](https://github.com/FlyBrainLab/datasets/blob/main/fib19/v1.0/README.md)| [Link](https://opticlobe.neuronlp.fruitflybrain.org)|

To load the database in OrientDB, use the following command (and replace `/path/to` in two places to the directory of the orientdb and the downloaded zip file, respectively):

```bash
/path/to/orientdb/bin/console.sh "create database plocal:../databases/fib19 admin admin; restore database /path/to/fib19_1.0_na_v1.0.0_backup.zip"
```



## References

1. <a name="ref-1"></a> Ann-Shyn Chiang et al., Three-dimensional reconstruction of brain-wide wiring networks in Drosophila at single-cell resolution, Current Biology 2011, 21(1), pp.1-11. [DOI](https://doi.org/10.1016/j.cub.2010.11.056).
2. <a name="ref-2"></a> Louis K. Scheffer et al., A connectome and analysis of the adult *Drosophila* central brain. eLife 2020;9:e57443. [DOI](https://doi.org/10.7554/eLife.57443).
3. <a name="ref-3"></a> Ohyama T. et al., A multilevel multimodal circuit enhances action selection in Drosophila. Nature. 2015. [DOI](https://doi.org/10.1038/nature14297).
4. <a name="ref-medulla"></a> Takemura S. et al., Synaptic circuits and their variations in the fly medulla. Proceedings of the National Academy of Sciences. 2015, 112 (44) 13711-13716. [DOI](https://doi.org/10.1073/pnas.1509820112).
5. <a name="ref-manc"></a> Shin-ya Takemura et al., A Connectome of the Male Drosophila Ventral Nerve Cord
bioRxiv, 2023.06.05.543757, 2023. [DOI](https://doi.org/10.1101/2023.06.05.543757).
6. <a name="ref-flywire"></a> Sven Dorkenwald et al., Neuronal wiring diagram of an adult brain
bioRxiv 2023.06.27.546656, 2023 [DOI](https://doi.org/10.1101/2023.06.27.546656).
7. <a name="ref-fib19"></a> Kazunori Shinomiya et al., Comparisons between the ON- and OFF-edge motion pathways in the Drosophila brain. eLife 8:e40025, 2019. [DOI](https://doi.org/10.7554/eLife.40025).

