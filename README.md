# Zero-Down-Hackathon

## Question 2 : Market hotness
<br>
The project is done with following technologies
<br><br>

```
Cloud Platform - Streamlit Cloud
Frontend - Streamlit
Database - Postgres SQL
```
```
Market Hotness
|__
  |_DB.py(Connecting with database)
  |_Fetchdata.py(fetch data from database)
  |_algo.py.py(main algo code and the UI part)
 ```
* In DB.py we create the table and insert records into it
* In Fetchdata.py we Use query to select the datas from the database and store it in a CSV and use it to preprocess it
* In algo.py file we use the CSV file to preprocess the the given data and use the median sale price to calculate the score of each market_id and based on the score we find the city where it belongs to and also used median_sale_to_list_ratio to find the best score.
* Developing another algorithm with taking the cost and and wit respect ratio and the days we could get a score for the particular market id

#### Deploying
* I used streamlit cloud to deploy my app but it caused an error so  i'm attaching below images to show the UI
![image](https://user-images.githubusercontent.com/81963819/218259134-6b708179-b46b-4547-a559-bd11addb13e3.png)

