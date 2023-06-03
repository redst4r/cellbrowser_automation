from setuptools import setup, find_packages

setup(name='cellbrowser_automation',
      version='0.1',
      description='Run cellbrowser on multiple datasets, creating a hierachy from a simple .yaml',
      url='http://github.com/redst4r/cellbrowser_automation/',
      author='redst4r',
      maintainer='redst4r',
      maintainer_email='redst4r@web.de',
      license='GNU GPL 3',
      keywords='scrnaseq, scanpy, cellbrowser',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'toolz',
          'h5py',
          'numpy',
          'scipy',
          'scanpy>1.7',
          'sctools @git+https://github.com/redst4r/sctools',
          'pyyaml', 
          ],
      zip_safe=False)
