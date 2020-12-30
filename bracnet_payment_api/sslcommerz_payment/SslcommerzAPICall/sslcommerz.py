from sslcommerz_lib import SSLCOMMERZ
import os


class SSLCommerzfunc():
    """
    Call SSLCOMMERZ api
    """
    settings = {'store_id': str(os.getenv("STORE_ID")),
                'store_pass': str(os.getenv("STORE_PASS")), 'issandbox': False}
    sslcommez = SSLCOMMERZ(settings)

    def create_session(self, post_body):
        response = self.sslcommez.createSession(post_body)
        return response

    def validate_session(self, val_id):
        response = self.sslcommez.validationTransactionOrder(val_id)
        return response


# {'amount': ['400.00'],
# 'bank_tran_id': ['2012011746531wNTMzVwsFzRmbn'],
# 'base_fair': ['0.00'],
# 'card_brand': ['VISA'],
# 'card_issuer': ['STANDARD CHARTERED BANK'],
# 'card_issuer_country': ['Bangladesh'],
# 'card_issuer_country_code': ['BD'],
# 'card_no': ['432155XXXXXX7491'],
# 'card_sub_brand': ['Classic'],
# 'card_type': ['VISA-Dutch Bangla'],
# 'currency': ['BDT'],
# 'currency_amount': ['400.00'],
# 'currency_rate': ['1.0000'],
# 'currency_type': ['BDT'],
# 'error': [''],
# 'risk_level': ['0'],
# 'risk_title': ['Safe'],
# 'status': ['VALID'],
# 'store_amount': ['390.00'],
# 'store_id': ['bracn5f9fee32c615c'],
# 'tran_date': ['2020-12-01 17:46:17'],
# 'tran_id': ['eca7cb48-5f7b-4640-8c21-2eb30dd3c47e'],
# 'val_id': ['20120117465317Ino4i0EhFOSvZ'],
# 'value_a': [''], 'value_b': [''],
# 'value_c': [''], 'value_d': [''],
# 'verify_sign': ['7ebc61f893e922a3130583cfa740e823'],
# 'verify_sign_sha2': ['44e1e31e47f07712392e4bf3f6fcf987b5a93cebd0e0a0709f8d96ae7ad74ece'],
# 'verify_key': ['amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,risk_level,risk_title,status,store_amount,store_id,tran_date,tran_id,val_id,value_a,value_b,value_c,value_d']}


# {"amount": "500.00",
# "bank_tran_id": "2012031240580q9M1CZM3XHbA6l",
# "base_fair": "0.00",
# "card_brand": "VISA",
# "card_issuer": "TRUST BANK, LTD.",
# "card_issuer_country": "Bangladesh",
# "card_issuer_country_code": "BD",
# "card_no": "418117XXXXXX7814",
# "card_sub_brand": "Classic",
# "card_type": "VISA-Dutch Bangla",
# "currency": "BDT",
# "currency_amount": "500.00",
# "currency_rate": "1.0000",
# "currency_type": "BDT",
# "error": ",
# "risk_level": "0",
# "risk_title": "Safe",
# "status": "VALID",
# "store_amount": "487.50",
# "store_id": "bracn5f9fee32c615c",
# "tran_date": "2020-12-03 12:40:04",
# "tran_id": "794fddc7-023c-4beb-8f1b-f09ed1d25119",
# "val_id": "2012031240581r6GgZhbcQgVZdA",
# "value_a": """,
# "value_b": """,
# "value_c": """,
# "value_d": """,
# "verify_sign": "823e9439b0370dc1bdb90ecf32adda70",
# "verify_sign_sha2": "ce2de5b23d939df4620c4a310a19d6d4c94983d35e483e368208108600c64ff2",
# "verify_key": "amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,risk_level,risk_title,status,store_amount,store_id,tran_date,tran_id,val_id,value_a,value_b,value_c,value_d"}

# 'amount': ['800.00'], 'bank_tran_id': ['201206123442ncmGrbSsNbcu03R'], 'base_fair': ['0.00'], 'card_brand': ['VISA'], 'card_issuer': ['STANDARD CHARTERED BANK'], 'card_issuer_country': ['Bangladesh'], 'card_issuer_country_code': ['BD'], 'card_no': ['421481XXXXXX4177'], 'card_sub_brand': ['Classic'], 'card_type': ['VISA-Dutch Bangla'], 'currency': ['BDT'], 'currency_amount': ['800.00'], 'currency_rate': ['1.0000'], 'currency_type': ['BDT'], 'error': [''], 'risk_level': ['0'], 'risk_title': ['Safe'], 'status': ['VALID'], 'store_amount': ['780.00'], 'store_id': ['bracn5f9fee32c615c'], 'tran_date': ['2020-12-06 12:34:05'], 'tran_id': ['c8278290-737f-4acb-b12a-c753eb11585e'], 'val_id': ['201206123442QE9vod04K32cvtJ'], 'value_a': [''], 'value_b': [''], 'value_c': [''], 'value_d': [''], 'verify_sign': ['73917f39927c647f3cfee4b25ee707e3'], 'verify_sign_sha2': ['143998cba9a5ededbe61d2dc443e36abd629c494f2a4622f398099eb6e3210ec'],

# {'amount': ['1400.00'], 'bank_tran_id': ['2012061608290lHgB2ilNsF3pSe'], 'base_fair': ['0.00'], 'card_brand': [''], 'card_issuer': [''], 'card_issuer_country': [''], 'card_issuer_country_code': [''], 'card_no': [''], 'card_sub_brand': ['Classic'], 'card_type': [''], 'currency': ['BDT'], 'currency_amount': ['1400.00'], 'currency_rate': ['1.0000'], 'currency_type': ['BDT'], 'error': ['3D Security Validation Failed'], 'status': ['FAILED'], 'store_id': ['bracn5f9fee32c615c'], 'tran_date': ['2020-12-06 16:08:06'], 'tran_id': ['58bfe1a7-cb19-44e5-a214-efa2b4df890d'], 'value_a': [''], 'value_b': [''], 'value_c': [''], 'value_d': [''], 'verify_sign': ['02870e86f1b7cb49cda768ee00b927c7'], 'verify_sign_sha2': ['c1f5b631a50201072f4e9efe1ce84ff899faf6fb434f2ba73c24e18aef3a1a15'], 'verify_key': ['amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,status,store_id,tran_date,tran_id,value_a,value_b,value_c,value_d']}
