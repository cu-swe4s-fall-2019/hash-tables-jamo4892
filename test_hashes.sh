#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle hash_functions.py
assert_no_stdout
run test_style pycodestyle hash_tables.py
assert_no_stdout
run test_style pycodestyle scatter.py
assert_no_stdout
# Verify pycodestyle formatting in all Python scripts.

run test_ascii_bad_input python hash_functions.py --input 10 --size 100000000 --method 'ascii'
assert_exit_code EX_OK
run test_rolling_bad_input python hash_functions.py --input 10 --size 100000000 --method 'rolling'
assert_exit_code EX_OK
# Test the h_ascii & h_rolling functions with an incorrect input string.

run test_linear_ascii_tables python hash_tables.py --size 1000 --method 'ascii' --input 'hash' --keys_add 1000 --keys_search 1000 --collision 'linear'
assert_no_stdout
run test_linear_rolling_tables python hash_tables.py --size 1000 --method 'rolling' --input 'hash' --keys_add 1000 --keys_search 1000 --collision 'linear'
assert_no_stdout
run test_chained_ascii_tables python hash_tables.py --size 1000 --method 'ascii' --input 'hash' --keys_add 1000 --keys_search 1000 --collision 'chained'
assert_no_stdout
run test_chained_rolling_tables python hash_tables.py --size 1000 --method 'rolling' --input 'hash' --keys_add 1000 --keys_search 1000 --collision 'chained'
assert_no_stdout
# Test the LinearProbe and ChainedHash classes in hash_tables.py.

run test_plot_ascii python hash_functions.py --input 'hash.txt' --size 1000 --method 'ascii' | python scatter.py --out_file ascii_hash.png
assert_no_stdout
run test_plot_rolling python hash_functions.py --input 'hash.txt' --size 1000 --method 'rolling' | python scatter.py --out_file rolling_hash.png
assert_no_stdout
# Test that plots of the hash functions are made by scatter.py.