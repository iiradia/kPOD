from setuptools import setup

setup(
      name='kPOD',
      version='0.1',
      description='Package for kPOD clustering',
      url='http://github.com/iiradia/kPOD',
      author='Ishaan Radia [trl, cre], Jocelyn T. Chi [aut], Eric C. Chi [aut], Richard G. Baraniuk [aut]',
      author_email='iiradia@ncsu.edu',
      license='MIT',
      packages=['kPOD'],
      install_requires = ['pandas', 'numpy', 'scipy'],
      include_package_data = True,
      zip_safe=False
)