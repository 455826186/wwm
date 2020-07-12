import requests
def cz_tx(url,data,token=None):
    header = {"X-Lemonban-Media-Type": "lemonban.v2",
           "Authorization":token}
    rec=requests.post(url,json=data,headers=header)
    rec_1=rec.json()
    return rec.json()

log_qqt={"X-Lemonban-Media-Type":"lemonban.v2"}
log_msg={'mobile_phone':15659070234,'pwd':123456789}
log_url="http://120.78.128.25:8766/futureloan/member/login"
response=cz_tx(url=log_url,data=log_msg)

#充值
token=response["data"]["token_info"]["token"]
rec_url = "http://120.78.128.25:8766/futureloan/member/recharge"
rec_msg = {'member_id': '196343', 'amount': '50000'}

print(cz_tx(rec_url,rec_msg,"Bearer "+token ))

