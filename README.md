# Intan RHS Single File Data Loader

`importrhsutilities.py` is renamed to `intanrhsreader.py`.

`COPYING` is renamed to `LICENSE` for clarity.

### To load a single rhs file:

```python
from intanrhsreader import load_file

rhsdata = load_file("<filepath>")
```