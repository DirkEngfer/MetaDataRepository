#!/usr/bin/env python
# coding: utf-8
import os, time

out = open('q_out.txt', 'w')
outputname = 'SDTM_CM_variables.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace(' ', '')
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)

out = open('q_out.txt', 'w')
outputname = 'SDTM_CM_variables_sort_order.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace(' ', '').replace('"', ' ')
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)

out = open('q_out.txt', 'w')
outputname = 'SDTM_Convert_CMSTDTC_to_ATM.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('| ', '').replace('|', '').replace('d:', '').replace('"', '')
        text = ' '.join(filter(None,text.split(' ')))
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)

out = open('q_out.txt', 'w')
outputname = 'EndDayImputation.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line[1:].replace('d:', '').replace('|\n', '\n')
        textL = text.split('|')
        text = '|'.join([x.strip() for x in textL])
        text = text + '\n'
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)

out = open('q_out.txt', 'w')
outputname = 'StartDayImputation.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace('"', '')
        text = ' '.join(filter(None,text.split(' ')))
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)


out = open('q_out.txt', 'w')
outputname = 'LLOQ.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace('"', '')
        text = ' '.join(filter(None,text.split(' ')))
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)

out = open('q_out.txt', 'w')
outputname = 'ARM_code_ADAS-Cog_summary_table.txt'
with open(outputname, 'rt') as f:
  i = 0
  for line in f:
    if i >= 3:
      if line[0:1] == '|':
        text = line.replace('|', '').replace('d:', '').replace('"', '')
        text = ' '.join(filter(None,text.split(' ')))
        out.write(text)
    i +=1
out.close()
os.remove("./" + outputname)
os.rename('q_out.txt', outputname)


