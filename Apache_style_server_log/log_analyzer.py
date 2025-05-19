import re
from collections import Counter

log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<date>.*?)\] '
    r'"(?:GET|POST|PUT|DELETE|HEAD) (?P<url>\S+) HTTP/\d\.\d" '
    r'(?P<status>\d{3})'
)

log_file_path = 'server.log'

ip_counter = Counter()
url_counter = Counter()
error_4xx = 0
error_5xx = 0

with open(log_file_path, 'r') as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            ip = match.group('ip')
            url = match.group('url')
            status = int(match.group('status'))

            ip_counter[ip] += 1
            url_counter[url] += 1

            if 400 <= status < 500:
                error_4xx += 1
            elif 500 <= status < 600:
                error_5xx += 1

print("\n--- Log File Analysis Report ---")
print("\nRequests per IP:")
for ip, count in ip_counter.items():
    print(f"{ip}: {count}")

print("\nTop 5 Most Requested URLs:")
for url, count in url_counter.most_common(5):
    print(f"{url}: {count}")

print(f"\nNumber of 4xx errors: {error_4xx}")
print(f"Number of 5xx errors: {error_5xx}")
