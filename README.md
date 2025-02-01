# Data Engineering Project

This project implements a **batch-processing-based data architecture** for a machine learning application. The system ingests, stores, preprocesses, and aggregates data for quarterly model updates.

## Components
- **Apache Kafka**: Handles data ingestion.
- **HDFS**: Stores raw data.
- **Apache Spark**: Preprocesses and aggregates data.
- **Flask API**: Serves processed data to the machine learning application.
- **Docker**: Containerizes all components for isolated and consistent environments.
- **Terraform**: Implements Infrastructure as Code (IaC) for reproducible setups.

## Dataset
The dataset used is the [Sentiment140 dataset](https://www.kaggle.com/datasets/kazanova/sentiment140), containing 1.6 million tweets.

## Setup Instructions
1. Clone this repository.
2. Run `docker-compose up` to start the system.
3. Ingest data using Kafka.
4. Process and aggregate data using Spark.
5. Serve processed data via the Flask API.

## License
This project is licensed under the MIT License.