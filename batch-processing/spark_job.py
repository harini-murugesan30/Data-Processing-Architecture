from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, avg, max, count, hour, dayofmonth, month, split, explode
from pyspark.ml.feature import StopWordsRemover

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Sentiment Analysis Pipeline") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .getOrCreate()

# Load data from HDFS with proper schema
schema = "target INT, ids STRING, date STRING, flag STRING, user STRING, text STRING"
df = spark.read.csv('hdfs://localhost:9000/sentiment140/sentiment_data.csv', schema=schema, header=False)

# Rename columns for clarity
tweets_df = df.select(
    col("target").alias("sentiment"),
    col("ids").alias("id"),
    col("date"),
    col("flag"),
    col("user"),
    col("text").alias("tweet")
)

# Show some data
tweets_df.show()

# ========================
# 1. Sentiment Aggregation
# ========================
# Add a word count column
tweets_df = tweets_df.withColumn("word_count", length(col("tweet")) - length(col("tweet").replace(" ", "")) + 1)

# Aggregate sentiment data
sentiment_aggregation = tweets_df.groupBy("sentiment").agg(
    count("*").alias("count"),
    avg("word_count").alias("avg_word_count"),
    max("word_count").alias("max_word_count")
)

# Save sentiment aggregation results
sentiment_aggregation.write.mode("overwrite").csv("hdfs://localhost:9000/output/sentiment_aggregation")

# ========================
# 2. Time-Based Sentiment Trend
# ========================
# Extract hour, day, and month from the date
tweets_df = tweets_df.withColumn("hour", hour(col("date")))
tweets_df = tweets_df.withColumn("day", dayofmonth(col("date")))
tweets_df = tweets_df.withColumn("month", month(col("date")))

# Aggregate time-based sentiment trends
time_sentiment_trend = tweets_df.groupBy("sentiment", "hour").count()

# Save time-based sentiment trend results
time_sentiment_trend.write.mode("overwrite").csv("hdfs://localhost:9000/output/time_sentiment_trend")

# ========================
# 3. Keyword Extraction and Analysis
# ========================
# Tokenize tweets
tweets_df = tweets_df.withColumn("tokens", split(col("tweet"), " "))

# Remove stop words
stopwords = ["a", "the", "is", "in", "at", "of", "and", "to", "this", "that"]  # Add more as needed
remover = StopWordsRemover(inputCol="tokens", outputCol="filtered_tokens", stopWords=stopwords)

stopwords = StopWordsRemover.loadDefaultStopWords("english")
remover = StopWordsRemover(inputCol="tokens", outputCol="filtered_tokens", stopWords=stopwords)
tweets_df = remover.transform(tweets_df)

# Explode tokens into rows
tokens_df = tweets_df.withColumn("token", explode(col("filtered_tokens")))

# Group by sentiment and token to calculate frequency
keyword_analysis = tokens_df.groupBy("sentiment", "token").count().orderBy(col("count").desc())

# Save keyword analysis results
keyword_analysis.write.mode("overwrite").csv("hdfs://localhost:9000/output/keyword_analysis")

# Stop Spark session
spark.stop()