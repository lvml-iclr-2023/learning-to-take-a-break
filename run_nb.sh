#! /bin/bash
in_file=$1.ipynb
out_file=$1_$2.ipynb
seed=$2
RANDOM_STATE=${seed} conda run -n lvml_submission jupyter nbconvert --to notebook --execute ${in_file} --output ${out_file}
