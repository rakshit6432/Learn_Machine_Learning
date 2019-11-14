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



<h2>Information Integration</h2>


<h3>Overview of Information Integration</h3>

Information integration refers to the problem of using many different information sources to accomplish a task.

Information integration system is a software that makes independent data appear as though they are together as a single database.

Querying multiple different data sources and combining their results, is called an integrated view. It is integrated because the data is retrieved from different data sources, and it's called a view because in database terminology it is a relation computed from other relations.

To populate the integrated view we need to go through a step called schema mapping. The term mapping means to establish correspondence between the attributes of the view, which is also called a target relation, and that of the source relations. For example, below is the schema mapping you would need if you want to find customers who have an account in the Insurance data and the Banking data:

<img src="../3. Big Data Integration and Processing/images/schema_mapping.png">

How do we query? For example, how do you find the bank account number of a person whose policyKey is known?

```sql
select AcctNumber from discountCandidates where policyKey='4-9375528734';
```

This is pretty straightforward, but the way the query will be evaluated depends on the query architecture of the data integration system. The figure below shows the elements of this architecture.

<img src="../3. Big Data Integration and Processing/images/integrated_data.png">

The vertical z axis specifies whether we have one data source or multiple data sources. The x axis asks whether the integrated data is actually stored physically in some place or whether it is computed on the fly, each time a query is asked. If it is all precomputed and stored, we say that the data is materialized. And if it is computed on the fly, we say it's virtual. The y axis asks whether there is a single schema or global schema defined all over the data integrated for an application or whether the data stay in different computers and it is accessed in a peer-to-peer manner at runtime.

_Record linkage problem_ means we would like to ensure that the set of data records that belong to a single entity are recognized, perhaps by clustering the values of different attributes or by using a set of matching rules so that we know how to deal with it during the integration process.

In a Big Data situation, there are dozens of data sources or more because the company's growing and each source may have a few hundred tables. So it becomes very hard to solve mapping to target problem completely and accurately just because the number of combinations one has to go through is really, really high.

One practical way to tackle this problem is not to do a full-scale data integration in the beginning but adopt what's called a pay-as-you-go model. The pay-as-you-go data management principle is simple. The system should provide some basic integration services at the outset and then evolve the schema mappings between the different sources on an as needed basis. So given a query, the system should generate a best effort or approximate answers from the data sources where a perfect schema mappings do not exist. One approach to do the first approximate schema mapping is called _Probabilistic Schema Mapping_.

In Probabilistic Mediated Schema Design, we answer the question of which data combinations should go together when creating an integrated or mediated schema by joining multiple data sources by associating probability values with each of these options. To compute these values, we need to quantify the relationships between attributes by figuring out which attributes should be grouped or clustered together.

Now two pieces of information available in the source schemas can serve as evidence for attribute clustering. One, the parallel similarity of source attributes, and two, statistical properties of service attributes.

- The first piece of information indicates when two attributes are likely to be similar and is used for creating multiple mediated schemas. One can apply a collection of attribute matching modules to compute pairwise similarity.

- The second piece of information indicates when two attributes are likely to be different, and is used for assigning probabilities to each of the mediated schemas.

For large schemas with large data volumes, one can estimate these measures by taking samples from the actual database to come up with reasonable similarity co-occurrence scores.

<h3>A Data Integration Scenario</h3>

There are several techniques of specifying schema mappings. One of them is called _Local-as-View_. This means we write the relations in each source as a view over the target schema.

<img src="../3. Big Data Integration and Processing/images/lav.png">

The SQL query shown here is straightforward but how do you translate this query so that it can be sent to the sources? Ideally this should be simplest query with no extra operations. To find such an optimal query reformulation, it turns out that this process is very complex and becomes worse as a number of sources increases. Thus query reformulation becomes a significant scalability problem in a big data integration scenario.

For example, let's say there is a governing organization that wants to connect all the health care service provider data to provide better healthcare to patients and they have developed a Reference Information Model (RIM) global schema and expects to use that as a standard. But each healthcare provider can have different schemas, same kind of data with different representations (data variety problem), different implementation standards and on top of it each provider can have large amount of data. So the data integration system's job is to transform the data from the source schema to the schema of the receiving system, the RIM. This is sometimes called the _data exchange problem_.

Informally a data exchange problem can be defined like this: Given a number of relations, a set of schema mappings, and a set of constraints, that the target schema must satisfy, the data exchange problem is to find a finite target database such that both the schema mappings and the target constraints are satisfied.

This can be achieved by:

- Format Conversions: is standardizing schemas and values. For example, the 50 states of the US all have two letter abbreviations. This helps us generalize and have a set of codes available for conversion.

- Constraints: are imposed by the target and source schema. For example, a source may not distinguish between an emergency surgical procedure and a regular surgical procedure. But the target may want to put them in different tables.

- Compressed Data: refers to a way of creating an encoded representation of data. So that this encoder form is smaller than the original representation. A common encoding method is called dictionary encoding. Consider a database with 10 million record of patient visits a lab. Each record indicates a test and its results and we store the data in a column stored relational database rather than a row store relational database. Suppose there are a total of 500 tests so this separate table called the dictionary has 500 rows, which is clearly much smaller than ten million. But if you can't reduce the full data and need to store the 10 million rows, we can compress the data and operate on the compressed data.

- Model transformation: is a process of taking data represented in one model in one source system and converting it to an equivalent data in another model the target system.

- Query transformation: is the process of taking a query on the target schema and converting it to a query against a different data model.

<h3>Integration for Multichannel Customer Analytics</h3>

Data Fusion: Consider a set of data sources, S and a set of data items, D. A data item represents a particular aspect of a real world entity, for each data item, a source can, but not necessarily will, provide a value. The value can be atomic, like good, or a set, or a list or sometimes embedded in the string. The goal of Data Fusion is to find the values of Data Items from a source. In other cases, we could find a value distribution of an item.

Now one obvious problem with the Internet is that there are too many data sources at any time, these lead to many difficulties. First, it is to be understood that with too many data sources there will be many values for the same item. Often these will differ and sometimes they will conflict. A standard technique in this case is to use a voting mechanism.

One of the problems is to estimate the trustworthiness of the source. For each data source, we need to evaluate whether it's reporting some basic or known facts correctly.

Source Selection is the problem of  evaluating the worthiness of sources before information integration.


<h2>Industry Examples for Big Data Integration and Processing</h2>


<h3>Why Splunk?</h3>

Splunk was founded to pursue a disruptive vision to make machine data accessible, usable, and valuable to everyone.



<h1>Week 4: Processing Big Data</h1>



<h2>Big Data Pipelines and High-level Operations for Big Data Processing</h2>


<h3>Big Data Processing Pipelines</h3>



<h3>Some High-Level Processing Operations in Big Data Pipelines</h3>



<h3>Aggregation Operations in Big Data Pipelines</h3>



<h3>Typical Analytical Operations in Big Data Pipelines</h3>




<h2>Big Data Processing Tools and Systems</h2>


<h3>Overview of Big Data Processing Systems</h3>



<h3>Big Data Workflow Management</h3>



<h3>The Integration and Processing Layer</h3>



<h3>Introduction to Apache Spark</h3>



<h3>Getting Started with Spark</h3>




<h1>Week 5: Big Data Analytics using Spark</h1>









<h1>Week 6: Learn By Doing: Putting MongoDB and Spark to Work</h1>
