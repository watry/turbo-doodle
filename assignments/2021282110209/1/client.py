from zeep import Client

# In the request, you need to pass the BLZ code for any bank in Germany 
# and it comes back with the bank details.
# You can get plenty of Bank BLZ codes at blzcodes.com.

def getBankInfo(blzcode):
    server_addr = "http://www.thomas-bayer.com/axis2/services/BLZService?wsdl"
    client = Client(server_addr)
    result = client.service.getBank(test_id)
    return result

if __name__ == "__main__":
    test_id = 60050101
    test_result = getBankInfo(test_id)
    print(test_result)
    assert(test_result['bic'] == "SOLADEST600")