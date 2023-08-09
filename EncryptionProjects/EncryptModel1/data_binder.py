import salt_pack
def bind_data(enc_data_parts):
    stage1_result = ''
    for x in enc_data_parts:
        stage1_result = stage1_result + x + salt_pack.get_salt()
    return stage1_result