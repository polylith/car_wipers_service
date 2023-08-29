#!/bin/bash
report_file="results.xml"
error_file="error.txt"

if [ "$1" == "run_tests" ]; then
  python -m windshield_wiper.tests  > ${report_file} 2>&1
fi
if [ -e ${report_file} ]
then
    cat ${report_file}
else
    cat ${error_file}
fi

if [ "$1" == "run_integration_tests" ]; then
  python -m windshield_wiper.integration_tests  > ${report_file} 2>&1
fi
if [ -e ${report_file} ]
then
    cat ${report_file}
else
    cat ${error_file}
fi

if [ "$1" == "run_car_tests" ]; then
  python -m windshield_wiper.car_tests  > ${report_file} 2>&1
fi
if [ -e ${report_file} ]
then
    cat ${report_file}
else
    cat ${error_file}
fi