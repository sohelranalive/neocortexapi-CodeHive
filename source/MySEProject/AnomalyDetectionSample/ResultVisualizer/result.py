import re
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

def parse_log_file(file_path):
    actual_values, predicted_values, similarity_scores, anomalies_per_seq = [], [], [], {}
    current_seq = None

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Match testing sequences
            seq_match = re.search(r'Testing the sequence for anomaly detection: ([\d, ]+)', line)
            if seq_match:
                current_seq = seq_match.group(1)
                anomalies_per_seq[current_seq] = 0
            
            # Match anomaly detection details
            anomaly_match = re.search(r'Anomaly detected.*predicted it to be (\d+) .* actual value is (\d+)', line)
            if anomaly_match:
                pred, actual = map(int, anomaly_match.groups())
                predicted_values.append(pred)
                actual_values.append(actual)
                anomalies_per_seq[current_seq] += 1
            
            # Match similarity scores
            similarity_match = re.search(r'found similarity to be: ([\d,\.]+)%', line)
            if similarity_match:
                similarity_scores.append(float(similarity_match.group(1).replace(',', '.')))
    
    return actual_values, predicted_values, similarity_scores, anomalies_per_seq

def plot_visualizations(actual, predicted, similarity, anomalies, delta_factor=1, absolute_threshold=20):  
    # Calculate errors and detect anomalies based on standard deviation
    print("Error analysis:")
    errors = np.abs(np.array(predicted) - np.array(actual))
    
    # Calculate mean and standard deviation of errors
    mean_error = np.mean(errors)
    std_error = np.std(errors)
    delta = mean_error + delta_factor * std_error  # Dynamic delta based on error distribution
    
    print(f"Mean Error: {mean_error}, Std Error: {std_error}, Delta Threshold: {delta}")
    
    anomalies_idx = []
    for i in range(len(actual)):
        error = errors[i]
        print(f"Index {i}: Actual = {actual[i]}, Predicted = {predicted[i]}, Error = {error}")
        
        # Check if the error exceeds the dynamic delta or absolute threshold
        if error > delta or error > absolute_threshold:
            anomalies_idx.append(i)
            print(f"Anomaly detected at index {i}: Actual = {actual[i]}, Predicted = {predicted[i]}, Error = {error}")

    print(f"Anomalies detected at indices: {anomalies_idx}")  # Debug print to see anomalies

    # Plot actual vs predicted values
    plt.figure(figsize=(12, 6))
    plt.plot(actual, label='Actual', marker='o', linestyle='-', color='black')
    plt.plot(predicted, label='Predicted', marker='x', linestyle='--', color='blue')
    
    # Highlight anomalies (red dots) - only if the absolute error is greater than delta
    if anomalies_idx:
        plt.scatter(np.array(anomalies_idx), np.array(actual)[anomalies_idx], color='red', label='Anomalies', zorder=5)
    
    plt.legend()
    plt.title('Actual vs. Predicted Values with Anomalies')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.savefig('actual_vs_predicted_with_anomalies.png')
    plt.show()

    # Plot error distribution using histogram and KDE
    plt.figure(figsize=(10, 6))
    sns.histplot(errors, bins=20, kde=True, color='orange')
    plt.title('Prediction Error Distribution (Histogram + KDE)')
    plt.xlabel('Prediction Error')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('prediction_error_distribution.png')
    plt.show()

    # Plot prediction error against actual values using a scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=actual, y=errors, color='green', label='Prediction Errors')

    # Optional: Add a line at y=0 for better reference
    plt.axhline(0, color='red', linestyle='--', linewidth=1, label='Zero Error Line')

    # Optional: Add a trend line (if necessary, using seaborn.regplot)
    sns.regplot(x=actual, y=errors, scatter=False, color='blue', line_kws={"color": "blue", "lw": 2, "ls": "--"})

    # Title and labels
    plt.title('Prediction Error vs. Actual Value', fontsize=14)
    plt.xlabel('Actual Value', fontsize=12)
    plt.ylabel('Prediction Error', fontsize=12)
    plt.grid(True)

    # Add a legend
    plt.legend()

    # Save the plot
    plt.savefig('prediction_error_scatter_enhanced.png')

    # Show the plot
    plt.show()

    # Plot anomalies per sequence
    plt.figure(figsize=(10, 6))
    seqs = list(anomalies.keys())
    anomaly_counts = list(anomalies.values())
    plt.barh(seqs, anomaly_counts, color='pink')
    plt.title('Anomalies per Sequence')
    plt.xlabel('Number of Anomalies')
    plt.ylabel('Sequences')
    plt.grid(True)
    plt.savefig('anomalies_per_sequence_enhanced.png')
    plt.show()

# Example usage
file_path = 'D:\\Update\\neocortexapi-CodeHive\\source\\MySEProject\\AnomalyDetectionSample\\ResultVisualizer\\experiment_results.txt'  # Replace with actual file path
try:
    actual_values, predicted_values, similarity_scores, anomalies_per_seq = parse_log_file(file_path)
    plot_visualizations(actual_values, predicted_values, similarity_scores, anomalies_per_seq)
except FileNotFoundError as e:
    print(e)
