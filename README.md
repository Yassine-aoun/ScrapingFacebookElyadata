# ScrapingFacebookElyadata
Elyadata Facebook Scraper is a FastAPI-based web scraping tool that extracts data from Facebook Public Profiles and stores it in a MongoDB database.

## Features

- **Web Scraping:** Extracts detailed data from Facebook Public Profiles.
- **FastAPI:** A high-performance web framework for building APIs.
- **MongoDB:** Efficient storage of scraped information.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Yassine-aoun/ScrapingFacebookElyadata.git
    cd ScrapingFacebokElyadata
    ```

2. **Build Docker image:**

    ```bash
    docker build -t scrapingfacebookelyadata:1.1.1 .
    ```

## Usage

1. **Start the Docker-Compose:**

    ```bash
    docker-compose up
    ```

2. **Make a Request using Curl Command:**

    ```bash
    curl "http://localhost:8000/scrape-facebook/<ID>?access_token=<ACCESS_TOKEN>"
    ```

3. **Access MongoDB Database:**

    ```bash
    docker exec -it scrapingfacebookelyadata-mongo-1 mongosh
    use facebook_scraping_db
    db.facebook_data.find().pretty()
    ```

## Technologies Used

- **FastAPI**
- **MongoDB**
- **Docker**
- **Python**

## Dockerization

The application is containerized using Docker. The Dockerfile is included in the repository for building the application image, and the `docker-compose.yaml` file defines the services and their configurations.

To pull and build the Docker image, run:

```bash
docker pull scrapingfacebookelyadata:1.1.1
docker build -t scrapingfacebookelyadata:1.1.1 .
```
## Running the Docker-compose:
![Image Alt Text](https://scontent.ftun1-2.fna.fbcdn.net/v/t1.15752-9/417660606_340674955453953_908899917345406216_n.png?_nc_cat=110&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=a9r1blZT9M8AX8RwQyr&_nc_ht=scontent.ftun1-2.fna&oh=03_AdQeglK1mRl4Y125Nkyzfj-qkv6HpCzx-oO0xJ1C7Emd6g&oe=65CF1A29)

## Request using Curl Command:
![Project Logo](https://scontent.ftun1-2.fna.fbcdn.net/v/t1.15752-9/417507052_353899820918970_8274530498879428990_n.png?_nc_cat=107&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=x4nAEXQ9BmYAX9PIJ_W&_nc_ht=scontent.ftun1-2.fna&oh=03_AdTQ2Nkv-6kP89Uz_9uWgJBIyWe1XXc46l_f4Na70MUM-g&oe=65CF2B7A)


## Request using Curl Command:
![Project Logo](https://scontent.ftun1-2.fna.fbcdn.net/v/t1.15752-9/417507052_353899820918970_8274530498879428990_n.png?_nc_cat=107&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=x4nAEXQ9BmYAX9PIJ_W&_nc_ht=scontent.ftun1-2.fna&oh=03_AdTQ2Nkv-6kP89Uz_9uWgJBIyWe1XXc46l_f4Na70MUM-g&oe=65CF2B7A)

## Verification of Data in Containerized Database
![Alt text](https://scontent.ftun1-2.fna.fbcdn.net/v/t1.15752-9/417619094_4417978388426719_1681949353280494202_n.png?_nc_cat=109&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=gdw7MjHMiigAX_tB7mR&_nc_ht=scontent.ftun1-2.fna&oh=03_AdT1Vn02uvcEOLhpoWKZfs3ik5M2XV-DwpH42Qw5ujcVHw&oe=65CF0843)

