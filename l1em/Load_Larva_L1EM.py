#!/usr/bin/env python
# coding: utf-8
'''Script for Loading Larva Dataset
'''
import neuroarch.na as na
import pandas as pd
from tqdm import tqdm
import numpy as np
import os
import argparse

DIR = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='Loading Larva L1EM Dataset')

parser.add_argument('--base_dir', '-bd', default=DIR, type=str,
                    help='Base directory that contains all files. Default to where this file is.')
parser.add_argument('--mode', '-m', default='o', type=str, choices=['o', 'w', 'r'],
                    help='Overwrite (o), Write (w) or Read (r) Database.')
parser.add_argument('--swc_dir', '-sdir', default='swc', type=str,
                    help='Relative path of SWC files from Base Dir')
parser.add_argument('--mesh_dir', '-mdir', default='meshes', type=str,
                    help='Rleative path of Mesh files')
parser.add_argument('--db_name', '-n', default='l1em', type=str,
                    help='Name of Database')
parser.add_argument('--db_ver', '-v', default='1.0', type=str,
                    help='Version of L1EM Dataset')
args = parser.parse_args()

BASE_DIR = args.base_dir
SWC_DIR = os.path.join(BASE_DIR, args.swc_dir)
MESH_DIR = os.path.join(BASE_DIR, args.mesh_dir)
NEURON_FNAME = os.path.join(BASE_DIR,'neurons_published_2020_12_04.csv')
SYNAPSE_FNAME = os.path.join(BASE_DIR, 'connectors_published.csv')

neuron_df = pd.read_csv(NEURON_FNAME, index_col=0)
synapse_df = pd.read_csv(SYNAPSE_FNAME, index_col=0)

# Check all files exist
assert os.path.exists(NEURON_FNAME), 'Neuron File Not Found.'
assert os.path.exists(SYNAPSE_FNAME), 'Synapse File Not Found.'
assert os.path.isdir(SWC_DIR), 'SWC Directory Not Found.'
assert os.path.isdir(MESH_DIR), 'MESH Directory Not Found.'
assert len(neuron_df) == len(os.listdir(SWC_DIR)), \
    'There are {} swc files in path {}, expect {} from the neuron file'.format(
        len(os.listdir(SWC_DIR)), SWC_DIR, len(neuron_df)
    )

# setup systems
cns = {
    'System': 'CNS',
    'synonyms': ['larva CNS', 'cns'],
    'morphology': {'type':'mesh', 'filename': os.path.join(MESH_DIR, 'CNS_um.json')}
}
neuropils = {
    'AL':{
        'System':'CNS',
        'Neuropil':'AL',
        'synonyms':['right antennal lobe','antennal lobe','al_r','al','right al'],
        'morphology': os.path.join(MESH_DIR, 'AL_um.json')
    },
    'al':{
        'System':'CNS',
        'Neuropil':'al',
        'synonyms':['left antennal lobe','antennal lobe','al_l','al','left al'],
        'morphology': os.path.join(MESH_DIR, 'AL_um.json')
    },
    'MB':{
        'System':'CNS',
        'Neuropil':'MB',
        'synonyms':['right mushroom body','mushroom body','right mb','mb_r','mb'],
        'morphology': os.path.join(MESH_DIR, 'MB_um.json')
    },
    'mb':{
        'System':'CNS',
        'Neuropil':'mb',
        'synonyms':['left mushroom body','mushroom body','left mb','mb_l','mb'],
        'morphology': os.path.join(MESH_DIR, 'MB_um.json')
    },
    'LON':{
        'System':'CNS',
        'Neuropil':'LON',
        'synonyms':['right larva optic neuropil','optic neuropil','right lon','lon_r','lon']
    },
    'lon':{
        'System':'CNS',
        'Neuropil':'lon',
        'synonyms':['left larva optic neuropil','optic neuropil','left lon','lon_f','lon']
    },
    'LH':{
        'System':'CNS',
        'Neuropil':'LH',
        'synonyms':['right lateral horn','lateral horn','right lh','lh']
    },
    'lh':{
        'System':'CNS',
        'Neuropil':'lh',
        'synonyms':['left lateral horn','lateral horn','left lh','lh']
    },
    'unknown':{
        'System':'CNS',
        'Neuropil':'unknown',
        'synonyms': ['left unknown', 'left unspecified', 'unspecified', 'na', 'unknown']
    },
    'UNKNOWN':{
        'System':'CNS',
        'Neuropil':'UNKNOWN',
        'synonyms': ['right unknown', 'right unspecified', 'unspecified', 'na', 'unknown']
    },
    'vnc':{
        'System':'CNS',
        'Neuropil':'vnc',
        'synonyms': ['left vnc', 'left ventral nerve cord', 'left ventral nerve', 'ventral nerve cord', 'vnc']
    },
    'VNC':{
        'System':'CNS',
        'Neuropil':'VNC',
        'synonyms': ['right vnc', 'right ventral nerve cord', 'left ventral nerve', 'ventral nerve cord', 'vnc']
    },
    'sez':{
        'System':'CNS',
        'Neuropil':'sez',
        'synonyms': ['left sez', 'left subesophageal zone', 'left subesophageal', 'subesophageal', 'sez']
    },
    'SEZ':{
        'System':'CNS',
        'Neuropil':'SEZ',
        'synonyms': ['right sez', 'right subesophageal zone', 'right subesophageal', 'subesophageal', 'sez']
    },
}


# In[9]:


neuron_synonyms = {
    'PR': ['PR', 'photoreceptor'],
    'PN': ['PN', 'Projection Neuron'],
    'uPN': ['upn', 'Uni PN', 'uni-PN', 'uniglomeruluar projection neuron', 'uniglomerular pn'],
    'mPN': ['mpn', 'Multi PN', 'multi-PN', 'multi Projection Neuron', 'Multi Projection Neuron', 'Multiglomeruli PN', 'Multiglomeruli Projection Neuron'],
    'OSN': ['OSN', 'ORN', 'Olfactory Receptor Neuron', 'Olfactory Sensory Neuron'],
    'KC': ['kc', 'kenyon cell'],
    'MBON': ['mbon', 'mushroom body output neuron', 'Output Neuron'],
    'MBIN': ['mbin', 'mushroom body input neuron', 'mbin'],
    'DAN': ['dan', 'Dopaminergic Neuron'],
    'OAN': ['oan', 'Octopaminergic Neuron'],
    'LHN': ['lhn', 'lateral horn neuron'],
    'LHON': ['lhon', 'lateral horn output neuron'],
    'CN': ['cn', 'convergence neuron'],
    'MB2ON': ['mb2on'],
    'VPN': ['vpn', 'visual projection neuron'],
    'LN': ['ln', 'antennal lobe local neuron'],
    'Motor': ['motor', 'motor neuron'],
    'PMN': ['pmn', 'premotor neuron', 'pre-motor neuron'],
    'APL': ['apl', 'anterior posterior lateral'],
    'FFN': ['ffn', 'feedforward neuron'],
    'FBN': ['fbn', 'feedback neuron'],
    'FAN': ['fan', 'feedacross neuron']
}

l1em = na.NeuroArch('localhost', args.db_name, mode = args.mode)

species = l1em.add_species('Drosophila Melanogaster', stage = 'larva',
                                sex = 'female',
                                synonyms = ['larva fruit fly'])

version = args.db_ver
datasource = l1em.add_DataSource('L1EM', version = version,
                                 url = 'https://l1em.catmaid.virtualflybrain.org/',
                                 species = species)
l1em.default_DataSource = datasource

cns = l1em.add_Subsystem(cns['System'], synonyms=cns['synonyms'], morphology=cns['morphology'])

for k, v in neuropils.items():
    if 'morphology' in v:
        l1em.add_Neuropil(k,
                           morphology = {'type': 'mesh', 'filename': v['morphology']},
                           subsystem = v['System']
        )
    else:
        l1em.add_Neuropil(k,
                   subsystem = v['System']
        )


'''Load Neurons

The `neuron_df` dataframe contains a list of neurons of the following fields:

1. `uname`: globally unique name in the database
2. `label`: display name of the neuron. Follows `neuron_type-index` structure whenever possible. When `neuron_type` is not characterized by the FlyBrainLab developers, we follow the `catmaid_names` for the label
3. `catmaid_names`: names of the neuron in the catmaid database
4. `type`: neuron type
5. `side`: left/right side of the brain. Bilateral neurons are not currently handled by the database and are assumed as left by default.
6. `neurotransmitter`: neurotransmiter information of the neuron whenever available.
7. `locality`: whether a neuron is `input` to or `output` from or `local` to the associated `neuropil`
8. `neuropil`: name of neuropil that neuron is associated with
9. `source`: publication where data is originally released
10. `skid`: skeleton id, the identifier in catmaid database for neuron skeletons
'''
pbar = tqdm(neuron_df.iterrows(), desc='Loading Neurons', total=neuron_df.shape[0])
for i, row in pbar:
    bodyID = row['skid']
    cell_type = row['type']
    uname = row['uname']
    name = row['label']

    info = {
        'source': row.source,
    }

    if row.catmaid_names != 'unknown':
        info['catmaid_name'] = row.catmaid_names


    neuropils = row['neuropil'].split(',')
    if row.neuropil != 'unknown':
        npl = neuropils[0].lower() if row.side.lower() == 'left' else neuropils[0].upper()
        arborization = {
            'type': 'neuropil',
             'dendrites': {npl: 1},
             'axons': {}
        }
    else:
        arborization = None
    l1em.add_Neuron(uname, # uname
                     name, # name
                     locality=True if row.locality == 'local' else False,
                     synonyms=neuron_synonyms[cell_type] if cell_type in neuron_synonyms else None,
                     neurotransmitters=row.neurotransmitter if row.neurotransmitter != 'unknown' else None,
                     referenceId = str(bodyID), #referenceId
                     info = info if len(info) else None,
                     morphology = {'type': 'swc', 'filename': os.path.join(SWC_DIR, '{}.swc'.format(bodyID)), 'scale': 1.},
                     arborization = arborization)
pbar.close()

# find all the neurons so they can be keyed by their referenceId.
neurons = l1em.sql_query('select from Neuron').nodes_as_objs
# set the cache so there is no need for database access.
for neuron in neurons:
    l1em.set('Neuron', neuron.uname, neuron, l1em.default_DataSource)
neuron_ref_to_obj = {int(neuron.referenceId): neuron for neuron in neurons}


'''Load synapses

The `synapse_df` dataframe contains a list of neurons of the following fields:

1. `N`: number of synapses
2. `presynaptic`: `uname` of presynaptic neuron
3. `postsynaptic`: `uname` of postsynaptic neuron
4. `pre_skid`: `skid` of presynaptic neuron
5. `post_skid`: `skid` of postsynaptic neuron
6. `uname`: uname of the synapse that follows the `presynaptic--postsynaptic` structure.
7. `x`: list of `x`-coordinates for synapse locations
8. `y`: list of `y`-coordinates for synapse locations
9. `z`: list of `z`-coordinates for synapse locations
10. `r`: list of radius of synapses. If `0`, the minimum size as specified in the `Neu3D` renderer is used when the synapses are rendered
'''
pbar = tqdm(synapse_df.iterrows(), total=synapse_df.shape[0], desc='Loading Synapses')
for i, row in pbar:
    pre_neuron = neuron_ref_to_obj[row['pre_skid']]
    post_neuron = neuron_ref_to_obj[row['post_skid']]

    x = eval(row['x'].replace('\n', '').replace('  ', ' ').replace(', ', ',').replace(' ', ','))
    y = eval(row['y'].replace('\n', '').replace('  ', ' ').replace(', ', ',').replace(' ', ','))
    z = eval(row['z'].replace('\n', '').replace('  ', ' ').replace(', ', ',').replace(' ', ','))
    r = eval(row['r'].replace('\n', '').replace('  ', ' ').replace(', ', ',').replace(' ', ','))

    content = {'type': 'swc'}
    content['x'] = [round(i, 3) for i in np.array(x+x)/1000.] # conver from nm to um
    content['y'] = [round(i, 3) for i in np.array(y+y)/1000.] # conver from nm to um
    content['z'] = [round(i, 3) for i in np.array(z+z)/1000.] # conver from nm to um
    content['r'] = [round(i, 3) for i in np.array(r+r)/1000.] # conver from nm to um
    content['parent'] = [-1]*len(x) + [i+1 for i in range(len(x))]
    content['identifier'] = [7]*len(x) + [8]*len(x)
    content['sample'] = [i+1 for i in range(len(content['x']))]
    l1em.add_Synapse(pre_neuron, post_neuron, N = row['N'],
                      morphology = content)
pbar.close()
