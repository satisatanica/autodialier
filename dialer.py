#!/usr/bin/python
from twilio.rest import Client
import time

def main():

    #Constants
    FROM = "+1234567890"
    TO = "+1234567890"

    CNT = 0
    LIMIT = 20

    ACCOUNT_SID="from_twilio"
    AUTH_TOKEN="from_twilio"
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    while CNT<LIMIT:
         call = client.calls.create(
            to = TO,
            from_ = FROM,
            url = "https://github.com/satisatanica/autodialier/blob/main/voice.xml"
         )

         CNT = CNT+1
         time.sleep(30.0)
if __name__ == '__main__':
    print("Calling the scammer... MUAH HA HA")
    main()
    
