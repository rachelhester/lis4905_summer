import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

start = dt.datetime(2010,1,1)
end = dt.datetime.now()

f = web.DataReader('AAPL', 'yahoo', start, end)
def get_requirements():
	
	"""Get the program requirements"""

	print('''
		\n1. Work with your team.
		\n2. Backward-engineer screenshot below.
		\n3. If errors, check missing installations (e.g. pandas_datareader, matplotlib pyplot and style)
		\n4. Research how to do any necessary installations, *only* if needed:
		\n5. Also, include at *least* three graphs (dates from Jan. 1st 2010 until now).
		\n6. Create a different * style * of graph for each of the companies shown below.
		\n7. Optional: Create at least three functions that are called by the program:
		\n\ta. main(): calls at least two other functions
		\n\tb. get_requirements(): displays the program requirements.
		\n\tc. data_analysis_1(): displays the following data.''')
def data_analysis_1():
	
	"""Get data analysis from a ticker"""

	print("\n\nPrint number of records:",len(f),sep='\n')
	print("\n\nPrint columns:",f.columns,sep='\n')
	print("\n\nPrint data frame:\n",f,sep='\n')

	stocker = [
	{
		'ticker': 'AAPL',
		'name': 'Apple'
	}
	]

	stocklist = [
	{
		'ticker': 'AAPL',
		'name': 'Apple'
	},
	{
		'ticker': 'TSLA',
		'name': 'Tesla'
	},
	{
		'ticker': 'AMC',
		'name':'AMC Entertainment'
	}
	]

	for stock in stocker:
			df = web.DataReader([stock['ticker']], 'yahoo', start, end)
			print("\n\nPrint first 8 rows:")
			print(f.head(8))
			print("\n\nPrint last 6 rows:")
			print(f.tail(6))


	styles = ['Solarize_Light2', 'grayscale', 'seaborn']	
	for i, stock in enumerate(stocklist):
		style.use(styles[i])
		df = web.DataReader(stock['ticker'], 'yahoo', start, end)
		df[['High', 'Adj Close']].plot(label=stock['name'])
		plt.title(stock['name'] + " - " + styles[i])
		plt.legend()
		plt.xlabel('Date')
		plt.show()



def main():
	get_requirements()
	data_analysis_1()

main()


