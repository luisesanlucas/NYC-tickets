#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/wqParking_Violations_Issued_-_Fiscal_Year_2015.csv /project/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/project/mapper.py -mapper ../../mapreduce-test-python/project/mapper.py \
-file ../../mapreduce-test-python/project/reducer.py -reducer ../../mapreduce-test-python/project/reducer.py \
-input /project/input/* -output /project/output/
/usr/local/hadoop/bin/hdfs dfs -cat /project/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/output/
../../stop.sh


