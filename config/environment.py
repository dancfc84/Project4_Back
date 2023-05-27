import os

db_URI = os.getenv('DATABASE_URL', 'postgres://mfkecnxplbplwi:528b8b2f54538f5f6c41d7dcb0e0bb7842a7fd4fe714046fae201ab8caacebce@ec2-54-73-22-169.eu-west-1.compute.amazonaws.com:5432/d47jd86gtmt2ku')
secret = os.getenv('SECRET', 'a suitable secret')