#!/bin/bash
#SBATCH -o output/logs2/TDG_SNEE.log         # 输出日志，可以查看ckpt文件夹
#SBATCH -J TDG_SNEE          # 任务名称
#SBATCH -p sugon
#SBATCH --gres=gpu:P100:1
#SBATCH -c 10

CUDA_VISIBLE_DEVICES=0,1 python TC_preprocess.py
CUDA_VISIBLE_DEVICES=0,1 python TC/run_bert.py --do_data 
CUDA_VISIBLE_DEVICES=0,1 python TC/run_bert.py --do_train --save_best
CUDA_VISIBLE_DEVICES=0,1 python TC/run_bert.py --do_test
CUDA_VISIBLE_DEVICES=0,1 python AI_RC_preprocess.py
CUDA_VISIBLE_DEVICES=0,1 python AI_RC/get_data.py
CUDA_VISIBLE_DEVICES=0 python AI_RC/train_start.py
CUDA_VISIBLE_DEVICES=0 python AI_RC/test.py
