from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class GetOrderByClientOrderIdService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/getClientOrder"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, Order, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






