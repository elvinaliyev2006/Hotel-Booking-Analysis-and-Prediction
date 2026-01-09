import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_HOST = "localhost"  
DB_PORT = "3306"

try:
    connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    print("⏳ CSV is reading...")
    df = pd.read_csv("clean_hotel_data.csv") 
    print(f"🚀 {len(df)} rows into the Docker database...")
    df.to_sql("hotels", con=engine, if_exists="replace", index=False)

    print("✅")

except Exception as e:
    print(f"❌ Error: {e}")