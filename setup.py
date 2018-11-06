from setuptools import setup

VERSION = "0.1.1"

setup(
    name='blendercam',
    version=VERSION,
    description='Blender CAM',
    author='various',
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7"
    ],
    packages=["blendercam",
              ],
    install_requires=[
        "flake8",
        "flask",
        "pylint",
        "nose",
        "nose-cov"
    ],
    setup_requires=[
        "mock"
    ],
#    entry_points={
#        'console_scripts': [
#            "dir2stdout = traffic_distributor.dir2stdout:main",
#            "stdin2dir = traffic_distributor.stdin2dir:main",
#            "tcs_traffic_move = traffic_distributor.tcs_traffic_move:main"
#        ]
#    }
)
