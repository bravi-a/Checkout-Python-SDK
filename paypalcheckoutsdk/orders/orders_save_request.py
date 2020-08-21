import paypalhttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+


class OrdersSaveRequest:
    """
    Save an order.
    """
    def __init__(self, order_id):
        self.verb = "POST"
        self.path = "/v2/checkout/orders/{order_id}/save?".replace("{order_id}", quote(str(order_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def prefer(self, prefer):
        self.headers["Prefer"] = str(prefer)

    def request_body(self, patch_request):
        self.body = patch_request
        return self
