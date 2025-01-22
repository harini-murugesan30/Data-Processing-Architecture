from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Sentiment Analysis") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .getOrCreate()

# Load data from HDFS
df = spark.read.csv('hdfs://localhost:9000/sentiment140/sentiment_data.csv')

# Show some data
df.show()

# Example: Filter tweets with positive sentiment
positive_tweets = df.filter(df['_c0'] == 4)

# Save filtered data back to HDFS
positive_tweets.write.csv('hdfs://localhost:9000/sentiment140/positive_tweets.csv')

spark.stop()