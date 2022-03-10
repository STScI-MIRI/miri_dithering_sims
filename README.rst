MIRI Imaging Dither and Mosaic Simulations
==========================================

Simulations of MIRI Imaging dither and mosaic simulations.
Used for illustrations for JDox.

In Development!
---------------

Active development.

Contributors
-----------
Karl Gordon

License
-------

This code is licensed under a 3-clause BSD style license (see the
``LICENSE`` file).

Dither Patterns
---------------

Specific dither patterns can be created using a combination of APT and the
miricoord package.

- setup an observation in APT with the desired dither/mosaic pattern
- export the pointing file (File -> Export -> pointing file)
- save to apt_pointing subdirectory
- run `python pointing_to_mirisim.py file.pointings` - this will create the
  mirisim compatible file in the mirisim_dithers subdirectory

These instructions are derived from
https://innerspace.stsci.edu/pages/viewpage.action?spaceKey=JWST&title=Using+MIRISim+to+create+dithered+mosaic+images

Notebooks
---------

- Create_MIRISim_SkyCube_From_FITS.ipynb: Make the needed MIRISim SkyCube from
  an input FITS file.  The FITS files for this notebook are from large IRAC 8um
  and MIPS 24um mosaics of the galaxy M101.  Manual changes to the lines used
  switch between the two files.

- MIRISim_Using_Scene_From_File.ipynb: Run a MIRISim Imager simulation based
  on a SkyCube created using the previous notebook.  Main change is the dither
  pattern.  A number available in mirisim_dithers subdirectory created with
  the above instructions.
