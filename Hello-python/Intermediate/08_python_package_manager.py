# Python Package Manager

# pip 

# pip --version
# pip install numpy
import numpy

print(numpy.version.version)

numpy_array  =numpy.array([35,24,62,52,30,30,17])
print(type(numpy_array))

print(numpy_array*2)


# Pandas
# pip install pandas


# pip list

# pip uninstall pandas

# pip show 

#pip install requests
import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package 
from my_package import arithmethics

print(arithmethics.sum_two_values(1,4))

from my_other_package import otherarithmethics

print(otherarithmethics.sum_two_values(1,4))