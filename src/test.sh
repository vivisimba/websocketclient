#!/bin/bash

vmstat
cpuPercent=`vmstat|awk 'NR==3'|awk '{print $12}'`
echo $cpuPercent
