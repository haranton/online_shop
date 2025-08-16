import time
import psycopg2
import requests

def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="mydb",
                user="mydb",
                password="mydb",
                host="shop-db",
                port="5432",
            )
            conn.close()
            print("Postgres is ready")
            break
        except psycopg2.OperationalError:
            print("Waiting for Postgres...")
            time.sleep(2)

def wait_for_minio():
    url = "http://minio:9000/minio/health/live"
    while True:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print("MinIO is ready")
                break
        except requests.exceptions.RequestException:
            pass
        print("Waiting for MinIO...")
        time.sleep(2)

if __name__ == "__main__":
    wait_for_postgres()
    wait_for_minio()
