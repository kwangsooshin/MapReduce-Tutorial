# MapReduce-Tutorial

```bash
chmod +x mapper.py reducer.py
perl -pi -e 's/\r\n/\n/g' mapper.py
perl -pi -e 's/\r\n/\n/g' reducer.py
```

```bash
yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \ -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py \-input /example/data/gutenberg/davinci.txt \-output /example/wordcountout
```

```bassh
hdfs dfs-text /example/wordcountout/part-00000
```