# ResSDN: A Machine Learning-based Tool for Joint QoS-Security Optimization in Software-Defined Networking
This repository contains the Python code, datasets, PCAP files, and machine learning models developed for *ResSDN*, a novel approach in Software-Defined Networking (SDN) that applies machine learning to optimize both Quality of Service (QoS) and security. This project is part of my Doctor of Engineering praxis at George Washington University.

## Project Overview
*ResSDN* aims to address the balance between security and performance in SDN environments. By leveraging machine learning algorithms, *ResSDN* enhances security while maintaining or improving QoS, providing a resilient and efficient network framework.

### Key Components
- **Code**: Scripts and modules implementing ResSDN’s machine learning models, feature extraction, and network optimization algorithms.
- **Dataset**: Network data collected from SDN environments, including traffic flow information, QoS metrics, and security incidents, formatted for machine learning training and evaluation.
- **Pcap**: Network captures used for traffic analysis and feature extraction.
- **Model**: Pre-trained and/or fine-tuned models designed to predict and optimize QoS-security metrics in real-time.

## Repository Structure
|-- Code/
|   |-- dataset_preprocessing.py
|   |-- main1.py
|   |-- main2.py
|   |-- testdata.py
|   |-- valcode.py
|-- Dataset/
|   |-- Victim1_Output.csv
|   |-- Victim2_Output.csv
|   |-- Victim3_Output.csv
|   |-- combined_file.csv
|   |-- Train_Data.csv
|   |-- Vali_Data.csv
|-- Pcap/
|   |-- Victim1_PC18.pcap
|   |-- Victim2_DK16.pcap
|   |-- Victim3_VM11.pcap
|-- Model/
|   |-- C_LightGBM_Model.joblib
|   |-- C_Random Forest_Model.joblib
|   |-- C_Stacking_Model.joblib
|   |-- C_XGBoost_Model.joblib
|   |-- R_BiGRU_Model.h5
|   |-- R_GRU_Model.h5
|   |-- R_LSTM_Model.h5
|-- README.md

### Descriptions of Key Files
- dataset_preprocessing.py: Script for preprocessing the collected PCAP files with Scapy.
- Main1.py: Script for processing dataset for security optimization.
- Main2.py: Script for processing dataset for QoS optimization.
- PraxisDataset1.csv: Preprocessed dataset with Scapy, formatted as CSV files.
- Victim1_PC18.pcap: Traffic captured from the 1st Victim VM.
- Victim2_DK16.pcap: Traffic captured from the 2nd Victim VM.
- Victim3_VM11.pcap: Traffic captured from the 3rd Victim VM.

## Results and Evaluation
Results from this project, including trained models and evaluations, are detailed in my praxis paper. The models have been tested on simulated datasets to validate ResSDN’s effectiveness in balancing QoS and security in SDN environments.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
This project was developed as part of my Doctor of Engineering praxis at George Washington University, and I would like to thank my advisors, peers, and the academic community for their invaluable guidance.
