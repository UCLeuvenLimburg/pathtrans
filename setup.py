from setuptools import setup


def fetch_version():
      '''
      Fetches version variable from version.py
      '''
      version = {}

      with open('pathtrans/version.py') as f:
            exec(f.read(), version)

      return version['__version__']



setup(name='pathtrans',
      version=fetch_version(),
      description='Converts between Unix and Windows paths',
      url='http://github.com/UCLeuvenLimburg/pathtrans',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['pathtrans'],
      entry_points = {
            'console_scripts': [ 'p2unix=pathtrans.command_line:windows_to_unix', 'p2win=pathtrans.command_line:unix_to_windows' ]
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)