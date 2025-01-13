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

In the project, the NeoCortexAPI – a .NET implementation of the HTM framework – will be used to make an anomaly detection system. The project include two parts:

* 1. Training : The HTM model trains from the normal numeric sequences, such as network traffic loads, from artificially created data.

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

 
