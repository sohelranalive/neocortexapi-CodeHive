using System.Collections.Generic;
using System.Linq;

namespace AnomalyDetectionSample
{
    public static class Normalization
    {
        // Parameters for MultiSequenceLearning tuning
        public static int MaxEpochs { get; set; } = 100; // Default number of epochs
        public static double LearningRate { get; set; } = 0.01; // Default learning rate
        public static double InputNoise { get; set; } = 0.05; // Default input noise level

        /// <summary>
        /// Normalizes a list of numerical sequences for better HTM training.
        /// </summary>
        /// <param name="sequences">List of numerical sequences.</param>
        /// <returns>Normalized list of numerical sequences.</returns>
        public static List<List<double>> NormalizeSequences(List<List<double>> sequences)
        {
            List<List<double>> normalizedSequences = new List<List<double>>();
            foreach (var sequence in sequences)
            {
                double min = sequence.Min();
                double max = sequence.Max();

                // Avoid division by zero
                double range = max - min == 0 ? 1 : max - min;

                normalizedSequences.Add(sequence.Select(value => (value - min) / range).ToList());
            }
            return normalizedSequences;
        }

        /// <summary>
        /// Configures the tuning parameters for MultiSequenceLearning.
        /// </summary>
        /// <param name="maxEpochs">Maximum number of epochs.</param>
        /// <param name="learningRate">Learning rate for the model.</param>
        /// <param name="inputNoise">Noise level to add for robustness.</param>
        public static void ConfigureTuningParameters(int maxEpochs, double learningRate, double inputNoise)
        {
            MaxEpochs = maxEpochs;
            LearningRate = learningRate;
            InputNoise = inputNoise;
        }
    }
}
