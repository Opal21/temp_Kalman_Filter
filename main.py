import csv
import random

period = 30  # seconds
std_uncertainty = 0.01
noise_variance = 0.01  # q
initial_guess = 9  # Celsius degree
x = initial_guess
estimate_error = 100
estimate_uncertainty = estimate_error ** 2  # p0,0
next_estimate_uncertainty = estimate_uncertainty + noise_variance
measurements = [9.2, 9.4, 9.8, 10.2, 10.4, 10.6, 10.7, 10.9, 11, 11.3, 11.5, 11.7, 11.8, 12.1, 12.3,
                12.4, 12.6, 12.7, 12.9]  # Celsius degree
results = []
noisy_numbers = []
possible_signs = ["+", "-"]


def estimate_next_state(current_result):
    global next_estimate_uncertainty, x
    k = next_estimate_uncertainty / (next_estimate_uncertainty + std_uncertainty)
    x = x + k * (current_result - x)
    next_estimate_uncertainty = (1 - k) * next_estimate_uncertainty
    next_estimate_uncertainty += noise_variance
    results.append(x)
    # print(f"k: {k} x: {x} p: {next_estimate_uncertainty}")


def main():
    generate_noisy_data()
    with open("results.csv", mode="r") as read_file:
        measurements = []
        csv_reader = csv.reader(read_file)
        for element in csv_reader:
            for value in element:
                # print(value)
                measurements.append(float(value))

    for result in measurements:
        estimate_next_state(result)

    with open("filtered_results.csv", mode='w') as write_file:
        file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for result in results:
            file_writer.writerow([result])


def generate_noisy_data():
    for number in measurements:
        for i in range(10):
            noise = random.random()
            sign = random.choice(possible_signs)
            if sign == "+":
                noisy_numbers.append(number + noise / 5)
            elif sign == "-":
                noisy_numbers.append(number - noise / 5)

    with open("results.csv", mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for n in noisy_numbers:
            file_writer.writerow([n])


if __name__ == '__main__':
    main()
