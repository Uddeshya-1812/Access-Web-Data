import concurrent.futures
import time
from Crawl_Product import main_func


		      
if __name__ =='__main__':
	
	begin = time.time()
	#Here urls are arranged in a definite pattern which is 'https://www.amazon.in/'PRODUCT_NAME'/product-reviews/'PRODUCT_CODE'/ref=cm_cr_arp_d_viewopt_rvwer?sortBy=recent&pageNumber=' which gives importance to product code and product name
	with open('urls.txt','r') as f:
		urls = f.readlines()
	f.close()
	length = len(urls)
	urls = [i[:-1] for i in urls]
	Task = [None]*length
	user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
		     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
		     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
		     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
		      ]
	args = [ [urls[0],'2020-07-01',user_agent[0],'Redmi-8A-Dual-Blue-Storage.csv'],#arguments for main funcs which performs product crawling
		[urls[1],'2019-07-01',user_agent[0],'Test-Exclusive-748.csv'],
		[urls[2],'2020-07-01',user_agent[1],'Redmi-Note-Neptune-Blue-Storage.csv'],
		[urls[3],'2020-07-01',user_agent[1],'Redmi-8A-Dual-Midnight-Storage.csv'],
		[urls[4],'2020-07-01',user_agent[2],'Test-Exclusive-669.csv'],
		[urls[5],'2020-07-01',user_agent[2],'Dazzling-Storage-Additional-Exchange-Offers.csv'],
		[urls[6],'2020-07-01',user_agent[3],'Apple-iPhone-11-64GB-Black.csv'],
		[urls[7],'2019-07-01',user_agent[3],'Redmi-Note-Space-Black-Storage.csv'],
		[urls[8],'2020-07-01',user_agent[4],'Redmi-8A-Dual-Blue-Storage.csv'],
		[urls[9],'2020-07-01',user_agent[4],'Apple-iPhone-Pro-Max-64GB.csv']
		]
	#concurrent.futures is a library for python3 that wraps up multithreading as well as multiprocessing libraries of python	
	#here max workers correspond to number of cores of your cpu,when no arument passed it automatically takes the max  number of cores for multiprocessing,here 4 
	with concurrent.futures.ProcessPoolExecutor(max_workers = 4) as task:
		for i in range(length):
			Task[i] = task.submit(main_func,args[i])
	ends = time.time()	
	print('Time taken in Minutes ~~',round((ends-begin)/60,2))	
	
