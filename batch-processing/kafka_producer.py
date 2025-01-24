from kafka import KafkaProducer
import json
import csv

# Initialize Kafka Producer
def create_kafka_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers='localhost:9094',  # External listener for Kafka
            value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON serialization
        )
        print("Kafka Producer successfully connected.")
        return producer
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        return None

# Function to send CSV data to Kafka in batches
def send_data_to_kafka(producer, file_path, batch_size=100, max_rows=1000):
    if producer is None:
        print("Kafka Producer is not initialized. Exiting.")
        return

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)  # Use DictReader to work with column names
            batch = []
            for i, row in enumerate(reader):
                if i >= max_rows:  # Stop after max_rows for testing
                    break
                batch.append(row)
                if len(batch) >= batch_size:  # Send batch to Kafka
                    producer.send('sentiment_topic', value=batch)
                    print(f"Sent batch of {len(batch)} rows to Kafka.")
                    batch = []  # Reset the batch
            
            # Send any remaining rows
            if batch:
                producer.send('sentiment_topic', value=batch)
                print(f"Sent final batch of {len(batch)} rows to Kafka.")
        producer.flush()
    except Exception as e:
        print(f"Error sending data to Kafka: {e}")
    finally:
        producer.close()

if __name__ == "__main__":
    kafka_producer = create_kafka_producer()
    send_data_to_kafka(kafka_producer, 'training.1600000.processed.noemoticon.csv', batch_size=100, max_rows=1000)
