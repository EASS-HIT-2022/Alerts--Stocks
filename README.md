# Stock Alert System

-   [Description](#description)
-   [Quick start](#Quick-start)
-   [Walk through](#walk-through)
    -   [Services](#Services)
    -   [File structure](#file-structure)
    -   [Final Project](#Final)


### Description

The system will track stocks at the customer's request and send an appropriate message when the stock enters the trigger.

### Quick-start

### To run the project, we will enter the following commands:

1. --To build the project -- run following command :

    **docker compose build**

2. --To run the project -- run following command :
 
    **docker compose up**

3. And finally go to the following link: http://localhost:8501/ in browser 

###walk-through
#### Services
The project contains three services:
The first service is the Backend that works with FastAPI, the second service is the UI that works with Streamlit and the third service is the DB.
And the docker-compose runs them all.

### File-structure

```sh
├── README.md
├── docker-compose.yml
├── backend
│   ├── __init__.py
│   ├── api_yahoo.py
│   ├── data.json
│   ├── db.py
│   ├── df_yahoo.csv
│   ├── Dockerfile
│   ├── main.py
│   ├── patterns.py
│   └── requirements.txt
│   ├── test_system.py
└── database
│   ├── data.json
│   ├── db.py
│   ├── Dockerfile
│   └── requirements.txt
└── frontend
    ├── app.py
    ├── Dockerfile
    ├── pipfile
    └── requirements.txt
```





### Screenshots

## Final Project

![](/images/gif_alert_stock.gif)
