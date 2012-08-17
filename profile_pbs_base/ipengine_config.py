from IPython.utils.path import expand_path

c = get_config()

# set working directory
work_dir = expand_path('~/ipclusterworkdir')
if not os.path.exists(work_dir):
    os.makedirs(work_dir)
c.IPClusterStart.work_dir = work_dir
