from setuptools import setup, find_packages


setup(name='pylendingclub',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')]
      description = 'A Python wrapper for automation of the Lending Club API.',
      author = 'Brandon Barney',
      author_email = 'brandon.barney213@yahoo.com',
      keywords = ['python', 'lendingclub'],
      url = 'https://github.com/bbarney213/PyLendingClub',
      classifiers = [
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']

)
"""
setup(
    name = 'pylendingclub',
    packages = ['pylendingclub'],
    version = 'v3.0.1',  # Ideally should be same as your GitHub release tag version
    description = 'A Python wrapper for the Lending Club API.',
    author = 'Brandon Barney',
    author_email = 'brandon.barney213@yahoo.com',
    url = 'https://github.com/bbarney213/PyLendingClub-Wrapper',
    download_url = 'https://github.com/bbarney213/PyLendingClub-Wrapper/archive/v3.0.1.tar.gz',
    keywords = ['python', 'lendingclub'],
    classifiers = [],
)
"""
