#!/usr/bin/env python
# coding: utf-8
import os

out = open('q_out.txt', 'w')
with open('SDTM_CM_variables.txt', 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace(' ', '')
        out.write(text)
    i +=1
out.close()
os.remove("./SDTM_CM_variables.txt")
os.rename('q_out.txt', 'SDTM_CM_variables.txt')

out = open('q_out.txt', 'w')
with open('SDTM_CM_variables_sort_order.txt', 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace(' ', '').replace('"', ' ')
        out.write(text)
    i +=1
out.close()
os.remove("./SDTM_CM_variables_sort_order.txt")
os.rename('q_out.txt', 'SDTM_CM_variables_sort_order.txt')