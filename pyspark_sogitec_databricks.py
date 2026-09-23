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
df.createOrReplaceTempView("simulations")

# Requête 1: Total A350 par site
resultat1 = spark.sql("""
    SELECT Site, SUM(Heures_Sim) AS total_heures
    FROM simulations
    WHERE Avion = 'A350' AND Site IN ('Suresnes', 'Brest')
    GROUP BY Site
""")
resultat1.show()

# Requête 2: Total par site et avion
resultat2 = spark.sql("""
    SELECT Site, Avion, SUM(Heures_Sim) AS tot_h
    FROM simulations
    GROUP BY Site, Avion
    ORDER BY tot_h DESC
""")
resultat2.show()
