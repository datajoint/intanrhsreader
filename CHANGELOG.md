# Changelog

Observes [Semantic Versioning](https://semver.org/spec/v2.0.0.html) standard and
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/) convention.


## [1.0.0] - 2023-02-17
- Update - Rename `COPYING` to `LICENSE`
- Update - Remove `LoadIntanRHS_Python.ipynb`
- Update - Rename `importrhsutilities.py` to `intanrhsreader.py`
- Update - Black format `intanrhsreader.py`
- Update - In `intanrhsreader.py` and the `load_file` function, remove the `data_present` variable from the return statement
- Add - In `intanrhsreader.py` and the `data_to_result` function, add header information to the `result` dictionary