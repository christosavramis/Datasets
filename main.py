import numpy as np
import matplotlib.pyplot as plt


def generate_dataset_a(_length):
    _data = np.zeros((_length, 3))
    n1 = round(_length/2)
    _data[:n1, [0, 1]] = np.round(np.random.randint(0, 3+1, (n1, 2))/10, 2)
    _data[n1:, [0, 1]] = np.round(np.random.randint(7, 9+1, (n1, 2))/10, 2)
    _data[n1:, -1] = 1
    return _data


def generate_dataset_b(_length):
    np.round(np.random.randint(0, 9 + 1, (round(_length / 4))) / 10, 2)
    return _data _data = np.zeros((_length, 3))
    n1 = round(_length / 2)
    n2 = round(_length/4) + n1

    # (x, y)€[0.0: 0.3,0.0: 0.3]
    _data[:n1, [0, 1]] = np.round(np.random.randint(0, 3 + 1, (n1, 2)) / 10, 2)

    #  (x, y)€[0.0: 0.3,0.4: 0.9]
    _data[n1:, -1] = 1
    _data[n1:n2, 0] = np.round(np.random.randint(0, 3 + 1, (round(_length/4))) / 10, 2)
    _data[n1:n2, 1] = np.round(np.random.randint(4, 9 + 1, (round(_length/4))) / 10, 2)

    #  (x, y)€[0.4: 0.9,0.0: 0.9]
    _data[n2:, 0] = np.round(np.random.randint(4, 9 + 1, (round(_length / 4))) / 10, 2)
    _data[n2:, 1] =


def generate_dataset_c(_length):
    _data = np.zeros((_length, 3))
    n1 = round(_length / 2)
    n2 = round(_length / 8) + n1
    n3 = round(_length / 8) + n2
    n4 = round(_length / 8) + n3

    #  (x, y)€[0.4: 0.6,0.4: 0.6]
    _data[:n1, [0, 1]] = np.round(np.random.randint(4, 6 + 1, (n1, 2)) / 10, 2)

    #  (x, y)€[0.0: 0.9,0.0: 0.3]
    _data[n1:, -1] = 1
    _data[n1:n2, 0] = np.round(np.random.randint(0, 9 + 1, (round(_length / 8))) / 10, 2)
    _data[n1:n2, 1] = np.round(np.random.randint(0, 3 + 1, (round(_length / 8))) / 10, 2)

    #  (x, y)€[0.0: 0.9,0.7: 0.9]
    _data[n2:n3, 0] = np.round(np.random.randint(0, 9 + 1, (round(_length / 8))) / 10, 2)
    _data[n2:n3, 1] = np.round(np.random.randint(7, 9 + 1, (round(_length / 8))) / 10, 2)

    #  (x, y)€[0.0: 0.3,0.0: 0.9]
    _data[n3:n4, 0] = np.round(np.random.randint(0, 3 + 1, (round(_length / 8))) / 10, 2)
    _data[n3:n4, 1] = np.round(np.random.randint(0, 9 + 1, (round(_length / 8))) / 10, 2)

    #  (x, y)€[0.7: 0.9,0.0: 0.9]
    _data[n4:, 0] = np.round(np.random.randint(7, 9 + 1, (round(_length / 8))) / 10, 2)
    _data[n4:, 1] = np.round(np.random.randint(0, 9 + 1, (round(_length / 8))) / 10, 2)

    return _data


def generate_dataset_d(_length):
    _data = np.zeros((_length, 3))
    n1 = round(_length / 4)
    n2 = round(_length / 4) + n1
    n3 = round(_length / 4) + n2

    #  (x, y)€[0.0: 0.3,0.0: 0.3]
    _data[:n1, [0, 1]] = np.round(np.random.randint(0, 3 + 1, (n1, 2)) / 10, 2)

    #  (x, y)€[0.7: 0.9,0.7: 0.9]
    _data[n1:n2, 0] = np.round(np.random.randint(7, 9 + 1, (round(_length / 4))) / 10, 2)
    _data[n1:n2, 1] = np.round(np.random.randint(7, 9 + 1, (round(_length / 4))) / 10, 2)

    #  (x, y)€[0.7: 0.9,0.0: 0.3]
    _data[n2:, -1] = 1
    _data[n2:n3, 0] = np.round(np.random.randint(7, 9 + 1, (round(_length / 4))) / 10, 2)
    _data[n2:n3, 1] = np.round(np.random.randint(0, 3 + 1, (round(_length / 4))) / 10, 2)

    #  (x, y)€[0.0: 0.3,0.7: 0.9]
    _data[n3:, 0] = np.round(np.random.randint(0, 3 + 1, (round(_length / 4))) / 10, 2)
    _data[n3:, 1] = np.round(np.random.randint(7, 9 + 1, (round(_length / 4))) / 10, 2)

    return _data


if __name__ == '__main__':
    length = 100
    # data = generate_dataset_a(length)
    # np.savetxt("a_linear_2_classes.csv", data, fmt='%2.1f', delimiter=",")
    # plt.scatter(np.array(data[50:, 0]), np.array(data[50:, 1]), marker='x', label='versicolor')
    # plt.scatter(np.array(data[:50, 0]), np.array(data[:50, 1]), marker='o', label='setosa')
    # # display the equation
    # plt.xlabel('petal length')
    # plt.ylabel('sepal length')
    # plt.legend()
    # plt.show()

    # data = generate_dataset_b(length)
    # np.savetxt("b_non_linear_2_classes.csv", data, fmt='%2.1f', delimiter=",")
    # plt.scatter(np.array(data[:50, 0]), np.array(data[:50, 1]), marker='o', label='classA')
    # plt.scatter(np.array(data[50:, 0]), np.array(data[50:, 1]), marker='x', label='classB')
    # # display the equation
    # plt.xlabel('feature X')
    # plt.ylabel('feature y')
    # plt.legend()
    # plt.show()

    # length % 8 == 0 <-true!
    # length = 112
    # data = generate_dataset_c(length)
    # np.savetxt("c_non_linear_2_classes.csv", data, fmt='%2.1f', delimiter=",")
    # plt.scatter(np.array(data[62:, 0]), np.array(data[62:, 1]), marker='x', label='classA')
    # plt.scatter(np.array(data[:62, 0]), np.array(data[:62, 1]), marker='o', label='classB')
    # # display the equation
    # plt.xlabel('petal length')
    # plt.ylabel('sepal length')
    # plt.legend()
    # plt.show()
    # print(data)

    # length = 100
    # data = generate_dataset_d(length)
    # np.savetxt("d_non_linear_2_classes.csv", data, fmt='%2.1f', delimiter=",")
    # plt.scatter(np.array(data[50:, 0]), np.array(data[50:, 1]), marker='x', label='classA')
    # plt.scatter(np.array(data[:50, 0]), np.array(data[:50, 1]), marker='o', label='classB')
    # # display the equation
    # plt.xlabel('feature X')
    # plt.ylabel('feature y')
    # plt.legend()
    # plt.show()
    # print(data)
