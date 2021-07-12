# Firstly we show install the module i.e countryinfo
pip install countryinfo # if want to take information about this module the go to pypi.org and read.

from countryinfo import CountryInfo
country=CountryInfo("india")

print(country.area())

print(country.borders())

print(country.info())  #gives total info which contains.
