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

# Introduction:

Hierarchical Temporal Memory (HTM) is a biologically inspired machine learning algorithm designed to model the neocortex's functionality for sequence learning and anomaly detection. By utilizing a hierarchical network of nodes, HTM processes time-series data in a distributed manner, where each node identifies and learns recurring patterns. This project implements an anomaly detection system using the NeoCortex API’s MultiSequenceLearning class. It ingests numerical sequences from multiple CSV files, trains the HTM engine to recognize temporal patterns, and detects anomalies by highlighting deviations from learned norms. This innovative method offers robust solutions for dynamic and predictive analysis in real-world scenarios.

# Requirements:

To run this project, we need.

- .NET 8.0 SDK
- Nuget package: NeoCortexApi Version= 1.1.4
  For code debugging, we recommend using Visual Studio IDE/Visual Studio Code. This project can be run on github codespaces as well.

# Usage

To run this project,

- Install .NET SDK. Then using the code editor/IDE of your choice, create a new console project and place all the C# codes inside your project folder.
- Add/reference Nuget package NeoCortexApi v1.1.4 to this project.
- Place numerical sequence CSV Files (datasets) under relevant folders respectively. All the folders should be inside the project folder. More details are given below.
