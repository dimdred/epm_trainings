#old parcing and mapping
#! /bin/env/ python
# run this command in cmd
# cd "C:\Users\Sasha\Documents\PythonStudy"
# type net-dump.log | python 20170103_LogParsing_by_teacher.py
# type -n 100 net-dump.log | python 20161229_LogParsing.py - first n rows
'''
import sys

def words2(st, sep=' '):
    cPos = 0
    try:
        while True:
            sPos = st.index(sep, cPos+1)
            yield st[cPos:sPos]
            cPos = sPos + 1
        yield st[cPos:]
    except:
        1==1

f = open('net-dump.log', 'r')
dataFrame = []
for ln in f:
    record = []
    for w in words2(ln, sep=' '):
        record.append(w)
    dataFrame.append(record)
f.close()

dataFrame = filter(lambda x: x[1]=='IP', dataFrame)


def min_ip_map(record):
    i = 0
    sMin = ''
    sIP = ''
    for x in words2(record[0], ':'):
        if i == 1:
            sMin = x
            break
        i += 1
    i = 0
    for x in words2(record[2], '.'):
        if i == 4:break
        sIP = sIP + x + '.'
        i += 1
    return (sMin, sIP)
print map(min_ip_map, dataFrame)
'''

# run this command in cmd
# type net-dump.log | python 20161229_LogParsing.py
import sys
# data = sys.stdin.readlines()
# print "Counted", len(data), "lines."

# for line in sys.stdin:
#     print line
import re

x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2(5[0-5]|[0-4]\d))'
IpRegExp = "(" + x + "\.){3}" + x

time = []
sourceIP = []
targetIP = []
f = open('net-dump.log', 'r')
flagS = '\[.*S.*\]'
for ln in f:
    if len(list(re.finditer(flagS, ln))) != 0:
        IPs = re.finditer(IpRegExp, ln)
        sourceIP.append(IPs.next().group())
        targetIP.append(IPs.next().group())
f.close()
sourceIPunic = set(sourceIP)
targetIPunic = set(targetIP)

n = 0
l = []
for sIPunic in sourceIPunic:
    for IP in targetIP:
        if sIPunic == IP:
            n += 1
    # l.append(sIPunic + ' - ' + IP + ' - ' + str(n))
    print sIPunic + ' - ' + IP + ' - ' + str(n)
    n = 0
