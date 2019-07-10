from setuptools import setup

setup(
    name='pytest-testmon',
    description='find bugs 10x faster',
    long_description=''.join(open('README.rst').readlines()),
    version='0.9.18',
    license='MIT',
    platforms=['linux', 'osx', 'win32'],
    packages=['testmon'],
    url='https://testmon.org',
    project_urls={
        "Source Code": 'https://github.com/tarpas/pytest-testmon/',
    },
    author_email='tibor.arpas@infinit.sk',
    author='Tibor Arpas, Jozef Knaperek, Martin Riesz, Daniel Hahler',
    entry_points={
        'pytest11': [
            'testmon = testmon.pytest_testmon',
        ],
        'tox': [
            'testmon = testmon.tox_testmon',
        ],
    },
    install_requires=[
        'pytest>=2.8.0,<6',
        'coverage>=4,<5',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python',
    ],
)
