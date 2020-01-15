import sys
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":

    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))

    #create Spark context with necessary configuration
    sc = SparkContext("local","PySpark Word Count Exmaple")

    #read data from text file and split each line into words
    words = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))

    #count the occurence of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

    wordCounts.saveAsTextFile(sys.argv[2])


