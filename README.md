# vodf-docs

Documentation source for the *Very-high-energy Open Data Format* (VODF)

The documentation is automatically built at https://vodf.readthedocs.org

## Building Locally:

Set up your environment with *conda* or *mamba*:

``` sh
conda env create -f environment.yaml
conda activate vodf-docs
```

Then build the documentation locally:

```sh
make html
```

results will be in `build/html`, to view them locally use:

``` sh
python -m http.server 8000 --directory build/html
```

and visit http://localhost:8000 with your web browser.
