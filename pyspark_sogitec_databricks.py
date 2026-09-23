# Projet SOGITEC Suresnes - 7112769
# Blanchard IYA BONZOLO - ISC Bandundu
# Data Engineering PySpark - Databricks

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SOGITEC-Suresnes-7112769").getOrCreate()

data = [("A350", "Suresnes", 150), ("Rafale", "Brest", 80), ("A320", "Suresnes", 200)]
df = spark.createDataFrame(data, ["Avion", "Site", "Heures_Sim"])

df_suresnes = df.filter(col("Site") == "Suresnes")
df_suresnes.show()

print("Projet Data Engineering - Pret pour SOGITEC Suresnes!")
