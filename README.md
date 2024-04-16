# City Percentage of Population with Higher Education Degrees in Kazakhstan

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```shell
    $ git clone https://github.com/open-data-kazakhstan/city-percentage-of-population-with-higher-education-degrees.git
    ```

2. Create and activate a virtual environment:
    ```bash
    pip install venv
    python -m venv /path/to/localrepo
    cd /path/to/localrepo
    Scripts/activate  # For Windows users
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the scripts:
    ```bash
    python scripts/transform.py
    python scripts/package.py
    ```

## Data

Education data is sourced from ([stat.gov.kz](https://stat.gov.kz/upload/iblock/3a8/7c99zhdr5fpt1htbcd1migx7aqgazend/%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.pdf)).

- 'document.pdf': The original document containing the data about the education levels in Kazakhstan.
- `source.xlsx`: Raw data of population age 10 and older with higher education degrees by region for the year 2021. The 2022 data was not available from credible sources, hence the dataset focuses on 2021.
- `higher_education.csv`: English version containing data of population percentages with higher education degrees in urban areas only in 2021.

All percentage values are given relative to the total population aged 10 and older.

**Note:** The values for the Abai, Jetisu, and Ulytau regions are based on the broader location they are part of, due to specific data unavailability for these regions. For example, Jetisu's figures are included with those of the Almaty region.

## Scripts

- `package.py`: Used to create or update the `datapackage.json` file containing metadata about the dataset.
- `transform.py`: Used to convert the `source.csv` file for easier processing.

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License](https://www.opendatacommons.org/licenses/pddl/1-0/ "‌").

---