
#!/usr/bin/python3


import requests     # used to make HTTP requests (GET, POST, PUT, DELETE, etc.)

# this is USDA Cattle Market API link For National Cow and Bull
REPORT = "https://mpr.datamart.ams.usda.gov/services/v1.1/reports/2488"

def main():
   
       # perform an HTTP GET request
    response = requests.get(REPORT)   # response is the USDA Cattle market API response object
       # Convert API to market_data
    market_data = response.json()     # .json() method transforms data into python dictionary format   
                               
    #  ** IF ISSUE WITH NO MARKET DATA RUN STATUS CODE !!**                               
    #print(response.status_code)   # TESTS the HTTP Connection status code returned should be a 200 =successful 
      
    #print(type(market_data))      # TESTS type of output for market_data
    #print(market_data)              # Prints the data in market_data
    
 # Slice    
    sliceme= requests.get(REPORT).json()   
    for i in sliceme['results']:
       
        print(f"{i['report_date_end']} National Confirmed {i['current_volume']}") 
        print(f"{i['report_date_end']} Northwest Confirmed {i['current_volume_1']}") 
        print(f"{i['report_date_end']} Southwest Confirmed {i['current_volume_2']}") 
        print(f"{i['report_date_end']} Eastern Area Confirmed {i['current_volume_3']}:\n")
     


        

if __name__ == "__main__":
   main()

