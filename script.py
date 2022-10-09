from pathlib import Path
from geopy.geocoders import Nominatim
import requests
import pandas as pd
import json

def get_forecast( city='Pittsburgh' ):
    '''
    Returns the nightly's forecast for a given city.

    Inputs:
    city (string): A valid string

    Output:
    period (dictionary/JSON): a dictionary containing at least, the forecast keys startTime, endTime and detailedForecast.

    Throws:
    CityNotFoundError if geopy returns empty list or if the latitude longitude fields are empty.

    ForecastUnavailable if the period is empty or the API throws any status code that is not 200

    Hint:
    * Return the period that is labeled as "Tonight"
    '''
    temp = []

    
    output_dic=json.loads(city)
    if output_dic.get('latitude') or output_dic.get('longitude')is None:
        warnings.warn("CityNotFoundError")    
    if output_dic.get('latitude')
    
    
    period = 'Tonight'
    return period
    raise NotImplementedError()

def main():
    period = get_forecast()

    file = 'weather.pkl'

    if Path(file).exists():
        df = pd.read_pickle( file )
    else:
        df = pd.DataFrame(columns=['Start Date', 'End Date', 'Forecast'])

    df = df.append({'Start Date': period['startTime'], 'End Date': period['endTime'], 'Forecast': period['detailedForecast']}, ignore_index=True)
    df = df.drop_duplicates()
    df.to_pickle(file)

    #sort repositories
    file = open("README.md", "w")
    file.write('![Status](https://github.com/alicewuhhh/python-get-forecast/actions/workflows/build.yml/badge.svg)\n')
    file.write('![Status](https://github.com/alicewuhhh/python-get-forecast/actions/workflows/pretty.yml/badge.svg)\n')
    file.write('# Pittsburgh Nightly Forecast\n\n')
    
    file.write(df.to_markdown(tablefmt='github'))
    file.write('\n\n---\nCopyright © 2022 Pittsburgh Supercomputing Center. All Rights Reserved.')
    file.close()

if __name__ == "__main__":
    main()
