import argparse

# The data samples will be appended to this list
sample_data = []

# Computes the average of the --window-size data from our sample_data list
def average(sample_data, win_size):
    # Initiliazes window_size_data as the interval between index 0 and the inddex of the last --window-size number
    window_size_data = sample_data[0:win_size]
    # Returns the average and handles the exception of dividing by zero
    return sum(window_size_data) / len(window_size_data) if len(window_size_data) else 0

# Detects the anomalies
def detect_anomaly(win_size, threshold):
    for i in range(win_size * 2):
        # User inputs the data (2x the win-size)
        data = float(input())
        # Appends the user input to the empty sample_data initialized above
        sample_data.append(data)

        # Handling the 3 situations our loop might run into
        if sample_data.index(data) <= win_size - 1 and sample_data.index(data) == 0:
            print(f"{sample_data[i]} - Normal (no historical data)")
        elif sample_data.index(data) <= win_size - 1:
            print(f"{sample_data[i]} - Normal (historical data size < window size)")
        elif sample_data[i] >= average(sample_data, win_size) - threshold and sample_data[i] <= average(sample_data, win_size) + threshold:
            print(f"{sample_data[i]} - Normal")
        else:
            print(f"{sample_data[i]} - Anomaly")


if __name__ == "__main__":
    # Creates the parser for the CL arguments
    parser = argparse.ArgumentParser()
    # Adds the required --window-size arg of type int
    parser.add_argument('--window-size', type=int, required=True)
    # Adds the required --threshold arg of type float
    parser.add_argument('--threshold', type=float, required=True)
    # Checks and parses the arguments if provided, if not, an error is thrown
    args = parser.parse_args()

    # Runs the detect_anomaly function with the CL args as parameters
    detect_anomaly(args.window_size, args.threshold)
