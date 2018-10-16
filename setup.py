from distutils.core import setup


setup(name='pylendingclub',
      packages = ['pylendingclub'],
      description = 'A Python wrapper for automation of the Lending Club API.',
      author = 'Brandon Barney',
      author_email = 'brandon.barney213@yahoo.com',
      keywords = ['python', 'lendingclub'],
      url = 'https://github.com/bbarney213/PyLendingClub',
      classifiers = [],
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
