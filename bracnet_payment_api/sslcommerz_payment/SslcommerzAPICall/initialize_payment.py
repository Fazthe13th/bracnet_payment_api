from sslcommerz_lib import SSLCOMMERZ
import os


class SSLCommerzInitialize():
    """
    Call SSLCOMMERZ api
    """
    settings = {'store_id': str(os.getenv("STORE_ID")),
                'store_pass': str(os.getenv("STORE_PASS")), 'issandbox': bool(os.getenv("ISSANDBOX"))}
    sslcommez = SSLCOMMERZ(settings)

    def create_session(self, post_body):
        response = self.sslcommez.createSession(post_body)
        return response
