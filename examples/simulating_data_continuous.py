import os
import sys

# this needs to happen before import pytetrad (otherwise lib cant be found)
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(BASE_DIR)

# For large simulations if you have enough RAM...
# import jpype
# import jpype.imports
#
# jpype.startJVM("-Xmx40g", classpath=[f"{BASE_DIR}/tetrad-gui-7.2.2-launch.jar"])

# Otherwise...
from pytetrad.util import startJVM
startJVM()

from edu.cmu.tetrad.util import Params, Parameters
import edu.cmu.tetrad.algcomparison.simulation as sim
import edu.cmu.tetrad.algcomparison.graph as graph
import pytetrad.translate as tr

# An easy way to simulate data in Tetrad is to use the algorithm comparison tool.
# Here's an example.

# Set the parameters for the simulation
params = Parameters()

params.set(Params.SAMPLE_SIZE, 500)
params.set(Params.NUM_MEASURES, 20)
params.set(Params.AVG_DEGREE, 6)
params.set(Params.NUM_LATENTS, 8)
params.set(Params.RANDOMIZE_COLUMNS, True)
params.set(Params.COEF_LOW, 0)
params.set(Params.COEF_HIGH, 1)
params.set(Params.VAR_LOW, 1)
params.set(Params.VAR_HIGH, 3)
params.set(Params.VERBOSE, False)
params.set(Params.NUM_RUNS, 1)
# params.set(Params.SEED, 29483)

# Do the simulation and grab the dataset and generative graph
sim_ = sim.LinearFisherModel(graph.RandomForward())
sim_.createData(params, True)
data_model = sim_.getDataModel(0)
graph = sim_.getTrueGraph(0)

#Save data to a file
df = tr.tetrad_to_pandas(data_model)
df.to_csv('../mydata.csv', index=False)

# To save out causal learn graph:
gr = tr.tetrad_graph_to_causal_learn(graph)
with open('../mygraph.txt', 'w') as f:
    f.write(str(gr))

# To save out in PCALG format:
gr = tr.tetrad_graph_to_pcalg(graph)
gr.to_csv('../mygraph.csv', index=False)



