import os
from IPython.utils.path import get_ipython_dir

# Configuration file for ipcluster.
c = get_config()
load_subconfig('ipcluster_config.py', profile='pbs_base')

c.PBSEngineSetLauncher.batch_template_file = os.path.join(
    get_ipython_dir(), 'templates', 'pbs.engine.12hr')
