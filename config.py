from decouple import config

api_hash = config('API_HASH')
api_id = config('API_ID')

# input_chat_id = config('INPUT_CHAT_ID')
# output_chat_id = config('OUTPUT_CHAT_ID')
input_chat_id = 'reciever_1_0_1'
output_chat_id = 'forwarder_1_0_1'
session = config('SESSION')