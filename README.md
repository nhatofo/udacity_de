Data Modeling Project

This is my solution for the first project in the Data Engineering Nanodegree at Udacity . The goal is to design a star schema data warehouse and implement ETL processes for a music streaming startup(Sparkify).


Getting Started
These instructions will get you a copy of the project up and running on any dev/test machine. The below steps where tested on Udacity Virtual Student env.

Running the ETL Process

To create and populate the database, execute the below commands on workspace :


ls           # to list files and dirs
python create_tables.py   # create database and empty tables
python etl.py             # populate tables

For validate the process I executed  the following commands:

python test.py                   # to verify if everthing went as planned 

Data Warehousing at Sparkify
Sparkify is a music streaming startup that provides free and paid on cloud music streaming  plans and there are trying  to enquire more users with paid plans. So they need any analytic data wharehouse so that they can learn more about their users and how to convert them to paid customers.

Currently, Sparkify is storing there data on json format which is very deficult to extract insights from. So as solution for the need, they dicided to implement a data wharehouse to support their data analytics process sinse the data still grouying and ramain on silos. so they will need to extract the data from json files, transform and load on a postgress data wherehouse for futher analysis.

Database Schema
The database schema follows the Snowflake style, with one fact table (songplays) and four dimension tables (time, users, songs and artists).
The songplays table has foreign key constraints to all dimensions and well as a composite primary key, made out of all foreign keys(time, users_id, songs_id and artists_id).


Authors
Teofilo Carlos Chichume





