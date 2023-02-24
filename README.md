# Intan RHS Single File Data Loader


### Intall the package directly from this repo by running:

```bash
pip install git+https://github.com/datajoint/intanrhsreader.git
```


### To load a single rhs file:

```python
from intanrhsreader import load_file

rhsdata = load_file("<filepath>")
```