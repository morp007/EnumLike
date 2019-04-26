# -*- coding:utf-8 -*-

import argparse
import sys

from enum_like import EnumLike, Args


#
# define some "types"
#

class CheckType(EnumLike):
    pass


class ConnectionType(EnumLike):
    pass


#
# create some values
#

Args.CONNECTION_1 = ConnectionType('connection 1')
Args.CONNECTION_2 = ConnectionType('connection 2')
Args.BASE_CHECK = CheckType(1)
Args.EXTENDED_CHECK = CheckType(2)

# same value as Args.BASE_CHECK
# you can do it, but it's bad
Args.ANOTHER_CHECK = CheckType(1)


# some function
def f(check_type, connection_type):
    """
    Args:
        check_type(CheckType):               The check type
        connection_type(ConnectionType):     The connection type

    """
    assert isinstance(check_type, CheckType)
    assert isinstance(connection_type, ConnectionType)

    # do some
    pass


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-check_type', default=Args.BASE_CHECK.value)
    parser.add_argument('-connection_type', default=Args.CONNECTION_1.value)
    return parser.parse_args(sys.argv[1:])


if __name__ == '__main__':
    print '{:-<80}'.format('Task #1')
    print 'getting variables from its value ...',
    check = Args.get(1, CheckType)[0]
    conn = Args.get('connection 1', ConnectionType)[0]
    print 'done'
    print 'call function f() ...',
    f(check, conn)
    print ('done,'
           '\n\tArgs.get() returns values with proper type,' 
           ' otherwise an exception occur')
    print

    print '{:-<80}'.format('Task #2:')
    print 'get variables from call arguments ...',
    input_args = get_args()
    f(check_type=Args.get(input_args.check_type, CheckType)[0],
      connection_type=Args.get(input_args.connection_type, ConnectionType)[0])
    print 'done'
    print

    print '{:-<80}'.format('Additional info:')
    print 'Situation when Args have multiple variables with same value.'
    print
    print 'get variable by value ...',
    check_list = Args.get(1, CheckType)
    print 'done'
    assert len(check_list) == 2
    print "found more than one variable, let's see..."
    for i, _ in enumerate(check_list):
        print '  variable #{}: id = 0x{:X}, value = "{}"'.format(i, id(_), _)
        print '  comparing ...',
        print "it's", {Args.BASE_CHECK: 'Args.BASE_CHECK',
                       Args.EXTENDED_CHECK: 'Args.EXTENDED_CHECK',
                       Args.ANOTHER_CHECK: 'Args.ANOTHER_CHECK'}[_]
