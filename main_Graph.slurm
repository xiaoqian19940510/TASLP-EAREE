#!/bin/bash
#SBATCH -o output/logs2/CAT_Cls_Graph_changeModeling4.log         # 输出日志，可以查看ckpt文件夹
#SBATCH -J CAT_Cls_Graph_changeModeling4         # 任务名称
#SBATCH -p sugon
#SBATCH --gres=gpu:P100:2
#SBATCH -c 10
CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/Cls_data_preprocess.py
CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Cls/run_bert1.py --do_data 
CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Cls/run_bert1.py --do_train --save_best
CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Cls/run_bert1.py --do_test
CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/Mrc_data_preprocess.py
CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Mrc/get_data.py
CUDA_VISIBLE_DEVICES=0 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Mrc/train_start.py
CUDA_VISIBLE_DEVICES=0 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Mrc/test.py
# CUDA_VISIBLE_DEVICES=0,1 python /home/LAB/liqian/test/game/Ori_graph/CCKS-Mrc/get_submission.py