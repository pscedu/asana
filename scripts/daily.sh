#!/bin/bash

module load anaconda3
cd /jet/home/icaoberg/code/asana/scripts

python ./create_general_task.py -m "Run daily_report.py" -n "Do it on hive as hive. Creates daily report until Gesina turns this into a DAG." -d 1

python ./create_general_task.py -m "Run daily_builder.py" -n "Do it on hive as hive. Attempts to build inventories for new datasets until Gesina turns this into a DAG." -d 1

