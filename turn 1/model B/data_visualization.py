import matplotlib.pyplot as plt


def parse_data(data_file):
    with open(data_file, 'r') as file:
        data = file.read().splitlines()
    return data


def visualize_data(data):
    plt.plot(range(len(data)), data)
    plt.show()
