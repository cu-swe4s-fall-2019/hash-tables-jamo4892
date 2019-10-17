#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle hash_functions.py
assert_no_stdout
run test_style pycodestyle hash_tables.py
assert_no_stdout
# Verify pycodestyle formatting in all Python scripts.

run test_ascii_bad_input python hash_functions.py --input 10 --size 100000000 --method 'ascii'
assert_exit_code EX_OK
# Test the h_ascii function with an incorrect input string.

run test_rolling_bad_input python hash_functions.py --input 10 --size 100000000 --method 'rolling'
assert_exit_code EX_OK
# Test the h_rolling function with an incorrect input string.