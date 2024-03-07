from setuptools import setup, find_packages

setup(
    name='my_naito_app',
    version='0.0.1',
    description='A Frappe app',
    author='Piscium Solutions',
    author_email='kiogora.tcf@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['frappe'],
)
