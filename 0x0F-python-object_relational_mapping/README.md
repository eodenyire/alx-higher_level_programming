# ALX Higher Level Programming - Object-Relational Mapping with Python

## Overview

This repository contains solutions to the Object-Relational Mapping (ORM) tasks as part of the ALX Higher Level Programming curriculum. The tasks involve using SQLAlchemy, a Python SQL toolkit and Object-Relational Mapping (ORM) library, to interact with relational databases from Python applications.

## Author Information

This repository is maintained by:

**Emmanuel Odenyire Anyira**

- ALX Africa Student, Software Engineering Program
- Senior Data Analytics Engineer - BI at Safaricom PLC
- Graduate Student at The Cooperative University of Kenya, Masters of Science in Data Science

**LinkedIn:** [Emmanuel Odenyire Anyira on LinkedIn](https://www.linkedin.com/in/emmanuelodenyire/)
**Email:** eodenyire@gmail.com

## Repository Structure

The repository structure is organized by tasks corresponding to specific ORM operations and concepts:

- **0-select_states.py**: Script to list all states from the database.
- **1-filter_states.py**: Script to list states that contain a specific letter.
- **2-my_filter_states.py**: Script to list states using safe parameterized queries.
- **3-my_safe_filter_states.py**: Script to list states using safe parameterized queries with user input.
- **4-cities_by_state.py**: Script to list cities with their respective states.
- **5-filter_cities.py**: Script to list cities based on user input state name.
- **6-model_state.py**: Definition of the State class using SQLAlchemy.
- **7-model_state_fetch_all.py**: Script to list all State objects from the database.
- **8-model_state_fetch_first.py**: Script to fetch the first State object from the database.
- **9-model_state_filter_a.py**: Script to list State objects that contain the letter 'a'.
- **10-model_state_my_get.py**: Script to print the State object with the name passed as an argument.
- **11-model_state_insert.py**: Script to add the State object "Louisiana" to the database.
- **12-model_state_update_id_2.py**: Script to change the name of a State object with a specific ID.
- **13-model_state_delete_a.py**: Script to delete State objects containing the letter 'a'.
- **14-model_city_fetch_by_state.py**: Script to print all City objects from the database with their corresponding State.

## Requirements

- Python 3.x
- SQLAlchemy

## Usage

Each script can be executed with Python from the command line. For example:

```bash
python3 0-select_states.py root root hbtn_0e_6_usa

