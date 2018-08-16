# Spark, Big Data Case study  

There are several goals of this case study:  
* Practice Spark  
* Practice AWS, including AMAZON EMR, S3, and boto3  
* Reinforce the utility of **working with a sub-sample of big data locally first** to get **rough estimates of the values you are looking for** and to **make sure your model works** BEFORE training on the full dataset (or a larger subset of the data) on S3.  
* Practice scoping a potentially extremely time-intensive project so that you have reliable results in just one day.  

All the datasets below can be found on [Amazon's Registry of Open Data on AWS](https://registry.opendata.aws/).  Specific links to the datasets are provided in the project descriptions.
<br/>  
### Option 1: The Common Crawl  
_Database size:_ more than 100 TB of data from more than 5 billion web pages (p.s. do NOT attempt 100 TB!)  
_S3 Amazon resource name:_ `arn:aws:s3:::commoncrawl`  
<br/>
_Description:_  
The Common Crawl is a non-profit organization that uses web crawlers to index the world wide web. Besides providing useful search results, data obtained from web crawling has been used to "improve language translation software, predict trends, track disease propogation and more."    
<br/>
_A Web crawler starts with a list of URLs to visit, called the seeds. As the crawler visits these URLs, it identifies all the hyperlinks in the page and adds them to the list of URLs to visit, called the crawl frontier. URLs from the frontier are recursively visited according to a set of policies. If the crawler is performing archiving of websites it copies and saves the information as it goes. The archives are usually stored in such a way they can be viewed, read and navigated as they were on the live web, but are preserved as ‘snapshots'_ - Wikipedia
<br/>  
_Directions:_    
There are many projects utilizing Common Crawl data.  Particularly useful to you is the [cc-pyspark](https://github.com/commoncrawl/cc-pyspark) Github project that examines the data using Python, Spark (via pyspark), and Amazon EMR.  Fork and clone this repo, **ignore** the set-up directions (you already have spark and all the necessary libraries installed, except for `warcio` which you can install with `$ pip install warcio`), then get sample data files running the bash script `get-data.sh`.  You can then follow the directions to run locally and then in the cloud.  
<br/>
_Possible questions to ask:_   
You can ask almost any questions of this data.  The [cc-pyspark](https://github.com/commoncrawl/cc-pyspark) repo includes code to count servers (`server_count.py`) and words (`word_count.py`).  Other questions that you could ask include:
  * How many pages were counted in a given month?
  * What was the proportional breakdown of media types on the web in a given month? (e.g. html, jpg, pdf, msword, etc.)
  * Of fetch requests, what fraction were successful/redirected/denied/failed?  

_References:_   
[Common Crawl data AWS link](https://registry.opendata.aws/commoncrawl/)  
[About the Commmon Crawl](http://commoncrawl.org/big-picture/frequently-asked-questions/)  
[Web crawler - Wikipedia](https://en.wikipedia.org/wiki/Web_crawler)  
[Medium - Web Crawlers - Everything you need to know](https://medium.com/@cabot_solutions/web-crawlers-everything-you-need-to-know-6dce26ee8ad8)  
[Example projects using Common Crawl Data](http://commoncrawl.org/the-data/examples/)  

### Option 2: NYC Taxi and Limo Trip Record Database  
_Database size:_ 45 GB  
_S3 Amazon resource name:_ `arn:aws:s3:::nyc-tlc`  
_Description:_  
The yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP).  
<br/>
_Possible questions to ask:_  
* How long is an average taxi ride in a 'Yellow' Taxi?  In a 'Green' Taxi?  
* What's the average tip?  
* Can you predict the average tip?  

_References:_  
[NYC Taxi and Limo data on AWS](https://registry.opendata.aws/nyc-tlc-trip-records-pds/)  
[NYC Yellow Cab galvanize DSI capstone](https://github.com/mkls2319/NYC_Yellow_Cab)
## Presentations
At the end of the day your group will be expected to present for 5-10 minutes on your findings.  You can do this directly from your README. 

Cover the following in your presentation:

   1. How you accessed the data
   2. A description of what's in the data (EDA)
   3. How you decided on the question to answer
   4. Your workflow (how did your work evolve from local to cloud development?)
   5. Things learned along the way.

