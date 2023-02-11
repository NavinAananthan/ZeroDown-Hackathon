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
* In algo.py file we use the CSV file to preprocess the the given data and use the median sale price to calculate the score of each market_id and based on the score we find the city where it belongs to and also used median_sale_to_list_ratio to find the best score

#### Deploying
* I used streamlit cloud to deploy my app but it caused an error so  i'm attaching below images to show the UI
![image](https://user-images.githubusercontent.com/81963819/218258999-7052c099-76c6-45fd-b1e6-bb2e937bf6b0.png)
