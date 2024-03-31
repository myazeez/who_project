#!/bin/bash

program_name="blastp"

if command -v $program_name
then
    echo "ncbi blast+ is installed."
else
    echo "$program_name not found, but can be installed with:\n"
fi