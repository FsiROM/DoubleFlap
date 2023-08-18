import KratosMultiphysics as KM
from KratosMultiphysics.CoSimulationApplication.co_simulation_analysis import CoSimulationAnalysis

"""
For user-scripting it is intended that a new class is derived
from CoSimulationAnalysis to do modifications
Check also "kratos/python_scripts/analysis-stage.py" for available methods that can be overridden
"""
import numpy as np
class Specific_w():
    
    def __init__(self,):
        pass
    
    def train(self, dims = None, means = None, stds = None, amazon = None, imported = False):
        
        if imported:
            self.dims = dims
            self.means = means
            self.stds = stds
            self.amazon = amazon
            
    def pred(self, prev_load, prev_disp, dist, dim):
        
        input_array = np.array([1., np.linalg.norm(prev_load), prev_disp, dist]).reshape((1, 4))
        
        which_dim = np.where(self.dims == dim)[0]
        if len(which_dim)>0:
            input_array = (input_array - self.means[:, [which_dim[0]]])/(self.stds[:, [which_dim[0]]])
            pred_w = self.amazon[which_dim[0]].predict(input_array)[0]
            if pred_w < 0.:
                return 0.
            elif pred_w > 1.:
                return 1.
            else:
                return pred_w
        else:
            return 0.2

parameter_file_name = "DoubleFlap_fsi_parameters_ROM.json"
with open(parameter_file_name,'r') as parameter_file:
    parameters = KM.Parameters(parameter_file.read())

simulation = CoSimulationAnalysis(parameters)
simulation.Run()
