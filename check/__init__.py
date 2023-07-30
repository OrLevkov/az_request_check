import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('az_request_check initiated')

    GOVMAP_URL = "https://open.govmap.gov.il/geoserver/opendata/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=opendata:PARCEL_ALL&cql_filter=GUSH_NUM={}+AND+PARCEL={}&outputFormat=application/json&SRSNAME=EPSG:4326"

    gush    = req.params.get('gush')
    helka   = req.params.get('helka')


    test_url = GOVMAP_URL % (gush, helka)
    logging.info(f'test_url: {test_url}')

    try:
        response = requests.get(test_url)
        logging.info(f'response: {response}')
        output = response.json()
    except Exception as e:
        logging.error(f'Exception: {e}')

    return func.HttpResponse(
        json.dumps(output), status_code=200
    )
