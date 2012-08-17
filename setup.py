import os
import glob
from IPython.utils.path import get_ipython_dir


def link(src, dest):
    src = os.path.abspath(src)
    dest = os.path.abspath(dest)
    
    if os.path.exists(dest):
        if os.path.islink(dest):
            if os.path.abspath(os.readlink(dest)) == src:
                print 'Link already in place: %s' % src
                return
        
        backup = dest + '.backup.' + strftime("%Y.%m.%d")
        print 'Backing up current copy to %s' % backup
        if os.path.exists(backup): raise Exception('Backup already exists')
        os.rename(dest, backup)
    
    print 'Softlinking %s to %s' % (src, dest)
    os.symlink(src, dest)

def main():
    links_to_make = glob.glob('profile_*')
    links_to_make.append('templates')
    for d in links_to_make:
        link(d, os.path.join(get_ipython_dir(), d))
    
    

if __name__ == '__main__':
    main()
