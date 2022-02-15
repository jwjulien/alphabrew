New Features and Known Bugs
------------------------------------------------------------------------------------------------------------------------
- [ ] Add support (make functional) the mash pH calculations.
- [ ] Add support (make functional) the brewing acid additions.
- [ ] Update the recipe loading to make more robust against bad input files.
    - Supply the user with a warning dialog indicating why loading failed so they can patch it.
- [ ] Convert the Excel database into multiple files (maybe ini or TOML).
    - The monolithic Excel file does not make diffing or merging very easy.  This will be disastrous should the project ever grow beyond a single maintainer.
