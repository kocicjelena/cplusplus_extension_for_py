Build and test the module


> python setup.py install
import c_module
c_module.c_module_calc_stat()


test:
python setup.py test

reference: https://docs.python.org/3.6/install/index.html
Creating a Source Distribution:
python setup.py sdist
Creating Built Distributions::
python setup.py bdist
Creating RPM packages:
python setup.py bdist_rpm
python setup.py bdist_wininst
or the bdist command with the --formats option:
windows:
python setup.py bdist --formats=wininst
64bit version of your extension:
python setup.py build --plat-name=win-amd64
The Windows Installers also::
python setup.py build --plat-name=win-amd64 bdist_wininst


