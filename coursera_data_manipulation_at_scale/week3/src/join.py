import sys
import itertools

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    table, order_id = record[:2]
    mr.emit_intermediate(order_id, record)


def reducer(key, list_of_values):
    from_line_item = [r for r in list_of_values if r[0] == 'line_item']
    from_order = [r for r in list_of_values if r[0] == 'order']
    for r1, r2 in itertools.product(from_order, from_line_item):
        mr.emit(r1 + r2)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
