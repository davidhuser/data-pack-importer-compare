# Compare psnu and site jsons

[![Build Status](https://travis-ci.org/davidhuser/data-pack-importer-compare.svg?branch=master)](https://travis-ci.org/davidhuser/data-pack-importer-compare)

### Install

```bash
pip install dpi-compare --user
```

### Usage

```bash
dpi-compare --help

Compare data JSONs in folders

arguments:
  -h, --help           show this help message and exit
  --folder1 FOLDER1    File path of first folder
  --folder2 FOLDER2    File path of second folder
  --country COUNTRY    Country string, e.g. "nigeria"
  --level              Level, either "psnu" or "site"
  --type               Type, either "normal" or "hts"
```

e.g.

```bash
dpi-compare --folder1 data/v1 --folder2 data/v2 --country swazi --level psnu --type normal
```

Outputs a CSV file showing the difference between each file.
Uses a `pandas` DataFrame and applying a _merge_ and _outer join_.

#### Example folder structure

```
data/
├── v1/
│   ├── swazi_psnu_hts.json
│   ├── swazi_psnu_normal.json
│   ├── swazi_site_hts.json
│   └── swazi_site_normal.json
└── v2/
    ├── swazi_psnu_hts.json
    ├── swazi_psnu_normal.json
    ├── swazi_site_hts.json
    └── swazi_site_normal.json
```

#### Naming convention

Files within a directory must have a matching file in the other directory.

`<country>_{psnu|site}_{hts|normal}.json`


### R script to generate those JSONs

See [data-pack-importer](https://github.com/jason-p-pickering/data-pack-importer)

## Develop

```bash
pip install pipenv
git clone <this repo>
cd <this repo>
pipenv install --dev
```

## Tests
```
python setup.py test
```
