from setuptools import setup, find_packages

setup(
    name='anjaWebhooks',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)