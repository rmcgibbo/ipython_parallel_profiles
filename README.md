ipython_parallel_profiles
=========================

Profiles for IPython.parallel using the PBS engines

Two profiles are provided: pbs1hr, and pbs12hr which submit jobs of 1 and 12 hours in duration. Both profiles use a queue named defaul. They should not be too hard to customize

To install the profiles, use
    python setup.py

To use this profile to start up two engines that will run for 1hr each, for example, use
    ipcluster start --profile=pbs1hr --n 2

More information is available at http://ipython.org/ipython-doc/dev/parallel/parallel_process.html
