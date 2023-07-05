from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()
  
setup(
    name = 'hilbert',
    version = '0.9.4',
    description = 'An infinite dimensional vector module.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    
    author = 'Sebastian Gössl',
    author_email = 'goessl@student.tugraz.at',
    license = 'MIT',
    
    url = 'https://github.com/goessl/hilbert',
    py_modules = ['hilbert'],
    python_requires = '>=3.7',
    install_requires = ['numpy'],
    
    classifiers = [
      'Programming Language :: Python :: 3.7',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent'
    ]
)
