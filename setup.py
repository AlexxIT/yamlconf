from distutils.core import setup

setup(
    name='yamlconf',
    version='0.1.0',
    description="Store app config in yaml file",
    author="Alexey Khit",
    install_requires=['pyyaml'],
    packages=['yamlconf']
)