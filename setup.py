from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
setup(name='SequenceAligner',
      version='0.0.1',
      author='T Williams',
      author_email='trw.visions@gmail.com',
      description='FASTA sequence aligner.',
      url='https://github.com/Tiffany8/Sequence-Aligner',
      long_description=readme,
      packages=find_packages(exclude=['tests']),
      entry_points={
          'console_scripts': [
              'aligner = sequence_aligner.main:main'
          ]
      })
