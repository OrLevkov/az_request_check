import requests
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    test_url = "http://google.com"
    # logging.info('az_request_check initiated')

    # GOVMAP_URL = "https://open.govmap.gov.il/geoserver/opendata/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=opendata:PARCEL_ALL&cql_filter=GUSH_NUM={}+AND+PARCEL={}&outputFormat=application/json&SRSNAME=EPSG:4326"

    if len(req.params) > 0:
        query_params = req.params
        # Convert the dictionary to a string representation
        test_url = "&".join([f"{key}={value}" for key, value in query_params.items()])
    else:
        test_url = "http://google.com"  

    

    # test_url = GOVMAP_URL % (gush, helka)
    logging.info(f'test_url: {test_url}')

    try:
        response = requests.get(test_url)
        logging.info(f'response: {response}')
        output = response.text
    except Exception as e:
        logging.error(f'Exception: {e}')

    return func.HttpResponse(
        output, status_code=200
    )
