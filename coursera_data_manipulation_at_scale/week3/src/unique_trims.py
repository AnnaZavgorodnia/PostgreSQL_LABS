import sys
import itertools

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[:-10], key)


def reducer(key, _):
    mr.emit(key)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
