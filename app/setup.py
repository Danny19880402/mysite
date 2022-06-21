from setuptools import setup, find_packages

install_requires = [
    'Flask == 1.1.0',
    'flask_sqlalchemy == 2.3.2',
    'requests==2.13.0',
    'numpy==1.22.0',
    'pandas==0.23.0'
]

tests_require = [
    'pytest',
    ]

setup(
    name='mysite',
    version='1.0.1',
    author='Duxuede',
    author_email='duxuede1988@163.com',
    license='MIT',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True
)
