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
run test_rolling_bad_input python hash_functions.py --input 10 --size 100000000 --method 'rolling'
assert_exit_code EX_OK
# Test the h_ascii & h_rolling functions with an incorrect input string.

run test_linear_ascii_tables python hash_tables.py --size 10 --method 'ascii' --input 'hash' --keys_add 0 --keys_search 0 --collision 'linear'
assert_no_stdout
run test_linear_rolling_tables python hash_tables.py --size 10 --method 'rolling' --input 'hash' --keys_add 0 --keys_search 0 --collision 'linear'
assert_no_stdout
run test_chained_ascii_tables python hash_tables.py --size 10 --method 'ascii' --input 'hash' --keys_add 0 --keys_search 0 --collision 'chained'
assert_no_stdout
run test_chained_rolling_tables python hash_tables.py --size 10 --method 'rolling' --input 'hash' --keys_add 0 --keys_search 0 --collision 'chained'
assert_no_stdout
# Test the LinearProbe and ChainedHash class initializations in hash_tables.py.