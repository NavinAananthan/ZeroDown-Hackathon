# Zero-Down-Hackathon

## Question 2 : Market Hotness
<br>
The project is done with following technologies
<br><br>

```
Cloud Hosting Platform - Streamlit Cloud
Frontend - Streamlit (Python Framework)
Database - Postgres SQL
```

```
Market Hotness
|__
  |_DB.py(Connecting with database)
  |_Fetchdata.py(fetch data from database)
  |_algo.py.py(main algo code and the UI part)
 ```
 
* In DB.py created the given table and inserted the records into PostgreSQL using python with the help of psycopg2 package inserting the records was done by reading the SQL file and executing it.
* In Fetchdata.py the main agenda was to retrive the datas from the postgreSQL database and load the datas into a csv file for preprocessing it
* In algo.py preprocessing stage was performed here we used the CSV files to preprocess the datas where NULL values are present so we find avg and many preprocessing to fill the NULL values and removing NULL values rows for inappropriate data and after preprocessing to calculate the scores for each Market metrics, Grouped by market id and calculated the avg for each column in the market metrics file using wieghted values we can get the score for which Market id it is best.
* Market id was used to fetch the city from the market file and used streamlit library for the front end for entering market_id and getting the respective score and also to analyze the datas with a graph
* Developing another algorithm with taking the cost and median sales to list ration would give you a score for the particular market id

### Deploying
* The project was deployed in streamlit cloud
* Link to the web app : https://navinaananthan-zerodown-hackathon-algo-zguczv.streamlit.app/

##Screenshots
![image](https://user-images.githubusercontent.com/81963819/218269916-e2b801d6-341b-49ad-8139-1dd4489457fd.png)


