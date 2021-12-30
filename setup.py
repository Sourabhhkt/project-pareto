from setuptools import setup, find_packages


NAME = "project_pareto"
VERSION = "0.1.0dev"


setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    py_modules=["stagedfright"],
    install_requires=[
        "pyomo<6.1",
        "pandas==1.2.*",
        "openpyxl",
        # for the moment mainly for getting solvers with `idaes get-extensions`
        "idaes-pse",
        "requests",
        "plotly",
        "kaleido",
    ],
    include_package_data=True,
    package_data={
        # If any package contains these files, include them:
        "": [
            "*.xlsx",
        ]
    },
    entry_points={
        "console_scripts": [
            "stagedfright=stagedfright:main",
        ]
    },
    maintainer="Keith Beattie",
    maintainer_email="ksbeattie@lbl.gov",
    platforms=["any"],
    license="TODO",
    keywords=[
        NAME
        # TODO add keywords
    ],
    classifiers=[
        # TODO add classifiers
    ],
)
