import os
import sys

import matplotlib as mpl
import mpl_ascii
import numpy as np

from diffusion_model import load_params_from_path, run_diffusion_model

mpl_ascii.AXES_WIDTH = 70
mpl_ascii.AXES_HEIGHT = 15

mpl.use("module://mpl_ascii")

filepath = "diffusion.toml"

if os.path.isfile(filepath):
    params = load_params_from_path(filepath)
else:
    params = {}
concentration = run_diffusion_model(**params)

np.savetxt(sys.stdout, concentration, fmt="%.6f")
