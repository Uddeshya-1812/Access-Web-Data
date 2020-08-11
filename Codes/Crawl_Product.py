import pandas as pd
import time
from Scrapper_funcs import scrape


start = time.time()
def main_func(array):
	'''
	main_func(array) has argumnents in form of list which has product_url,last_date(last date to scrape),user_agent and name of output file at 0,1,2,3 index respectively 
	'''
	try:
		print('Scrapping Started')
		url = array[0]
		last_date = array[1]	
		user_agent = array[2]
		output_file = array[3]
		
		
		start = time.time()
		pge_num = 1

		data = scrape(url + '1',user_agent)
		
		max_review_date = pd.to_datetime([i.split('on')[1] for i in data['ReviewDate']])[0]#First comment on each page with converted for comparison

		last_date =  pd.to_datetime(last_date)
		frames = []
		
		tot_num_of_pages = 0
		while max_review_date >= last_date:
			data = scrape(url+ str(pge_num),user_agent)
			review_dates = pd.to_datetime([i.split('on')[1] for i in data['ReviewDate']])#Converted dates through pandas.to_datetime for comparison
			max_review_date = review_dates[0]
			min_review_date = review_dates[-1] #last review on each page
			output = pd.DataFrame({'Website':'Amazon',
			'Review_Title':data['ReviewTitle'],
			'Review_Text':data['ReviewText'],            
			})
			#output = pd.concat([dictionary_df,output],axis=1)#concatenated user-profiles and their review into frames
			frames.append(output)
			if min_review_date <= last_date:
           			break
			pge_num+=1
			
		if len(frames) > 1: 
        			output = pd.concat(frames,axis=0)  #Concatenated all frames that were stored as dataframe in variable name 'fames' of type List and make a new dataframe
        			 
		output.to_csv(output_file,index = False) #Converted dataframe to csv file
		end = time.time()        
		print("Crawled ",output_file[:-4],' in  ',round((end-start)/60,3),"Min")
	
	except Exception as e:
		print("Exception Occured ~~ ",e,'for product',output_file[:-4])
		
