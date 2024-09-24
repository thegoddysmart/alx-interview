#!/usr/bin/python3
"""Log Parser"""
import sys


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """
        Prints the current total file size and
        counts of status codes
        """
        print('File size: {}'.format(file_size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_line(line):
        """ Checks the line for matches """
        try:
            line = line[:-1]
            word = line.split(' ')
            # Update the file size
            file_size[0] += int(word[-1])
            # Update the status code count if it is a valid code
            status_code = int(word[-2])
            # Loop
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    line_count = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            """After every 10 lines, print the metrics"""
            if line_count % 10 == 0:
                print_stats()
            line_count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
