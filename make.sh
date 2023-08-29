#!/bin/bash

report_file="results.xml"
error_file="error.txt"

run_tests() {
  module_name="windshield_wiper.$1"
  python -m "$module_name" > "$report_file" 2>&1
}

if [ "$1" == "tests" ] || [ "$1" == "integration_tests" ] || [ "$1" == "car_tests" ]; then
  run_tests "$1"
  if [ -e "$report_file" ]; then
    cat "$report_file"
  else
    cat "$error_file"
  fi
fi