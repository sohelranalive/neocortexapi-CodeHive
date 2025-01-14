# ML 24/25-03 Implement Anomaly Detection Sample

## Overview:

- [Problem Statement](#Problem-Statement)
- [Introduction](#Introduction)
- [Objectives](#Objectives)
- [HTM Basics](#HTM-Basics)
- [Requirements](#Requirements)
- [Project Structure](#Project-Structure)
- [Project Structure](#Data-Preparation)
- [HTM Model Configuration](#HTM-Model-Configuration)
- [Model Training and Learning Process](#Model-Training-and-Learning-Process)
- [Anomaly Detection Process](#Anomaly-Detection-Process)
- [Evaluation Metrics and Analysis](#Evaluation-Metrics-and-Analysis)
- [Challenges and Limitations](#Challenges-and-Limitations)
- [Optimization and Future Scope](#Optimization-and-Future-Scope)
- [Results and Discussion](#Results-and-Discussion)
- [Conclusion](#Conclusion)

## Problem Statement

The initial challenge to apply a that can accurately identify the anomalies in numeric time-series data using Hierarchical Temporal Memory(HTM). The problem involves teaching the HTM model to identify the underlying patterns from the train dataset, then using the knowledge to predict and identify irregularities in the test dataset. Anomalies can be defined as data points that deviate significantly from the expected range or pattern. The aim of the project is to simulate a real-world scenario by generating artificial data to train and test the system. Detecting irregularities accurately is critical for applications in areas like network monitoring, fraud detection and predictive maintenance.

## Introduction

Hierarchical Temporal Memory(HTM) is a machine learning algorithm which is inspired from the neocortex of the human brain. HTM excels at recognizing temporal patterns and making predictions in time-series data. For taking input data efficiently and robustly HTM used Sparse Distributed Representations(SDRs).


Figure 1: HTM is inspired from neocortex of human brain. 

In the project, the NeoCortexAPI – a .NET implementation of the HTM framework – will be used to make an anomaly detection system. The project include two parts:

* 1. Training: The HTM model trains from the normal numeric sequences, such as network traffic loads, from artificially created data.

* 2. Testing: The trained model is tested on new sequences containing both normal data and anomalies. The model identifies  anomalies based on deviations from predicted values. 

The project will used C# and the NeoCortexAPI library to process the data, train the HTM model, and evaluate the performance. The main objective of the project is to determine a robust and efficient system which can accurately predict the anomalies while analyzing the results using metrics like False Negative Rate(FNR)  and False Positive Rate(FNR).

The anomaly detection helps to identify any unusual traffic patterns or anomalies in the network such as cyberattacks or system failures. Moreover it is used for fraud detection in financial transactions. For monitoring machine and equipment performance and detecting anomalies to prevent breakdowns. The model can also be used to detect diseases on the human body or energy consumption to survey irregularities and optimize energy distribution.

## Objectives

The primary objective of the project is to create and demonstrate an anomalies detection system using HTM. The specific goals include: 

* Feature Engineering
Generate artificial numeric data representing network traffic load percentages. Also prepare training data with normal sequences and testing data with random anomalies.

* HTM Model Training

Configure and train the HTM model using the NeoCortexAPI to identify normal patterns from the training dataset.

* Anomaly Detection

Using the trained HTM model to test predicting data and identify anomalies by comparing actual and the predictive values.

* Performance Evaluation
Measure the system’s effectiveness using performance metrics using False Negative Rate(FNR), False Positive Rate(FPR), Mean Square Error(MSE) etc.

By following the steps, I tried to complete the project, which is the practical application of the HTM model for detecting anomalies in time-series data and highlighting its strength and limitations.


## HTM Basics

A theoretical framework for comprehending and modelling how the human neocortex processes information is called Hierarchical Temporal Memory (HTM). It focusses on identifying temporal patterns and formulating predictions using them, and it draws inspiration from neurology. HTM works very effectively for detecting anomalies.HTM contrasts the real input SDR with the anticipated SDR during inference. The HTM quantifies the variance by assigning an anomaly score in the event that the input and the prediction do not match. Unusual or unexpected inputs are detected in real time using the anomaly score.


## Requirements

	### Software Requirements:

 		*.NET Framework/SDK: Version 7.0 or higher.
 		* NeoCortexAPI: Library for implementing sequence learning and prediction.
 		* IDE: Visual Studio 2022 or any compatible .NET development environment.

	### Dependencies:

		* NeoCortexAPI NuGet package (NeoCortexApi Version= 1.1.4 For code debugging).
		* CSV file handling libraries (optional, use in-built .NET functionality).

## Data Preparation

Data preparation is one of the most tricky step in the project as it ensures the model is trained and tested wit appropripate, well-structed data. In the project numeric values are stored in the .csv file, representing time-series data. This explicit real-workd scenarios, such as network load percentages with normal data and anomalies strategically included in separate datasets.

* Input Data Overview
The data consist of numeric sequences representing network load values in percentages. The range of the values between 0 to 100 and normal values are typically within the range of 45 to 55. The dataset has two categories e.g, one is training dataset and another one is testing dataset. The train data follows the numeric order where the testing data contains random sequences.

* Folder Structure
Data is organised with two folders, where one folder contains train_data and another folder contains predict_data. 

 
