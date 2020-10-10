from setuptools import setup, find_packages

NAME = "server"
VERSION = "1.0.0"

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Explorando Marte",
    author_email="emanuelle.de.pa@gmail.com",
    url="",
    keywords=["Swagger", "Explorando Marte"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['server=server.__main__:main']},
    long_description="""\
    API para criar planaltos, onde serão incluídas sondas que poderão ser movimentadas.
    """
)

