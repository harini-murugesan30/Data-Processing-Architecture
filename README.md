# Batch-Processing-Based Data Architecture for a Data-Intensive Application

This project implements a **batch-processing pipeline** to handle data-intensive tasks, leveraging modern tools such as Docker, Kafka, HDFS, and Spark. It processes the **Sentiment140 dataset** for sentiment analysis, showcasing how large-scale data can be ingested, stored, processed, and analyzed efficiently.

---

## Architecture

![Architecture Diagram](https://github.com/harini-murugesan30/Data-Processing-Architecture/blob/main/images/Data_Architecture.png)

### Components:
- **Kafka**: Entry point for data ingestion, streaming raw data.
- **HDFS**: Stores raw and processed data.
- **Spark**: Processes and aggregates data stored in HDFS.
- **Flask API**: Delivers processed results to downstream applications.
- **Prometheus & Grafana**: Monitor system health and visualize metrics.
- **Docker**: Ensures isolated and consistent environments.

---

## Features
- **Real-time Data Streaming**: Tweets from the Sentiment140 dataset are streamed into Kafka.
- **Batch Data Storage**: Messages are retrieved from Kafka and efficiently stored in HDFS.
- **Sentiment Analysis**: Spark processes data, analyzing tweets based on sentiment.
- **Scalability**: Dockerized services ensure seamless scaling for real-world applications.
- **Monitoring**: Prometheus tracks metrics, while Grafana provides visual dashboards.

---

## Prerequisites
1. **Docker Desktop** (latest version)
2. **Python 3.8+** with the following libraries:
   - `kafka-python`
   - `pyspark`
3. **Git** installed locally.

---

## Usage Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/harini-murugesan30/Data-Processing-Architecture.git
   cd Data-Processing-Architecture

2. **Start Docker Containers**
   ```bash
   docker-compose up --build

3. **Stream Data into Kafka** Run the producer script to stream tweets:
   ```bash
   python producer.py

4. **Consume Data into HDFS** Run the consumer script to ingest data into HDFS:
   ```bash
   python consumer.py
   
5. **Process Data with Spark** Execute the Spark job to analyze stored data:
   ```bash
   spark-submit spark_job.py
   
6. **Verify Data Storage** Open the HDFS Web UI:
    ```bash
    http://localhost:9870
    
7. **Monitor the System**
    - Prometheus: http://localhost:9090
    - Grafana: http://localhost:3000

## Example Output
- **Processed Tweets**: Filtered tweets based on positive or negative sentiment.
- **HDFS Storage**: Data stored in /user/hdfs/sentiment-analysis/.

---

## Limitations
- **Latency**: Batch processing introduces inherent delays compared to real-time systems.
- **Scalability**: Performance may degrade with significantly larger datasets or resource constraints.

---

## Future Enhancements
- Implement more complex Spark transformations, such as keyword extraction or trend analysis.
- Add support for real-time dashboards using Flask and a frontend library.
- Automate deployment using CI/CD pipelines.

---

## Acknowledgments
- **Dataset**: [Sentiment140 dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)
- **Tools**: Apache Kafka, Hadoop HDFS, Apache Spark, Prometheus, Grafana, Docker.
