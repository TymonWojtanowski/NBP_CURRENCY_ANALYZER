# NBP_CURRENCY_ANALYZER
# NBP Currency Analyzer

## Description

This project implements a simple data pipeline to fetch daily currency exchange rates (Table A) from the public API of the National Bank of Poland (NBP). The extracted data is then loaded into a PostgreSQL database for storage and subsequent analysis using SQL. It serves as a foundational project demonstrating core Data Engineering principles (Extract-Load-Transform).

## Tech Stack

* **Python 3:** For data extraction and loading logic (`requests`, `psycopg2`).
* **PostgreSQL:** Relational database for storing the currency data (running inside a Docker container).
* **Docker:** For containerizing the PostgreSQL database service, ensuring a consistent environment.
* **SQL:** For database schema definition and data analysis queries.
* **Git & GitHub:** For version control and project hosting.
* **(Optional) BI Tool:** Metabase or Apache Superset (running in Docker) for data visualization.
* **(IDE/DB Client):** PyCharm/DataGrip recommended.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure you have the following installed on your system:
* Python 3 (comes with Ubuntu 25.10 / Fedora)
* Git
* Docker
* *(Recommended)* Docker Compose (usually installed as a plugin with Docker)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[TymonWojtanowski]/NBP_CURRENCY_ANALYZER.git
    cd NBP_CURRENCY_ANALYZER
    ```

2.  **Set up the PostgreSQL Database:**
    You need a running PostgreSQL instance. The recommended way is using Docker Compose for easy management.

    * **(Recommended) Using Docker Compose:**
        Create a `docker-compose.yml` file in the project root with the following content:
        ```yaml
        services:
          db:
            image: postgres
            container_name: nbp-postgres
            restart: unless-stopped
            environment:
              POSTGRES_PASSWORD: yoursecretpassword # Choose a strong password
            ports:
              - "5432:5432"
            volumes:
              - postgres_data:/var/lib/postgresql/data

        volumes:
          postgres_data:
        ```
        Then, run the database container:
        ```bash
        docker-compose up -d
        ```
        *(Make sure to add `postgres_data/` to your `.gitignore` if Docker creates it locally, although named volumes are usually managed elsewhere.)*

    * *(Alternative) Using `docker run` (as described in README initially):*
        If you prefer the single command:
        ```bash
        docker run --name nbp-postgres -e POSTGRES_PASSWORD=yoursecretpassword -p 5432:5432 -v nbp_postgres_data:/var/lib/postgresql/data -d postgres
        ```
        Ensure the container is running: `docker start nbp-postgres`

3.  **Set up the Python Environment:**
    It's highly recommended to use a virtual environment.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Create Database Schema:**
    Connect to your PostgreSQL database using DataGrip (or another SQL client) with the credentials you set (Host: `localhost`, Port: `5432`, User: `postgres`, Password: `yoursecretpassword`, Database: `postgres`). Execute the SQL commands found in `schema.sql` to create the necessary table(s).

## Usage

1.  **Ensure the PostgreSQL container is running.**
    ```bash
    docker ps # Check if nbp-postgres is listed and Up
    # If not: docker start nbp-postgres
    ```

2.  **Run the data extraction and loading script:**
    Make sure your virtual environment is activated (`source .venv/bin/activate`).
    ```bash
    python extract.py
    ```
    This script will fetch the latest data from the NBP API and load it into your `rates` table.

3.  **Analyze the Data:**
    Use DataGrip or your preferred SQL client to connect to the database. You can find example analysis queries in the `analysis.sql` file.

4.  **(Optional) Visualize the Data:**
    If you choose to use a BI tool like Metabase or Superset:
    * Run the BI tool (preferably in Docker).
    * Connect it to your PostgreSQL database.
    * Create dashboards and visualizations based on the `rates` table.

## Project Structure
