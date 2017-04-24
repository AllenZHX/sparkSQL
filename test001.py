from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option","some-value").getOrCreate()
'''
df = spark.read.json("examples/src/main/resources/people.json")
df.show()
'''
'''
df.printSchema()
df.select("name").show()
df.select(df['name'],df['age']+1).show()
df.filter(df['age']>21).show()
df.groupBy("age").count().show()
'''
'''
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()
'''
'''
df.createGlobalTempView("people")
spark.sql("SELECT * FROM global_temp.people").show()
spark.newSession().sql("SELECT * FROM global_temp.people").show()
''' 
'''          
from pyspark.sql import Row
sc = spark.sparkContext
lines = sc.textFile("examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

schemaPeople = spark.createDataFrame(people)
schemaPeople.createOrReplaceTempView("people") 

spark.sql("SELECT * FROM people").show()
teenagers = spark.sql("SELECT name FROM people WHERE age>=13 AND age<=19")

teenNames = teenagers.rdd.map(lambda p: "Name: " + p.name)
for name in teenNames.collect():
	print(name)
'''
'''
from pyspark.sql.types import *
sc = spark.sparkContext

lines = sc.textFile("examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: (p[0],p[1].strip()))

schemaString = "name age"
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)

schemaPeople = spark.createDataFrame(people, schema)

schemaPeople.createOrReplaceTempView("people")
schemaPeople.printSchema()
temp = spark.sql("SELECT * FROM people").show()
results = spark.sql("SELECT name FROM people WHERE age<20")
results.show()
'''
'''
peopleDF = spark.read.json("examples/src/main/resources/people.json")
peopleDF.write.parquet("people.parquet")

parquetFile = spark.read.parquet("people.parquet")

parquetFile.createOrReplaceTempView("parquetFile")

teenagers = spark.sql("SELECT name FROM parquetFile WHERE age>=13 AND age<=19")

teenagers.show()
'''
'''
from pyspark.sql import Row
sc = spark.sparkContext

squaresDF = spark.createDataFrame(sc.parallelize(range(1,6)).map(lambda i: Row(single=i, double=i**2)))
squaresDF.write.parquet("data/test_table/key=1",mode="overwrite")
cubesDF = spark.createDataFrame(sc.parallelize(range(6,11)).map(lambda i: Row(single=i, triple=i**3)))
cubesDF.write.parquet("data/test_table/key=2", mode="overwrite")

mergedDF = spark.read.option("mergeSchema", "true").parquet("data/test_table")
mergedDF.printSchema()
'''
'''
parquetFile = spark.read.parquet("examples/src/main/resources/users.parquet")
parquetFile.createOrReplaceTempView("parquetFile")

teenagers = spark.sql("SELECT * FROM parquetFile")

teenagers.show()
'''
'''
sc = spark.sparkContext

path = "examples/src/main/resources/people.json"
peopleDF = spark.read.json(path)
peopleDF.printSchema()

peopleDF.createOrReplaceTempView("people")

spark.sql("SELECT * FROM people").show()

jsonStrings = ['{"name":"Hongxiang","address":{"city":"Jersey City","state":"NJ"}}']
otherPeopleRDD = sc.parallelize(jsonStrings)
otherPeople = spark.read.json(otherPeopleRDD)
otherPeople.show()
'''
'''
from pyspark.sql.types import *

schema = StructType([StructField("#",IntegerType(),True), StructField("Name",StringType(),True), StructField("Type 1",StringType(),True), StructField("Type 2",StringType(),True), StructField("Total",IntegerType(),True), StructField("HP",IntegerType(),True), StructField("Attack",IntegerType(),True), StructField("Defense",IntegerType(),True), StructField("Sp. Atk",IntegerType(),True), StructField("Sp. Def",IntegerType(),True), StructField("Speed",IntegerType(),True), StructField("Generation",IntegerType(),True),  StructField("Legendary",BooleanType(),True)])

pokemonDF = spark.read.csv("Pokemon.csv", header=True, mode="DROPMALFORMED",schema=schema)

pokemonDF.printSchema()

pokemonDF.createOrReplaceTempView("pokemon")

spark.sql("SELECT Name,HP FROM pokemon WHERE HP>150").show()
'''

clear
























