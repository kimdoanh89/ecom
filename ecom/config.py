import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "doanhluong")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "doanhluong123")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecom")
TEST_DATABASE_NAME = os.getenv("TEST_DATABASE_NAME", "ecom_test")
