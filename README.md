
# User Management and Product API - BMDPE Technologies Private Limited

## Setup Instructions

### Environment Setup:

Create a .env file with the required configuration.

### using:  ***python -m venv env*** 

- ***cd env/scripts/activate***


## Install Dependencies:
### Activate your virtual environment and install the dependencies using:

***pip install -r requirements.txt***
## Database Initialization:

### Initialize Alembic using:

***alembic init alembic***  
Configure the Alembic env.py file to connect to your PostgreSQL database.
Apply migrations using:
***alembic upgrade head***
## Run the Application:
Start the server with:

***uvicorn main:app --reload***

## API Features
## 1. User Creation
Fields to Create User:
Required fields include ***name, email, password, etc.***

##Response on Success:
If the user is successfully created, the details are displayed in the response body:


![image](https://github.com/user-attachments/assets/b6c3c992-abd7-497f-990b-7c36fdc2980e)

## 2. Authentication
# Provide the email and password in the Authorization section.

Upon successful authentication, the following response is returned:
![image](https://github.com/user-attachments/assets/03709fec-e3cb-4028-b462-19c257ba822e)

give email and password in athorized section 
![image](https://github.com/user-attachments/assets/f25504c0-0246-473a-81be-2279638a91de)
if the authentication completed successful it will show this
![image](https://github.com/user-attachments/assets/fa733e04-68ed-4f68-84be-6022ccab3be9)
check for products
![image](https://github.com/user-attachments/assets/d153f83b-5eb7-4068-81d4-7deb7b6dd21b)
output of products
![image](https://github.com/user-attachments/assets/2adac5ef-0e1e-480b-81ff-12036722b327)
get products without id
![image](https://github.com/user-attachments/assets/23580dd3-7038-4e8e-bb01-ceadf1a7481e)
GET /products - filter by catogiry
![image](https://github.com/user-attachments/assets/276eed0b-76c3-4397-b8a4-75c1cf22c3a9)
sort by asending order
![image](https://github.com/user-attachments/assets/bf3ee5b9-d3b0-450b-983d-7e9083f0c5c4)
sort by desending order
![image](https://github.com/user-attachments/assets/87ad9b12-9e29-43fb-baa1-aff7a0e87f0f)
updated the code with low stock with boolien values
![image](https://github.com/user-attachments/assets/286cd77a-6528-4fa4-b9c6-365800a780ec)
when we give negative numbers 
![image](https://github.com/user-attachments/assets/50dec96c-9f41-420a-ad0d-f4f3615e18f7)
the output will be 
![image](https://github.com/user-attachments/assets/6b7bde1a-1a08-473f-8605-0a017502124e)












