# Prerequisites
- Python 3.10.8 (NOT 3.11 or higher)
- Check if `pip` is installed
- Basic `HTML` and `XPATH`
- Basic `Python` (`for`, `list`, etc.)
- Need to know how to handle `pandas` Dataframe (`df.dropna()`, `df.to_csv()`, `axis`, `how`, ...)

# Need to install
- pandas: `pip install pandas` (not for Colab)
- selenium: `pip install selenium`
- lxml: `pip install lxml`
- webdriver_manager (if no chromedriver.exe): `pip install webdriver_manager`
- matplotlib (if you want visualization): `pip install matplotlib` (not for Colab)

# Notes
- This project **WORKS** on Colab without opening up a new window but the `sise.csv` file is successfully created and no issues found in crawling data correctly (so far).
- Highly recommend using **VScode** or any other Python IDEs instead of Colab due to the note above.
- Because Colab does not support opening a new window (browser), the Colab version is slightly different in accessing the webpage.