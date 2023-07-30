import requests
import logging, os
from urllib.parse import urlparse

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('az_request_check initiated')
    logging.info(f'req.url: {req.url}')

    # GOVMAP_URL = "https://open.govmap.gov.il/geoserver/opendata/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=opendata:PARCEL_ALL&cql_filter=GUSH_NUM={}+AND+PARCEL={}&outputFormat=application/json&SRSNAME=EPSG:4326"

    # Get the raw query string from the request URL
    raw_query_string = urlparse(req.url).query
    test_url = f"{raw_query_string}"


    if test_url == "":
        test_url = "https://open.govmap.gov.il/geoserver/opendata/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=opendata:PARCEL_ALL&cql_filter=GUSH_NUM=6635+AND+PARCEL=286&outputFormat=application/json&SRSNAME=EPSG:4326"
        

    # test_url = GOVMAP_URL % (gush, helka)
    logging.info(f'test_url: {test_url}')
    output = ""

    try:
        response = requests.get(test_url)
        logging.info(f'response: {response}')

        # get response headers
        logging.info("Response Headers:")
        for key, value in response.headers.items():
            output+=(f"{key}: {value}\n")

        output += response.text
    except Exception as e:
        logging.error(f'Exception: {e}')

    return func.HttpResponse(
        output, status_code=200
    )
