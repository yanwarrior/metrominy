from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='metrominy',
      version='0.1',
      description='metrominy is a package that implements the method term frequency and inverse document '
                'frequency for weighting collection of documents by providing value to the cosine '
                'similarity search results of a search query.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Indexing',
      ],
      keywords='text mining preprocessing term frequency tf inverse document frequency idf cosine similarity',
      url='http://github.com/yanwarsolah/metrominy',
      author='Yanwar Solahudin',
      author_email='yanwarsolah@gmail.com',
      license='MIT',
      packages=['metrominy'],
      install_requires=['redis==2.10.3', ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],)