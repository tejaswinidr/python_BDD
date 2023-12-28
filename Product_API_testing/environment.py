from behave import *
from utilities.payLoad import *
from utilities.resources_api import *
from utilities.configurations import *
import requests
url = get_config()['API']['end_url'] + api_resources.create_prod
def after_scenario(context, scenario):
    uri = f"{url}/{context.user_id}/products/{context.product_id}"
    response = requests.delete(uri, headers=get_headers(token=context.auth_token))
    assert response.status_code == 204, f"Expected 204 response but found {response.status_code}"
    print("Deleted product successfully")