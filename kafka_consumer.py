from kafka import KafkaConsumer
from hdfs import InsecureClient
import os

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'sentiment_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# Initialize HDFS client
hdfs_client = InsecureClient('http://localhost:50070', user='root')

def store_to_hdfs():
    if not hdfs_client.status('/sentiment140', strict=False):
        hdfs_client.makedirs('/sentiment140')
    
    # Read messages from Kafka and store to HDFS
    with hdfs_client.write('/sentiment140/sentiment_data.csv', encoding='utf-8') as writer:
        for message in consumer:
            writer.write(message.value.decode('utf-8') + '\n')
            print(f'Stored: {message.value.decode('utf-8')}')

if __name__ == "__main__":
    store_to_hdfs()