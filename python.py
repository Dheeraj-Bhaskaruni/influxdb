from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# Replace these variables with your details
token = "5rjxBQ3DTYxirUZR0dU2xnDOMGSW_kbZisoZrA8zT0m9pzEb6upuPhmHJ8EG7GNEbAZIEaikOZKngoy9_3x6iQ=="
org = "automation"
bucket = "new"

# Connect to InfluxDB
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

# Create a point (sample data)
point = Point("weather").tag("location", "San Francisco").field("temperature", 25.3).time(time=datetime.utcnow(), write_precision=WritePrecision.NS)

# Write data
write_api.write(bucket=bucket, org=org, record=point)

# Always close the client when done
client.close()
