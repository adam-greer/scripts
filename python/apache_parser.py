import re
import argparse

def search_status_code(log_file, status_code):
    with open(log_file) as f:
        logs = f.readlines()

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*?HTTP/\d\.\d"\s'+ status_code
    regex = re.compile(pattern)

    matches = []
    for line in logs:
        match = regex.search(line)
        if match:
            matches.append(line.strip())

    return matches

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search Apache access log for status code.')
    parser.add_argument('log_file', help='Path to Apache access log file')
    parser.add_argument('status_code', help='HTTP status code to search for')
    args = parser.parse_args()

    logs = search_status_code(args.log_file, args.status_code)
    print('\n'.join(logs))
