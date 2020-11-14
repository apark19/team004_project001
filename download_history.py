import pandas as pd
import datetime
import sys
import getopt
import traceback
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def convert_ts(timestamp):
    result = datetime.datetime.fromtimestamp(timestamp)
    return (result.strftime('%Y-%m-%d %H:%M:%S'))

def get_contents(filename):
    with open(filename) as f:
        return f.read()

def get_hist(data, sym):
  session = Session()

  try:
    response = session.get('https://min-api.cryptocompare.com/data/v2/histoday?fsym='+str(sym)+'&tsym=USD&limit=2000&api_key='+str(data))

    return response.json()
  except (ConnectionError, Timeout, TooManyRedirects):
    traceback.print_exc()

def hist_to_file(out_file, k_file, symbol):
    out_frame=pd.DataFrame(columns=['Date','Open','Close','High','Low'])
    payload=get_hist(get_contents(k_file), symbol)
    
    if payload['Response']=="Success":
        data=payload['Data']
       
        start_ts=data['TimeFrom']
        arr=data['Data']

        for day in arr:
            dt=convert_ts(day['time'])[:10]
            out_frame=out_frame.append({'Date':dt,'Open':day['open'],'Close':day['close'],'High':day['high'],'Low':day['low']},ignore_index=True)

        out_frame.to_csv(out_file) 

    print(str(datetime.datetime.utcnow())+"|hist_to_file|processing completed")


def main(argv):
    config=""
    output=""
    symbol=""
    opts,args=getopt.getopt(argv,"c:i:s:")
  
    for opt,arg in opts:
        if opt=="-c":
            config=str(arg)
        elif opt=="-i":
            output=str(arg)
        elif opt=="-s":
            symbol=str(arg)
        else:
           sys.exit(1)

    try:
        hist_to_file(output,config,symbol)
    except:
        traceback.print_exc()
        pass

if __name__ == "__main__":
  main(sys.argv[1:])
exit()
