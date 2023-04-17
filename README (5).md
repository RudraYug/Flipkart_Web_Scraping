
# Python Web Scrapping

This is a Python script for scraping product data from an e-commerce website namely Flipkart. The script uses the Selenium WebDriver to automate the process of navigating the website and extracting product data.

Flipkart is a popular e-commerce website in India that offers a wide range of products, including electronics, fashion, home appliances, books, and more. It is an excellent platform for buyers to compare prices and buy products at a lower price.

Web scraping is the process of extracting data from websites. It involves the use of software to collect data automatically from websites. In the case of Flipkart, web scraping can be used to extract information about the products available on the website, their prices, ratings, customer reviews, and more.

One of the most popular Python libraries for web scraping is Selenium. It can be used to extract the relevant information. Another popular library for web scraping is Scrapy, which provides a more robust framework for web scraping and data extraction.

By using web scraping techniques, we can collect data from Flipkart and use it for various purposes, such as price comparison, market research, and data analysis.
## Table Of Contents

- Prerequisites
- Installation
- Usage
- Contribution
- Conclusion
- License
- Related

## Prerequisites

The following libraries need to be installed to run the script:

- [pandas](https://pandas.pydata.org/)
- [selenium](https://www.selenium.dev/)
- [webdriver_manager](https://pypi.org/project/webdriver-manager/)
- [logging](https://docs.python.org/3/library/logging.html)
- [pdb](https://docs.python.org/3/library/pdb.html)
## Installation

To run the Movie Recommender System, follow these steps:

- Clone the repository to your local machine.
- Install the required libraries using **`pip install -r requirements.txt`**.
- Run the **`flipkart_L1.py`** file using the command **`python flipkart_L1.py`**.
    
## Usage

To use this script, you need to provide the URL of the website you want to scrape, as well as the category and sub-category names for the products you are interested in.

You can run the script by executing the **`flipkart_L1.py`** file in the terminal using the command python **`flipkart_L1.py`**.

The script will prompt you to enter the website URL and the category and sub-category names. Once you have entered this information, the script will start scraping product data from the website.

Alternate method could be to, simply import the necessary modules and functions and call the **`download_page_data`** function with the required arguments.

```python
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import datetime
import sys
import os
import logging #logger text file created to maintain real time data of website
import pdb   #used for line by line debugging

def set_log_file(log_file_name):
    # ...
    return logger

def get_driver():
    # ...
    return driver

def download_page_data(driver, count, category, sub_c1, sub_c2, sub_c3, sub_c4,  website_output_file_name):
    # ...
    return
```

**`set_log_file`** function sets up a logger that saves real-time data of the website into a text file. The **`get_driver`** function is used to create a Selenium driver instance. Finally, the **`download_page_data`** function takes the driver instance and other required arguments to scrape the website and store the data in a Pandas DataFrame.


### Output

The script outputs the data in a CSV file. The name of the output file is based on the category and sub-category names entered by the user.

The output file contains the following fields for each product:

- **`Category`**: The main category of the product
- **`Sub-C1`**: The first level sub-category of the product
- **`Sub-C2`**: The second level sub-category of the product
- **`Sub-C3`**: The third level sub-category of the product
- **`Sub-C4`**: The fourth level sub-category of the product
- **`Brand`**: The brand of the product
- **`Product Name`**: The name of the product
- **`MRP`**: The maximum retail price of the product
- **`Discounted Price`**: The discounted price of the product
- **`Offer`**: Any offer that applies to the product
- **`Rating`**: The rating of the product
- **`Rating Count`**: The number of ratings received by the product
- **`Product Raw`**: The raw text of the product listing
- **`Product Url`**: The URL of the product page on the website


### Logging

The script also creates a log file to maintain real-time data of the website. The log file is created using the **`logging`** library and is named based on the category and sub-category names entered by the user.


### Debugging

The **`pdb library`** is used for line-by-line debugging of the script. It can be used to track down errors and exceptions that occur during execution.


### WebDrivers

The script uses the Chrome WebDriver for scraping data. The **`webdriver_manager`** library is used to automatically download and manage the WebDriver.

## Contribution

Contributions to the project are welcome. If you would like to contribute, please follow these steps:

- Fork the repository to your own GitHub account.
- Clone the repository to your local machine.
- Create a new branch with a descriptive name using the command **`git checkout -b your-branch-name`**.
- Make your changes and commit them using the command **`git commit -m "your commit message"`**.
- Push your changes to your forked repository using the command **`git push origin your-branch-name`**.
- Create a pull request on the original repository and wait for it to be reviewed.
## Conclusion

In conclusion, web scraping is a powerful tool for gathering data from the internet. By scraping data from Flipkart, we were able to extract useful information such as product names, prices, and ratings. This data can be used for a variety of purposes such as price comparison, market analysis, and research.

Overall, web scraping can provide valuable insights and information that can be used to make informed decisions in various industries.
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.


## Related

Here are some related projects

- [Spotify_Analysis](https://github.com/RudraYug/Spotify_Analysis.git)

- [Tic_Tac_Toe](https://github.com/RudraYug/Tic_Tac_Toe.git)

- [Football_Prediction_Analysis](https://github.com/RudraYug/Football-Prediction-Analysis.git)