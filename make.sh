#!/bin/bash
report_file="results.xml"
error_file="error.txt"

if [ "$1" == "run" ]; then
  python -m car_wipers.tests  > ${report_file} 2>&1
fi
if [ -e ${report_file} ]
then
    cat ${report_file}
else
    cat ${error_file}
fi