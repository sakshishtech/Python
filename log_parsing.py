def analyze_logs(file_path):
    counts = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    return counts


result = analyze_logs("application.log")
print(result)

#output
# {
#     'ERROR': 2,
#     'WARNING': 1,
#     'INFO': 2
# }
