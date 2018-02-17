from setuptools import setup, find_packages

setup(
    name='Evict-Query',
    version='0.1dev',
    packages=find_packages(),
    license='MIT License',
    author='Michael Pinkham, Nick Ackerman',
    install_requires=[
        'selenium',
	'geckodriver'
    ],
    long_description=open('README.md').read()
)
