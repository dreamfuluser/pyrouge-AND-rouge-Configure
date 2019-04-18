#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------
# Author: Amy_Zhang
# DateTime: 2018/11/29 21:32
# -------------------------------------------------
import pyrouge
import logging

r = pyrouge.Rouge155()
r.model_filename_pattern = 'ref.#ID#.txt'
r.system_filename_pattern = 'cand.(\d+).txt'
r.model_dir = 'D:/untitled/BertSum-master/results/model'
r.system_dir = 'D:/untitled/BertSum-master/results/system'
# r.model_dir = '../log/decode_data/reference'
# r.system_dir = '../log/decode_data/decoded'
# logging.getLogger('global').setLevel(logging.WARNING)  # silence pyrouge logging
rouge_results = r.convert_and_evaluate()
output_dict = r.output_to_dict(rouge_results)
