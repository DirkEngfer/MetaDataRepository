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
time.sleep(0.5)
os.remove("./" + outputname)
time.sleep(0.3)
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
time.sleep(0.5)
os.remove("./" + outputname)
time.sleep(0.3)
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
time.sleep(0.5)
os.remove("./" + outputname)
time.sleep(0.3)
os.rename('q_out.txt', outputname)

out = open('q_out.txt', 'w')
outputname = 'EndDayImputation.txt'
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
time.sleep(0.5)
os.remove("./" + outputname)
time.sleep(0.3)
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
time.sleep(0.5)
os.remove("./" + outputname)
time.sleep(0.3)
os.rename('q_out.txt', outputname)


