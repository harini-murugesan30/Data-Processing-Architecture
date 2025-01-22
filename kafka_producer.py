 from kafka import KafkaProducer
import json
import csv
import time

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Function to send CSV data to Kafka
def send_data_to_kafka(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            message = ','.join(row)
            producer.send('sentiment_topic', value=message.encode('utf-8'))
            print(f'Sent: {message}')
            time.sleep(1)

if __name__ == "__main__":
    send_data_to_kafka('training.1600000.processed.noemoticon.csv')