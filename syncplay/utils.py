#coding:utf8

import os


def split_args(args, number):
    # FIXME Make argument format smarter
    return args.split(None, number-1)

def parse_state(args):
    args = split_args(args, 3)
    l = len(args)
    if l == 2:
        state, position = args
        who_changed_state = None
    elif l == 3:
        state, position, who_changed_state = args
    else:
        return

    if not state in ('paused', 'playing'):
        return

    paused = state == 'paused'

    try:
        position = int(position)
    except ValueError:
        return

    position /= 100.0

    return paused, position, who_changed_state

def find_exec_path(name):
    if os.access(name, os.X_OK):
        return name
    for path in os.environ['PATH'].split(':'):
        path = os.path.join(os.path.realpath(path), name)
        if os.access(path, os.X_OK):
            return path

