# ML 24/25-03 Implement Anomaly Detection Sample

## Overview:

- [Problem Statement](#Problem-Statement)
- [Introduction](#Introduction)
- [Objectives](#Objectives)
- [HTM Basics](#HTM-Basics)
- [Requirements](#Requirements)
- [Project Structure](#Project-Structure)
- [Project Methodology](#Project-Methodology)
- [Details](#Details)
- [Execution of the project](#Execution of the project)
- [Results and Discussion](#Results-and-Discussion)
- [Conclusion](#Conclusion)

## Problem Statement

<p align='Justify'> The initial challenge to apply a model that can accurately identify the anomalies in numeric time-series data using Hierarchical Temporal Memory(HTM). The problem involves teaching the HTM model to identify the underlying patterns from the train dataset, then using the knowledge to predict and identify irregularities in the test dataset. Anomalies can be defined as data points that deviate significantly from the expected range or pattern. The aim of the project is to simulate a real-world scenario by generating artificial data to train and test the system. Detecting irregularities accurately is critical for applications in areas like network monitoring, fraud detection and predictive maintenance. </p>

## Introduction

<p align='Justify'> Hierarchical Temporal Memory(HTM) is a machine learning algorithm which is inspired from the neocortex of the human brain. HTM excels at recognizing temporal patterns and making predictions in time-series data. For taking input data efficiently and robustly HTM used Sparse Distributed Representations(SDRs).</p>

(Figure 1: HTM is inspired from neocortex of human brain.) - A figure need to add this point.

In the project, the NeoCortexAPI – a .NET implementation of the HTM framework – will be used to make an anomaly detection system. The project include two parts:

- 1. Training: The HTM model trains from the normal numeric sequences, such as network traffic loads, from artificially created data.

- 2. Testing: The trained model is tested on new sequences containing both normal data and anomalies. The model identifies anomalies based on deviations from predicted values.

<p align='Justify'> The project will used C# and the NeoCortexAPI library to process the data, train the HTM model, and evaluate the performance. The main objective of the project is to determine a robust and efficient system which can accurately predict the anomalies while analyzing the results using metrics like False Negative Rate(FNR) and False Positive Rate(FNR).</p>

<p align='Justify'> The anomaly detection helps to identify any unusual traffic patterns or anomalies in the network such as cyber-attacks or system failures. Moreover it is used for fraud detection in financial transactions. For monitoring machine and equipment performance and detecting anomalies to prevent breakdowns. The model can also be used to detect diseases on the human body or energy consumption to survey irregularities and optimize energy distribution.</p>

## Objectives

The primary objective of the project is to create and demonstrate an anomalies detection system using HTM. The specific goals include:

- Feature Engineering: Generate artificial numeric data representing network traffic load percentages. Also prepare training data with normal sequences and testing data with random anomalies.

- HTM Model Training: Configure and train the HTM model using the NeoCortexAPI to identify normal patterns from the training dataset.

- Anomaly Detection: Using the trained HTM model to test predicting data and identify anomalies by comparing actual and the predictive values.

- Performance Evaluation: Measure the system’s effectiveness using performance metrics using False Negative Rate(FNR), False Positive Rate(FPR), Mean Square Error(MSE) etc.

<p align='Justify'> By following the steps, I tried to complete the project, which is the practical application of the HTM model for detecting anomalies in time-series data and highlighting its strength and limitations.</p>

## HTM Basics

<p align='Justify'> A theoretical framework for comprehending and modelling how the human neocortex processes information is called Hierarchical Temporal Memory (HTM). It focusses on identifying temporal patterns and formulating predictions using them, and it draws inspiration from neurology. HTM works very effectively for detecting anomalies.HTM contrasts the real input SDR with the anticipated SDR during inference. The HTM quantifies the variance by assigning an anomaly score in the event that the input and the prediction do not match. Unusual or unexpected inputs are detected in real time using the anomaly score.</p>

<p align='Justify'>Hierarchical Temporal Memory (HTM) is fundamentally built on the principles of sparse distributed representations (SDRs), spatial pooling, and temporal memory. SDRs allow HTM to encode information in a way that closely resembles how the neocortex represents sensory inputs, making the model robust to noise and capable of generalizing patterns. The Spatial Pooler ensures that similar inputs generate similar representations while maintaining sparsity, helping the model extract essential features from data. Meanwhile, the Temporal Memory component enables HTM to learn sequences over time, associating past observations with future predictions.</p>

<p align='Justify'></p>

## Requirements

- Software Requirements:

  - .NET Framework/SDK: Version 7.0 or higher.
  - NeoCortexAPI: Library for implementing sequence learning and prediction.
  - IDE: Visual Studio 2022 or any compatible .NET development environment.

- Dependencies:

  - NeoCortexAPI NuGet package (NeoCortexApi Version= 1.1.4 For code debugging).
  - CSV file handling libraries (optional, use in-built .NET functionality).

## Project Structure

<div align="center">
  <img src='\_assets\workflow.jpeg'/>
</div>

## Project Methodology

<p align='Justify'> This point will illustrate the approach used to implement and evaluate the anomaly detection system inspired from the Hierarchical Temporal Model(HTM). It is designed to ensure clarity and efficiency during maintaining a strong foundation in both data science principles and HTM’s biological inspiration. It’s essential to find the best fit HTM model, after tuning its parameters and finding the best HTM model for the project.</p>

#### Data Preparation

<p align='Justify'> Data preparation is one of the most tricky step in the project as it ensures the model is trained and tested wit appropripate, well-structed data. In the project numeric values are stored in the .csv file, representing time-series data. This explicit real-workd scenarios, such as network load percentages with normal data and anomalies strategically included in separate datasets. <p>

- Input Data Overview
  <p align='Justify'> The data consist of numeric sequences representing network load values in percentages. The range of the values between 0 to 100 and normal values are typically within the range of 45 to 55. The dataset has two categories e.g, one is training dataset and another one is testing dataset. The train data follows the numeric order where the testing data contains random sequences. </p>

- Folder Structure
  <p align='Justify'> Data is organized with two folders, where one folder contains train_data and another folder contains predict_data.</p>

- Data Format
  <p align='Justify'> The data is stored in the CSV file and the values must be separate by commas. Training data files contain values within the normal range (e.g, 45 to 55), where testing data files introduce anomalies (e.g, values like 10, 90) at random position. </p>

- Trimming Sequences
  <p align='Justify'> To stimulate real-world incomplete data scenarios, test sequences are cut by removing random number of elements (1 to 4) from the beginning. For example, the sequence the sequence 49,52,55,48,52,47 may be trimmed to 55,48,52,47. Trimming helps the model to generalize and handle or partially observe sequences efficiently. </p>

- Exception Handling
  <p align='Justify'> If any CSV file contains non-numeric data, the system tries to convert the data to numeric values. If a sequences is too short after trimming, it is ignored to avoid error during prediction.</p>

<p align='Justify'> By following this process, the project ensures the HTM model receives clean, meaningful input that accurately represent the problem domain. The processing of the datasets lays the foundation for effective model training, testing and anomaly detection. </p>

#### Key Parameters Tuning of the HTM Model

- Input Dimensions
  <p align='Justify'> The input dimensions specify the length of the input space, represented in a 1D array of bits. If the input range between 0 to 100 with 101 buckets(discrete intervals), and 21 active bits are needed, the total input dimension would be Input Bits = 101 + 21-1=121. It’s important to choose input dimensions based on the range and granularity of the input data. Large input dimensions contain more resolution but raise computational cost. </p>

- Column Dimensions
  <p align='Justify'> This contains the number of mini -columns in the Spatial Pooler. Each column corresponds to a feature in the data. Raise the dimensions for high-dimensional data to gather more patterns. Reduce dimensions for simple datasets to optimize computation. </p>

- Active Threshold
  <p align='Justify'> Calculate the number of active cells required to represent an input. This value controls how many mini-column activate for a given input. For tuning the threshold start with a default threshold and adjust upwards for sparse data to prevent overfitting. Lower it slightly for noisy data to increase sensitivity. </p>

- Permanence Adjustments
  <p align='Justify'> Controlling the strength of synaptic connections in Temporal Memory. The amount by which a connection’s permanence increases when it is reinforced. When it is not used the amount by which a connection’s permanence decreases. For smaller increments or decrements to learn gradually for stable data. Use dynamic values for dynamic or fast changing data to adapt quickly. </p>

- Spatial Pooler
  <p align='Justify'> The input data is encoded into Sparse Distributed Representations(SDRs). For tuning defines the range of columns connected to an input. Take a moderate value to balance global and local connections. Determine the frequency of column activation Boots the activation of underused columns. Higher values used for diverse data. </p>

<div align="center">
  <img src='\_assets\tuning.png' width="300" height="400" />
</div>
  
#### Training and Learning Phase of HTM Model

- Temporal Memory
  <p align='Justify'> Gather sequential patterns by forming connections between cells in mini-columns. It tracks temporal relationships between inputs over time. For tuning, set max synapses per segment higher values to store more context. Determine activation threshold to active synapses required for a segment to be active. Adjust this based on input complexity.
  <br><br>
  In the training and learning phase HTM model enabling it to learn the temporal patterns and relationships in the sequences. Each sequence is processed step by step with the model constructing a representation of the data’s normal structure. The training phase emphasized on originating robust memory connections that capture the essence of normal behavior.
  <br><br>
  Then it goes for testing data which includes anomalies, and is passed to the trained HTM model for prediction. The model is predicted the value depends on the pattern it learns from the training process. Then the predicted value is compared with the actual value. If the deviation exceeds a predefined tolerance the value is flagged as an anomaly.
  <br><br>
  The predicted value is evaluated using metrics like False Negative Rate(FNR) and False Positive Rate(FPR) to determine the model’s performance. This represents the model strength to correctly identify anomalies while minimizing false detections. Logs and outputs are saved for analysis and further optimization.</p>

<div align="center">
  <img src='\_assets\output.png' width="300" height="400" />
</div>

<p align='Justify'> By following this structure methodology, the project ensures the HTM model is effectively trained and tested, resulting in a robust anomaly detection model capable of handling real-world data scenarios. </p>

## Details

We have used [MultiSequenceLearning](https://github.com/ddobric/neocortexapi/blob/master/source/Samples/NeoCortexApiSample/MultisequenceLearning.cs) class in NeoCortex API for training our HTM Engine. We are going to start by reading and using data from both our [training](https://github.com/sohelranalive/neocortexapi-CodeHive/tree/master/source/MySEProject/AnomalyDetectionSample/training) (learning) folder (present as numerical sequences in CSV Files in ['training']((https://github.com/sohelranalive/neocortexapi-CodeHive/tree/master/source/MySEProject/AnomalyDetectionSample/training))) folder inside project directory) and [predicting](https://github.com/sohelranalive/neocortexapi-CodeHive/tree/master/source/MySEProject/AnomalyDetectionSample/predicting) folder (present as numerical sequences in CSV Files in ['predecting'](https://github.com/sohelranalive/neocortexapi-CodeHive/tree/master/source/MySEProject/AnomalyDetectionSample/predicting) folder inside project directory) to train HTM Engine. For testing purposes, we are going to read numerical sequence data from [predicting](https://github.com/sohelranalive/neocortexapi-CodeHive/tree/master/source/MySEProject/AnomalyDetectionSample/predicting) folder and remove the first few elements (essentially, making it a subsequence of the original sequence; we already added anomalies in this data at random indexes), and then use it to detect anomalies.

Please note that all files are read with the .csv extension inside the folders, and exception handlers are in place if the format of the files is not in proper order.

For this project, we are using artificial integer sequence data of network load (rounded off to the nearest integer, in percentage), which are stored inside the CSV files. Example of a CSV file within the training folder.

```
49,52,55,48,52,47,46,50,52,47
49,52,55,48,52,47,46,50,49,47
.............................
.............................
48,54,55,48,52,47,46,50,49,45
51,54,55,48,52,47,46,50,49,45
```
Normally, the values stay within the range of 45 to 55. For testing, we consider anything outside this range to be an anomaly. 
   
### Encoding:

Encoding of our input data is very important, such that it can be processed by our HTM Engine. More on [this](https://github.com/ddobric/neocortexapi/blob/master/source/Documentation/Encoders.md). 

As we are going to train and test data between the range of integer values between 0-100 with no periodicity, we are using the following settings. Minimum and maximum values are set to 0 and 100 respectively, as we are expecting all the values to be in this range only. In other used cases, these values need to be changed.

```csharp

int inputBits = 121;
int numColumns = 1210;
.......................
.......................
double max = 100;

Dictionary<string, object> settings = new Dictionary<string, object>()
            {
                { "W", 21},
                ...........
                { "MinVal", 0.0},
                ...........
                { "MaxVal", max}
            };
 ```
 
 Complete settings:
 
 ```csharp

Dictionary<string, object> settings = new Dictionary<string, object>()
            {
                { "W", 21},
                { "N", inputBits},
                { "Radius", -1.0},
                { "MinVal", 0.0},
                { "Periodic", false},
                { "Name", "integer"},
                { "ClipInput", false},
                { "MaxVal", max}
            };
```

### HTM Configuration:

We have used the following configuration. More on [this](https://github.com/ddobric/neocortexapi/blob/master/source/Documentation/SpatialPooler.md#parameter-desription)

```csharp
{
                Random = new ThreadSafeRandom(42),

                CellsPerColumn = 25,
                GlobalInhibition = true,
                LocalAreaDensity = -1,
                NumActiveColumnsPerInhArea = 0.02 * numColumns,
                PotentialRadius = (int)(0.15 * inputBits),
                //InhibitionRadius = 15,

                MaxBoost = 10.0,
                DutyCyclePeriod = 25,
                MinPctOverlapDutyCycles = 0.75,
                MaxSynapsesPerSegment = (int)(0.02 * numColumns),

                ActivationThreshold = 15,
                ConnectedPermanence = 0.5,

                // Learning is slower than forgetting in this case.
                PermanenceDecrement = 0.25,
                PermanenceIncrement = 0.15,

                // Used by punishing of segments.
                PredictedSegmentDecrement = 0.1
};
```

### Multisequence learning

The [RunExperiment](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/MultiSequenceLearning.cs) method inside the [MultiSequenceLearning](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/MultiSequenceLearning.cs) class file demonstrates how multisequence learning works. To summarize, 

* HTM Configuration is taken and memory of connections are initialized. After that, the HTM Classifier, Cortex layer, and HomeostaticPlasticityController are initialized.
```csharp
.......
var mem = new Connections(cfg);
.......
HtmClassifier<string, ComputeCycle> cls = new HtmClassifier<string, ComputeCycle>();
CortexLayer<object, object> layer1 = new CortexLayer<object, object>("L1");
HomeostaticPlasticityController hpc = new HomeostaticPlasticityController(mem, numUniqueInputs * 150, (isStable, numPatterns, actColAvg, seenInputs) => ..
.......
.......
```

* After that, the Spatial Pooler and Temporal Memory are initialized.
```csharp
.....
TemporalMemory tm = new TemporalMemory();
SpatialPoolerMT sp = new SpatialPoolerMT(hpc);
.....
```
* After that, spatial pooler memory is added to the cortex layer and trained for a maximum number of cycles.
```csharp
.....
layer1.HtmModules.Add("sp", sp);
int maxCycles = 3500;
for (int i = 0; i < maxCycles && isInStableState == false; i++)
.....
`````
* After that, temporal memory is added to the cortex layer to learn all the input sequences.
```csharp
.....
layer1.HtmModules.Add("tm", tm);
foreach (var sequenceKeyPair in sequences){
.....
}
.....
```
* Finally, the trained cortex layer and HTM classifier are returned.
```csharp
.....
return new Predictor(layer1, mem, cls)
.....
`````
We will use this for prediction in later parts of our project.

## Execution of the project

Our project is executed in the following way. 

* In the beginning, we have ReadFolder method of [CSVFolderReader](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/CSVFolderReader.cs) class to read all the files placed inside a folder. Alternatively, we can use ReadFile method of [CSVFileReader](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/CSVFileReader.cs) to read a single file; it works in a similar way, except that it reads a single file. These classes store the read sequences to a list of numeric sequences, which will be used in a number of occasions later. These classes have exception handling implemented inside for handling non-numeric data. Data can be trimmed using Trimsequences method. It trims one to four elements(Number 1 to 4 is decided randomly) from the beginning of a numeric sequence and returns it.

```csharp
 public List<List<double>> ReadFolder()
        {
         ....  
          return folderSequences;
        }

public static List<List<double>> TrimSequences(List<List<double>> sequences)
        {
        ....
          return trimmedSequences;
        }
```

* After that, the method BuildHTMInput of [CSVToHTMInput](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/CSVToHTMInput.cs) class is there which converts all the read sequences to a format suitable for HTM training.
```csharp
Dictionary<string, List<double>> dictionary = new Dictionary<string, List<double>>();
for (int i = 0; i < sequences.Count; i++)
    {
     // Unique key created and added to dictionary for HTM Input                
     string key = "S" + (i + 1);
     List<double> value = sequences[i];
     dictionary.Add(key, value);
    }
     return dictionary;
```
* After that, we have RunHTMModelLearning method of [HTMModeltraining](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/HTMModeltraining.cs) class to train our model using the converted sequences. The numerical data sequences from training (for learning) and predicting folders are combined before training the HTM engine. This class returns our trained model object predictor.
```csharp
.....
MultiSequenceLearning learning = new MultiSequenceLearning();
predictor = learning.Run(htmInput);
.....
.....
List<List<double>> combinedSequences = new List<List<double>>(sequences1);
combinedSequences.AddRange(sequences2);
.....
```
* In the end, we use [HTMAnomalyTesting](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/HTMAnomalyTesting.cs) to detected anomalies in sequences read from files inside predicting folder. All the classes explained earlier- CSV files reading (CSVFileReader), combining and converting them for HTM training (CSVToHTMInput) and training the HTM engine (using HTMModelTraining) will be used here. We use the same class (CSVFolderReader) to read files for our predicting sequences. TrimSequences method is then used to trim sequences for anomaly testing. Method for trimming is already explained earlier.
```csharp
.....
CSVFolderReader testseq = new CSVFolderReader(_predictingFolderPath);
var inputtestseq = testseq.ReadFolder();
var triminputtestseq = CSVFolderReader.TrimSequences(inputtestseq);
.....
```
Path to training and predicting folder is set as default and passed on the constructor, or can be set inside the class manually.

```csharp
.....
 _trainingFolderPath = Path.Combine(projectbaseDirectory, trainingFolderPath);
_predictingFolderPath = Path.Combine(projectbaseDirectory, predictingFolderPath);
.....
```
In the end, DetectAnomaly method is used to detect anomalies in our trimmed sequences one by one, using our trained HTM Model predictor. 
```csharp
foreach (List<double> list in triminputtestseq)
       {
         .....
         double[] lst = list.ToArray();
         DetectAnomaly(myPredictor, lst);
       }
```
Exception handling is present, such that errors thrown from DetectAnomaly method can be handled (like passing of non-numeric values, or number of elements in list less than two).

DetectAnomaly is the main method which detects anomalies in our data. It traverses each value of a list one by one in a sliding window manner, and uses trained model predictor to predict the next element for comparison. We use an anomalyscore to quantify the comparison and detect anomalies; if the prediction crosses a certain tolerance level, it is declared as an anomaly.

In our sliding window approach, naturally the first element is skipped, so we ensure that the first element is checked for anomaly in the beginning.

We can get our prediction in a list of results in format of "NeoCortexApi.Classifiers.ClassifierResult`1[System.String]" from our trained model Predictor using the following:

```csharp
var res = predictor.Predict(item);
```
Here, assume that item passed to the model is of int type with value 8. We can use this to analyze how prediction works. When this is executed,
```csharp
foreach (var pred in res)
 {
   Console.WriteLine($"{pred.PredictedInput} - {pred.Similarity}");
    }
```
We get the following output.
```
S2_2-9-10-7-11-8-1 - 100
S1_1-2-3-4-2-5-0 - 5
S1_-1.0-0-1-2-3-4 - 0
S1_-1.0-0-1-2-3-4-2 - 0
```
We know that the item we passed here is 8. The first line gives us the best prediction with similarity accuracy. We can easily get the predicted value which will come after 8 (here, it is 1), and previous value (11, in this case). We use basic string operations to get our required values.

We will then use this to detect anomalies.

* When we iteratively pass values to DetectAnomaly method using our sliding window approach, we will not be able to detect anomaly in the first element. So, in the beginning, we use the second element of the list to predict and compare the previous element (which is the first element). A flag is set to control the command execution; if the first element has anomaly, then we will not use it to detect our second element. We will directly start from second element. Otherwise, we will start from first element as usual.

* Now, when we traverse the list one by one to the right, we pass the value to the predictor to get the next value and compare the prediction with the actual value. If there's anomaly, then it is outputted to the user, and the anomalous element is skipped. Upon reaching to the last element, we can end our traversal and move on to next list.

We use anomalyscore (difference ratio) for comparison with our already preset threshold. When it exceeds, probable anomalies are found.

To run this project, use the following class/methods given in [Program.cs](https://github.com/sohelranalive/neocortexapi-CodeHive/blob/master/source/MySEProject/AnomalyDetectionSample/Program.cs).

```csharp
 HTMAnomalyTesting tester = new HTMAnomalyTesting();
 tester.Run();
```

## Results and Discussion

<p align='Justify'>
After running this project, we got the following [output](). 

The amount of anomalies found in various numerical data sequences is displayed visually in figure 4. While the y-axis provides various numerical value sequences, the x-axis shows the number of anomalies. various sequences have various anomaly counts. Some sequences have more anomalies than others. Five numerical values make up each sequence, indicating that the dataset includes several five element sequences for which anomaly detection was carried out. The bars' horizontal alignment makes it easy to compare the sequences and identify which ones have more oddities. Heterogeneous patterns within the sequences are suggested by the variation in anomaly numbers. Higher anomaly counts in some sequences could be a sign of outliers, recurrent systematic mistakes, or changes in the behavior of the data. The dataset's regular patterns or steady trends may be represented by the sequences with fewer anomalies.
</p>

<div align="center">
  <img src='\_assets\anomalies per sequence.jpeg'/>
</div>

<p align='center'>Figure 4: Anomalies per sequence</p>

<p align='Justify'>
Here we got time-series comparison plot in figure 5 showing the relationship between actual values, predicted values, and detected anomalies over a sequence of indexed data points. The actual values, represented by a black solid line, show fluctuations over time, while the predicted values, depicted as a blue dashed line, indicate the expected trend. Significant deviations between these two lines are marked as anomalies with red dots, suggesting instances where the actual values diverge notably from predictions. These anomalies may result from unexpected real-world events, sensor malfunctions, or model inaccuracies. The pattern of detected anomalies suggests that the predictive model struggles to capture sudden spikes or drops, indicating potential limitations in forecasting accuracy.
</p>

<div align="center">
  <img src='\_assets\actual vs predicted values with anomalies'/>
</div>

<p align='center'>Figure 5: Actual vs predicted values with anomalies</p>

<p align='Justify'>
We can observe that the false negative rate is high in our output (0.19). It is desired that false negative rate should be as lower as possible in an anomaly detection program. Lower false positive rate is also desirable, but not absolutely essential.

Although, it depends on a number of factors, like quantity (the more, the better) and quality of data, and hyperparameters used to tune and train model; more data should be used for training, and hyperparameters should be further tuned to find the most optimal setting for training to get the best results. We were using less amount of numerical sequences as data to demonstrate our sample project due to time and computational constraints, but that can be improved if we use better resources, like cloud. Besides, in order to get over these limitations, future research could look into advanced preprocessing techniques to improve the data's quality. Additionally, integrating deep learning approaches with ensemble techniques may increase the durability of the anomaly detection system. Future study could evaluate the model's performance in real-time applications and on different datasets to ensure its scalability and flexibility.
</p>

## Conclusion

<p align='Justify'> 
To apply of an anomaly detection system using Hierarchical Temporal Memory(HTM) highlights the capacity of biologically-inspired machine learning models to process sequential data and identify irregular patterns effectively. By following HTM's unique architecture, which inspired from the human brain's neocortex, the system demonstrate its strength in learning temporal sequences and identifying irregularities in the dataset with better degree of accuracy.
</p>
