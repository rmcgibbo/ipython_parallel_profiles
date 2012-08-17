import os
import IPython.utils
# Configuration file for ipcluster.

c = get_config()

# delay between controller starting and engine starting
c.IPClusterStart.delay = 1.0 

# set working directory
work_dir = os.path.expanduser('~/ipclusterworkdir')
if not os.path.exists(work_dir):
    os.makedirs(work_dir)
c.IPClusterStart.work_dir = work_dir

# set the default number of engines to be 1
c.IPClusterEngines.n = 1

c.IPClusterStart.daemonize = False

c.IPClusterStart.controller_launcher_class = 'LocalControllerLauncher'
c.IPClusterEngines.engine_launcher_class = 'PBSEngineSetLauncher'

c.LocalControllerLauncher.controller_cmd = ['ipcontroller']

c.PBSEngineSetLauncher.job_id_regexp = '\\d+'
c.PBSEngineSetLauncher.submit_command = ['qsub']
c.PBSEngineSetLauncher.delete_command = ['qdel']

c.PBSEngineSetLauncher.batch_template_file = os.path.join(IPython.utils.path.get_ipython_dir(), 'profile_pbs', 'pbs_engine.template')

c.PBSEngineSetLauncher.queue = u'default'
