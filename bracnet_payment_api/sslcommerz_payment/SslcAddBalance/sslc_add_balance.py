import mariadb
import os
from dotenv import load_dotenv
load_dotenv()


class SSLcAddBalance():
    def connect_rdp_db(self):
        try:
            rdp_db = mariadb.connect(
                user=os.environ.get('RDP_USER'),
                password=os.environ.get('RDP_PASSWORD'),
                host=os.environ.get('RDP_HOST'),
                port=int(os.environ.get('RDP_PORT')),
                database=os.environ.get('RDP_HOST')
            )

            print('RDP Database connected')
            return rdp_db
        except mariadb.Error as e:
            print('An error happed: ' + str(e))
            return None

    def add_balance(self, custumer_id, payed_amount):
        rdp_db = self.connect_rdp_db()
        if not rdp_db:
            print('RDP Database not connected')
            return False
        cursor = rdp_db.cursor()
        try:
            cursor.execute("""
                update radius.tbl_rdp_customers set AcctBalance = IFNULL(AcctBalance, 0)+%s where ClientRefId=%s;
                    """, (custumer_id, int(payed_amount)))
            rdp_db.commit()
            cursor.close()
            rdp_db.close()
            return True
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            rdp_db.close()
            return False
