from sslcommerz_lib import SSLCOMMERZ
import os


class SSLCommerzfunc():
    """
    Call SSLCOMMERZ api
    """
    settings = {'store_id': str(os.getenv("STORE_ID")),
                'store_pass': str(os.getenv("STORE_PASS")), 'issandbox': bool(os.getenv("ISSANDBOX"))}
    sslcommez = SSLCOMMERZ(settings)

    def create_session(self, post_body):
        response = self.sslcommez.createSession(post_body)
        return response

    def validate_session(self, post_body):
        response = self.sslcommez.hash_validate_ipn(post_body)
        return response


# {'amount': ['400.00'], 'bank_tran_id': ['2012011746531wNTMzVwsFzRmbn'], 'base_fair': ['0.00'], 'card_brand': ['VISA'], 'card_issuer': ['STANDARD CHARTERED BANK'], 'card_issuer_country': ['Bangladesh'], 'card_issuer_country_code': ['BD'], 'card_no': ['432155XXXXXX7491'], 'card_sub_brand': ['Classic'], 'card_type': ['VISA-Dutch Bangla'], 'currency': ['BDT'], 'currency_amount': ['400.00'], 'currency_rate': ['1.0000'], 'currency_type': ['BDT'], 'error': [''], 'risk_level': ['0'], 'risk_title': ['Safe'], 'status': ['VALID'], 'store_amount': ['390.00'], 'store_id': ['bracn5f9fee32c615c'], 'tran_date': ['2020-12-01 17:46:17'], 'tran_id': ['eca7cb48-5f7b-4640-8c21-2eb30dd3c47e'], 'val_id': ['20120117465317Ino4i0EhFOSvZ'], 'value_a': [''], 'value_b': [''], 'value_c': [''], 'value_d': [''], 'verify_sign': ['7ebc61f893e922a3130583cfa740e823'], 'verify_sign_sha2': ['44e1e31e47f07712392e4bf3f6fcf987b5a93cebd0e0a0709f8d96ae7ad74ece'], 'verify_key': ['amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,risk_level,risk_title,status,store_amount,store_id,tran_date,tran_id,val_id,value_a,value_b,value_c,value_d']}
