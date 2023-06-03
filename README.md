# Cellbrowser_automation

This is a convenience tool around the [cellbrowser](https://github.com/maximilianh/cellBrowser) build process for multiple datasets from anndata.AnnData objects via scanpy.
Instead of running cbImport manually on differnt files, just create a `.yaml` file that lays out the hierarchy of the datasets, and this package will built it into a single cellbrowser website.

## Example
### yaml format
There's `datasets` and `collections` (of datasets).
A dataset has
- a title
- a description
- an h5ad file (containing hte actual data
- a config dictionary

A collection is simply a list of datasets, with its own title and description.

Here's an example of a 3 datasets, one on its own, the other two being grouped together:
```yaml
collection:
- config:
    clusterField: leiden
  title: A1
  description: A1 description
  h5ad: /tmp/a1.h5ad
- collection:
  description: A2/A3 collection description
  title: A2A3_collection
  - config: {}
    description: A2 desc
    h5ad: /tmp/a2.h5ad
    title: A2
  - config: {}
    description: ''
    h5ad: /tmp/a3.h5ad
    title: A3
description: basic test with 3 datasets
title: TestingCB
```

### Building it into cellbrowser
```python
from cbautomation import parse_collection
import yaml

with open('some.yaml', 'r') as fh:
    ymal_str = fh.read()
cb_dict = yaml.safe_load(ymal_str)

C = parse_collection(cb_dict, '/tmp')  # specify a tempory directory where cellbrowser stores intermediate results
C.pretty_print()   # to get a nice string representaiton
assert C.check_existance()  # make sure all h5ad paths exist on disk

importdir = '/tmp/CB_import'  # make sure those two directories are empty, cellbrowser gets thrown off by old results
cellbrowser_outfolder = '/tmp/CB_build'
C.do_import(importdir )


C.do_build(
    f'{importdir}/{C.name}',
    f'{importdir}/{C.name}',
    cellbrowser_outfolder
)
```
