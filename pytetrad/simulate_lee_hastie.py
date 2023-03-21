import jpype.imports

try:
    jpype.startJVM(classpath=[f"resources/tetrad-gui-7.3.0-launch.jar"])
except OSError:
    print("JVM already started")

import tools.simulate as util

## Simulates data with both continuous and discrete columns.
D, G = util.simulateLeeHastie(num_meas=100, samp_size=1000)

# Save data to a file
D.to_csv('../mydata.csv', index=False)

# To save out causal learn graph:
with open('../mygraph.txt', 'w') as f:
    f.write(str(G))
