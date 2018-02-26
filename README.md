# Compare psnu and site jsons

### install

```bash
pip install pipenv
pipenv install
pipenv shell
```

- drop files into new folder in `data` folder
- naming convention that should exist in both directories: `country_psnu_hts.json` or `country_site_normal` (or variations of it)

example:

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