from setuptools import setup,find_packages

config = {
    'include_package_data': True,
    'author': 'Avanti Shrikumar',
    'author_email': 'avanti@cs.stanford.edu',
    'url': 'https://github.com/AvantiShri/seqbatchproducers',
    'description': 'Load batches of data for deep learning models trained on sequence data',
    'version': '1.0.0.0',
    'packages': ['seqbatchproducers'],
    'setup_requires': [],
    'install_requires': ['numpy>=1.15','pyBigWig>=0.3.7','pyfaidx'],
    'scripts': [],
    'name': 'seqbatchproducers'
}

if __name__== '__main__':
    setup(**config)
