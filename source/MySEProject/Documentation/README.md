# ML 24/25-03 Implement Anomaly Detection Sample

## Overview:

- [Problem Statement](#Problem-Statement)
- [Introduction](#Introduction)
- [Objectives](#Objectives)
- [HTM Basics](#HTM-Basics)
- [Requirements](#Requirements)
- [Project Structure](#Project-Structure)
- [Project Methodology](#Project-Methodology)
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

<p align='Justify'>Some content will be added here (Ashiq)</p>

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

## Results and Discussion

<p align='Justify'> Working fine. Initial test done </p>

## Conclusion

<p align='Justify'> 
To apply of an anomaly detection system using Hierarchical Temporal Memory(HTM) highlights the capacity of biologically-inspired machine learning models to process sequential data and identify irregular patterns effecitively. By following HTM's unique architecture, which inspiredfrom the human brain's neocortex, the system demonstrate its strength in learning temporal sequeces and indentifying irregularities in the dataset with better degree of accuracy.

 </p>
