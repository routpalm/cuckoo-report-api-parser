import json
import matplotlib.pyplot as plt


def read_file(file_path):
    f = open(file_path)
    data = f.read()
    return json.loads(data)


def parse_json_file(file_name):
    print("Parsing report.json...")
    calls_list = []
    count_list = []
    data = read_file(file_name)
    apis = data['behavior']['apistats']
    keys = apis.keys() # roundabout way of obtaining the count (there are multiple json objects in apistats)
    for key in keys:
        calls = apis[key]
        counts = calls.keys()
        for call in counts:
            count = calls[call]
            print(f'API: {call} | count: {count}')
            calls_list.append(call)
            count_list.append(count)
    print("Parsing complete. Displaying data...")
    print("Calls: " + str(len(calls_list)))
    display_data(calls_list, count_list)
    return calls_list, count_list


def display_data(calls, counts):
    generate_histogram(counts)
    generate_bar(calls, counts)


def generate_bar(calls, counts):
    plt.title("Bar Graph")
    plt.xlabel("APIs")
    plt.ylabel("Count")
    plt.bar(calls, counts)
    plt.show()


def generate_histogram(counts):
    plt.title("Histogram")
    plt.xlabel("APIs")
    plt.ylabel("Count")
    plt.hist(counts, density=True, bins=50)
    plt.show()


def validate():
    script_calls, script_count = parse_json_file('/home/cuckoo/.cuckoo/storage/analyses/2/reports/report.json')
    non_script_calls, non_script_count = parse_json_file('/home/cuckoo/.cuckoo/storage/analyses/5/reports/report.json')

    print(set(script_calls) == set(non_script_calls))
    print(set(script_count) == set(non_script_count))


if __name__ == '__main__':
    analysis = input("Which analysis would you like to process? ")
    file = f'/home/cuckoo/.cuckoo/storage/analyses/{analysis}/reports/report.json'
    parse_json_file(file)
    # validate()
