from extract.extract  import read_drinking_fountains_data
from transform.transform import transform_drinking_fountains_data

def main():
    print("Starting ETL process...")
    data = read_drinking_fountains_data()
    transformedData = transform_drinking_fountains_data(data)
    print(transformedData.info())


if __name__ == "__main__":
    main()