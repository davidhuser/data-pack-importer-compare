# Compare psnu and site jsons

### Install

```bash
pip install pipenv
git clone <this repo>
cd <this repo>
pipenv install
```

### Usage

```bash
pipenv shell
python compare.py --folder1 data/v1 --folder2 data/v2 --country swazi
```

Outputs a CSV file showing the difference between each file.
Uses `pandas` DataFrame and applying a merge and outer join.

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