# ASA 2023 - Project 3

## Introduction
This project was made in the Analysis and synthesis of algorithms course. Made to deepen our knowledge about linear 
programming. This program was implemented in python using the [PuLP library](https://https://pypi.org/project/PuLP/),
and the [GLPK](https://www.gnu.org/software/glpk/) PL solver.

## Description
Given an `n` amount of toys, where each toy has a value and cost, `p` amount of packages (three toys each) with a cost,
and several constraints, what is the maximum amount of value we can accumulate daily.

### Constraints
Each toy has a specific production limit and there is also a general production limit

## Installing
PuLP installation
```s
python -m pip install pulp
```

PL solver
```s
sudo apt-get install glpk-utils
```

## Running
```s
python3 p3.py
```

## Input format
The first line receives `{num_of_toys} {num_of_packages} {general_production_limit}`

The next `n` lines receive `{toy_value} {toy_production_limt}`

The next `p` lines receive `{package_value} {toy_1} {toy_2} {toy_3}`

