<h1>Week 1: Introduction to Big Data Integration and Processing</h1>



<h2>Why Big Data Integration and Processing?</h2>


<h3>Summary of Big Data Modeling and Management</h3>

A data model as a specification that precisely characterizes the structure of the data, the operations on the data, and the constraints that may apply on data.

Database management systems handle low level data management operations, help organization of the data using a data model, and provide an open programmable access to data.

Four Data Models:
1. _Relational data_: is structured like tables which are formally called relations. The relational data model has been implemented in traditional database systems. But they are being refreshly implemented in modern data systems over Hadoop and Spark and are getting deployed on cloud platforms.

2. _Semi-structured data_: includes documents like HTML pages, XML data and JSON data that are used by many Internet applications. This data can have one element nested or embedded within another data element and hence can often be modeled as a tree.

3. _Graph data_: is a network where nodes represent entities and edges represent relationships between pairs of such entities, for example social networks and email networks.

4. _Text data_: is much more unstructured because an entire data item like a new article can be just a text string.

_Streaming data_, or data with velocity, is a special class of data that continually come to the system at some data rate. Streaming data is special because a stream is technically an infinite data source. And therefore, we keep filling up memory and storage and will eventually go beyond the capacity of any system. Streaming data, therefore, needs a different kind of management system. For this reason, streaming data is processed in chunks(windows). Often only the necessary part of the data stream or the results of queries against the data stream is stored.

<img src="../3. Big Data Integration and Processing/images/dbms_bdms.png">

<h3>Why is Big Data Processing Different?</h3>

__Requirements for Big Data Systems:__

1. Support Big Data Operations
    - Split Volumes of data
    - Access data fast
    - Distribute computations to nodes

2. Handle Fault Tolerance
    - Replicate data partitions
    - Recover files when needed

3. Enable adding more racks (Scaling out) without losing performance

4. Optimized and extensible for many data types

5. Enable both streaming and batch processing
    - _Low latency_ processing of streaming data
    - _Accurate_ processing of all available data

<img src="../3. Big Data Integration and Processing/images/3Vs.png">


<h2>Querying Data Part 1</h2>


<h3>What is Data Retrieval? Part 1</h3>

Data retrieval refers to the way in which data desired by a user is specified and retrieved from a data store.

A query language is a language in which a retrieval request is specified. A query language is often called declarative, which means it lets you specify what you want to retrieve without having to tell the system how to retrieve. For example, SQL, structured query language, it is the most used query language for relational data. Now, in contrast to a query language, a database programming language like Oracle's PL/SQL or Postgres's PgSQL are high-level procedural programming languages that embed query operations.

The most basic structure of a sql query is given below:

<img src="../3. Big Data Integration and Processing/images/basic_sql.png">

This form of query can also be represented as a selection operation on the relation Beers with a condition on the manf attribute, followed by a projection operation that outputs the name attribute from the result of the selection operation. This is given inside the black box in the image above.

Below are some more advanced sql queries:

<img src="../3. Big Data Integration and Processing/images/more_sql_examples.png">

The DISTINCT ensures that the result has no duplicates.

<h3>What is Data Retrieval? Part 2</h3>

If the table was large and had millions of entries, the table would possibly need to be split over many machines. Another way of saying that is that the table will be partitioned across a number of machines. Since a query simply performs a selection and projection here, it can be evaluated in parallel.

One standard way of partitioning the data is called a range partitioning by the primary key. This simply means that the rows of the table are put in groups depending on the alphabetical order of the name value. Below you can see how to query partition tables:

<img src="../3. Big Data Integration and Processing/images/queries_in_large.png">

When we use like, we're telling the query engine that we only have partial information about the string we want to match. This partly specified string is called a _string pattern_. There is this part of the string we know and a part that we do not know and for the part we don't know, we use the `%`. If we wanted to find, say, Am somewhere in the middle of the string, we would write the pattern as `%Am%`.

<h3>Querying Two Relations</h3>

<img src="../3. Big Data Integration and Processing/images/query_two_relations.png">

<h3>Subqueries</h3>

Let's look into a more complex query, "Find the bars that serve Miller for the same or less price than what TGAB charges for Bud". We can break it into two queries:
1. Find the price TGAB charges for Bud
2. Find the bars that serve Miller at that price

Now this is a classic situation where the result from the first part of the query should be fed as a parameter to the second query. Now this situation is called a subquery.

```sql
select bar
from sells
where beer = 'Miller' and
    price <= (select price
              from sells
              where bar = 'TGAB'
              and beer = 'bud'
              );
```

The part after price is called the _inner query_ or the _subquery_. Notice that the inner query is independent of the outer query. In other words, even if we did not have the outer query, we can still evaluate the inner query. We say in this case that the subquery is uncorrelated.

Let's look at another example:

<img src="../3. Big Data Integration and Processing/images/subquery_example.png">

Example of a correlated subquery:

<img src="../3. Big Data Integration and Processing/images/correlated_subquery.png">

__Aggregate queries:__

<img src="../3. Big Data Integration and Processing/images/aggregate_queries.png">

__Groupby queries:__

<img src="../3. Big Data Integration and Processing/images/groupby_queries.png">



<h1>Week 2: Retrieving Big Data (Part 2)</h1>



<h2>Querying Data Part 2</h2>


<h3>Querying JSON Data with MongoDB</h3>

Just like a basic SQL query states, which parts of which records from one or more table should be reported, a MongoDB query states which parts of which documents from a _document collection_ should be returned.

The primary query is expressed as a find function, which contains two arguments and an optional qualifier:

```sql
db.collection.find(<query filter>, <projection>).<cursor modifier>
```

There are four things to notice in this function:

<img src="../3. Big Data Integration and Processing/images/mongodb_find.png">

The same query in both SQL and MongoDB:

```sql
---------------------------- Query 1: ----------------------------
-- sql
select * from beers;

-- mongodb
db.beers.find()

---------------------------- Query 2: ----------------------------
-- sql
select beer, price from sells;

-- mongodb
db.sells.find({}, {beer:1, price:1})
-- Query condition is empty because we need to return all queries
-- The 1 in the projection clause means we have an output,
-- we can use 0 to specify no output

---------------------------- Query 3: ----------------------------
-- sql
select manf from beers where name='Heineken';

-- mongodb
db.beers.find({name:"Heineken"}, {manf:1, _id:0})

---------------------------- Query 4: ----------------------------
-- sql
select distinct beer, price from sells where price>15;

-- mongodb
db.sells.distinct({price:{$gt:15}}, {beer:1, price:1, _id:0})
```

__Some MongoDB Operators:__

<img src="../3. Big Data Integration and Processing/images/mongodb_operators.png">

The other MongoDB operators can be found in their [docs](https://docs.mongodb.com/manual/reference/operator/query/).

MongoDB uses regular expressions to specify partial string matches. For example

```sql
---------------------------- Query 5: ----------------------------
-- Count the number of manufacturers whose names have the partial
-- string "am" in it- must be case insensitive
db.beers.find(name:{$regex:/am/i}).count()
-- 'i' specifies case insensitive
db.beers.find({name: /am/i}).count() -- Usage in MongoDB

---------------------------- Query 6: ----------------------------
-- Same query as above but name starts with "Am"
db.beers.find(name:{$regex:/^Am/}).count()
db.beers.find({name: /^Am/}).count() -- Usage in MongoDB

---------------------------- Query 7: ----------------------------
-- Starts with "Am" and ends with "corp"
db.beers.count(name:{$regex:/^Am.*corps$/})
db.beers.find({name: /^Am.*corps/}).count() -- Usage in MongoDB

```

__Array Operations:__

<img src="../3. Big Data Integration and Processing/images/mongodb_array_ops.png">

__Compound Statements:__

<img src="../3. Big Data Integration and Processing/images/mongodb_compounds.png">

__Queries over Nested Elements:

<img src="../3. Big Data Integration and Processing/images/mongodb_nested.png">

<h3>Aggregation Functions</h3>

__On Counting and Distinct:__

<img src="../3. Big Data Integration and Processing/images/mongodb_count.png">

__Aggregation Framework:__

MongoDB uses an internal machinery called the aggregation framework, which is modeled on the concept of data processing pipelines. That means documents enter a multi-stage pipeline which transforms the documents at each stage until it becomes an aggregated result.

<img src="../3. Big Data Integration and Processing/images/mongodb_agg.png">

In the example here cust_id is the grouping attribute so it is passed as a parameter to the `$group` function. Now notice the syntax. `_id:$cust_id` says that the grouped data will have an _id attribute, and its value will be picked from the cust_id attribute from the previous stage of computation. Thus, the `$` before the cust_id is telling the system that cust_id is a known variable in the system and not a constant. The `$group` operation also needs a reducer, which is a function that operates on an activity to produce an aggregate result. In this case, the reduce function is sum

__Multi-attribute Grouping:__

As we saw in the relational case, data can be partitioned into chunks on the same machine or on different machines. These chunks are called _chards_. The aggregation pipeline of MongoDB can operate on a charded collection. The grouping operation in MongoDB can accept multiple attributes like the four shown here:

```sql
db.computers.aggregate(
    [
        {
            $group: {
                _id: {brand: "$brand", title: "$title", category: "$category", code:"$code"},
                count:{$sum: 1}
            }
        }
        {
            $sort: {count:1, category:-1}
        }
    ]
)
```

Also shown above is a post grouping directive to sort on the basis of two attributes. The first is a computed count variable in ascending order. So the one designates the ascending order. The next sorting attribute is secondary. That means if two groups have the same value for count, then they'll be further sorted based on the category value. But this time the order is descending because of the -1 directive.

__Text Search with Aggregation__

MongoDB has a built in text search engine which can be invoked through the same aggregation framework.

```sql
db.articles.aggregate(
    [
        {$match: {$text: {$search: "Hillary Democrat"}}},
        {$sort: {score: {$meta: "textScore"}}},
        {$project: {title:1, _id:0}}
    ]
)
```

__Join in MongoDB:__

<img src="../3. Big Data Integration and Processing/images/mongodb_join_a.png">

<img src="../3. Big Data Integration and Processing/images/mongodb_join_b.png">

<h3>Querying Aerospike</h3>

Aerospike which is a key value store. Key value stores typically offer an API. That is the way to access data using a programming language like Python or Java.

The data model of Aerospike is illustrated here:

<img src="../3. Big Data Integration and Processing/images/aerospike.png">

Data are organized in name spaces which can be in memory or on flash disks. Name spaces are top level data containers. The way you collect data in name spaces relates to how data is stored and managed. So name space contains records, indexes, and policies. Now policies dictate name space behavior like how data is stored, whether it's on RAM or disk, or how how many replicas exist for a record, and when records expire.

A name space can contain sets, you can think of them as tables. Within a record, data is stored in one or many bins. Bins consist of a name and a value.



<h1>Week 3: Big Data Integration</h1>










<h1>Week 4: Processing Big Data</h1>









<h1>Week 5: Big Data Analytics using Spark</h1>









<h1>Week 6: Learn By Doing: Putting MongoDB and Spark to Work</h1>
