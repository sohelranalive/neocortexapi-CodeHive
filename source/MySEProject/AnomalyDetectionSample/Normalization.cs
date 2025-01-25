using System.Collections.Generic;
using System.Linq;

namespace AnomalyDetectionSample
{
    public static class Normalization
    {
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
    }
}
