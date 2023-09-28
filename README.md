## DoubleFlap

This is the repository for the Double Flap Fluid-Structure Interaction (FSI) simulation files.
This is a test case for the data-driven reduced order modeling approach where a structural Reduced Order Model (ROM) is coupled wih a fluid Full Order Model (FOM).

The FOM simulation is done using [KratosMultiphysics](https://github.com/FsiROM/Kratos).

To reproduce the figures appearing in [1], a Python notebook in `ROMs/ROM-Generation.ipynb`

You can also customize your own solid ROM to use it for the ROM-FOM simulation.


The structural ROM settings can be modified in `/DoubleFlap_fsi_parameters_ROM.json`

You can launch the simulation using `python MainKratos.py`

![Alt Text](Figures/contours.gif)

[1] : A. Tiba, T. Dairay, F. Devuyst, I. Mortazavi, J-P. Berro Ramirez. Non-intrusive reduced order models for partitioned fluid-structure interactions. [arXiv:2306.07570](https://doi.org/10.48550/arXiv.2306.07570), 2023.