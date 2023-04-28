from pyspark import SparkContext
import sys
import string

def words_split(line):
    for c in string.punctuation+"¿!«»":
        line = line.replace(c,' ')
        line = line.lower()
    return len(line.split())

def main(filename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(filename)
        words_rdd = data.map(words_split)
        print ('RESULTS------------------')
        print ('words_count', words_rdd.sum())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No hay un número adecuado de parámetros: python3 {0} <file>".format(sys.argv[0]))
    else:
        main(sys.argv[1])
