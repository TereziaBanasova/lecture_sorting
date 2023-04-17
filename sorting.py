import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(number_array):
    n = len(number_array)
    for i in range(n):
        min_idx = i
        for num_idx in range(i + 1, n):
            if number_array[num_idx] < number_array[min_idx]:
                min_idx = num_idx
        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]
    return number_array



def main():
    my_data = read_data("numbers.csv")
    print(my_data)
    selection_sort_result = selection_sort(my_data["series_1"].copy())
    print(selection_sort_result)

if __name__ == '__main__':
    main()
