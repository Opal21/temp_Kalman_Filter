period = 30  # seconds
std_uncertainty = 0.1
noise_variance = 0.001  # q
initial_guess = 8  # Celsius degree
estimate_error = 10
estimate_uncertainty = estimate_error ** 2  # p0,0
next_estimate_uncertainty = estimate_uncertainty + noise_variance
results = [9.2, 9.4, 9.8, 10.2, 10.4, 10.6, 10.7, 10.9, 11, 11.3, 11.5, 11.7, 11.8, 12.1, 12.3,
           12.4, 12.6, 12.7, 12.9]  # Celsius degree
x = initial_guess


def estimate_next_state(current_result):
    global next_estimate_uncertainty, x
    k = next_estimate_uncertainty / (next_estimate_uncertainty + std_uncertainty)
    x = x + k * (current_result - x)
    next_estimate_uncertainty = (1 - k) * next_estimate_uncertainty
    print(f"k: {k} x: {x} p: {next_estimate_uncertainty}")


def main():
    for result in results:
        estimate_next_state(result)


if __name__ == '__main__':
    main()
