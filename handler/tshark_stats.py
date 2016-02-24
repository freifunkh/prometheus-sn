#!/usr/bin/python2

import argparse

def whitespaces(line, inverted=False):
    for i in range(len(line)):
        if inverted == line[i].isspace():
            return i

assert(whitespaces('    a') == 4)
assert(whitespaces('ass ', inverted=True) == 3)

def read(lines, tag):
    stack = []
    for l in lines:
        depth = whitespaces(l) + 2
        l = l.split()

        # difference in depth
        difference = (depth/2-len(stack))

        if difference > 0: # go deeper
            stack += [''] * difference
        elif difference < 0: # go up
            stack = stack[:difference]

        stack[-1] = l[0]

        p = {
            'filter': ':'.join(stack),
            'packets': l[1].split(':')[1],
            'bytes': l[2].split(':')[1],
            'tag': ',tag="%s"' % tag if tag else ""
        }
        
        print('tshark_packets{{filter="{filter}"{tag}}} {packets}'.format(**p))
        print('tshark_bytes{{filter="{filter}"{tag}}} {bytes}'.format(**p))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input_file',
                        help="stdout of 'tshark -qz io,phs -i <interface>'")
    parser.add_argument('-t', dest='tag', default=False,
                        help="an additional tag for the prometheus output")

    args = parser.parse_args()
    
    lines = []
    with open(args.input_file) as f:
        lines = f.readlines()

    # Remove useless header and tail
    lines = lines[5:-1]

    read(lines, args.tag)
