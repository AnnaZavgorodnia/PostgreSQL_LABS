import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    docid, text = record
    for word in text.split():
        mr.emit_intermediate(word, docid)


def reducer(key, list_of_values):
    total = set()
    for v in list_of_values:
        total.add(v)
    mr.emit((key, list(total)))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
