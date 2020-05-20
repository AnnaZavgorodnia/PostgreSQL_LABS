import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate(tuple(sorted(record)), True)


def reducer(key, list_of_values):
    if len(list_of_values) != 2:
        mr.emit(key)
        mr.emit(key[::-1])


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
