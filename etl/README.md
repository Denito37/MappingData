# ETL Python Script

### Purpose
a Python script to:
- Extract data from NYC Open data APIs & ultilizize Google Earth engine's images on NYC's surface temperature
- Transform that data to fit our needs
- Load that data into the database that our web application will use

### How to run : With Docker
- Make sure you have Docker desktop downloaded, if you don't go [here](https://www.docker.com/products/docker-desktop/)
- create an .env file with the API_TOKEN variable defined with the API key
- run this command in your terminal:
    ```console

        docker build --secret id=API_TOKEN,env=API_TOKEN -t [imageName]:latest  ./etl 

    ```
- Check your images in the Docker desktop & click run
