# Tweet Stock Correlation

Displays the relationship between the internet traffic (via Twitter) of the components of the Nasdaq-100 and the change in their stock price over a specified time interval. Uses Twitter's restfulAPI in order to find historical data on the amount of tweets containing cashtag of tickers. Also uses YFinanceAPI to pull historical data from different time periods. Python's Pandas library was prominently featured.

## Dependencies

```bash
Python Distribution: Python or Anaconda (recommended)
YFinance
Tweepy
Jupyter Lab or Jupyter Notebook (both included with Anaconda)
```

## Installing Dependencies

### YFinance
If using pip, enter in terminal:
```bash 
pip install yfinance --upgrade --no-cache-dir
```

If using conda, enter in conda prompt:
```bash
conda install -c ranaroussi yfinance
```

### Tweepy
If using pip, enter in terminal:
```bash 
pip install tweepy
```

If using conda, enter in conda prompt:
```bash
conda install -c conda-forge tweepy
```

## Running Notebook or Python File

With dependencies installed, clone the repo with one of the following in your terminal

HTTPS:
```bash
git clone https://github.com/sherloque-W/Tweet-Stock-Correlation.git
```

SSH:
```bash
git@github.com:sherloque-W/Tweet-Stock-Correlation.git
```

### Jupyter
If you want to run the program using the Jupyter Notebook (recommended for inline plot) or JupyterLab, first launch either one of the following through the conda prompt:
```bash
jupyter notebook
```
```bash 
jupyter lab
```
Then, navigate to the cloned repo in your  local filesystem in either of the two environments and open the .ipynb file. To run the notebook, select "Run all cells" and follow the input prompts.

### Terminal
If you want to run the .py file, open a terminal in the src folder of the repo and type the following:
```bash 
python CorrelationScript_JL.py
```
If using the Anaconda distrubution, then run the above command in the conda prompt rather than the standard terminal. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
