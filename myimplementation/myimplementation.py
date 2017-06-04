import c_module
import os, sys

def determine_path ():
    try:
        root = __file__
        if os.path.islink (root):
            root = os.path.realpath (root)
        return os.path.dirname (os.path.abspath (root))
    except:
        print "no root"
        sys.exit ()
        
def run ():
    modret = c_module.c_module_calc_stat()
	print modret
	print determine_path ()
    print "My c module is in:"
    files = [f for f in os.listdir(determine_path () + "/myimplementation/*")]
    print files
    
if __name__ == "__main__":
c_module.c_module_calc_stat()