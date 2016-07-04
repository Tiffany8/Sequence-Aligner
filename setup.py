from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
setup(name='SequenceAligner',
      version='0.1-rc11',
      author='T Williams',
      description='FASTA sequence aligner.',
      long_description=readme,
      packages=find_packages(exclude=['tests']),
      entry_points={
          'console_scripts': [
              'aligner = sequence_aligner.main:main'
          ]
      })
