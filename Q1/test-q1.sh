#!/bin/sh
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/sbin/start-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /q1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../project-1/Parking_Violations_Issued_-_Fiscal_Year_2014__August_2013___June_2014_.csv /q1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file mapperq1.py -mapper mapperq1.py \
-file reducerq1.py -reducer reducerq1.py \
-input /q1/input/* -output /q1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /q1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/stop-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh stop historyserver
