request_erc20_proxy = [{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'tokenAddress', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'indexed': True, 'internalType': 'bytes', 'name': 'paymentReference', 'type': 'bytes'}], 'name': 'TransferWithReference', 'type': 'event'}, {'payable': True, 'stateMutability': 'payable', 'type': 'fallback'}, {'constant': False, 'inputs': [{'internalType': 'address', 'name': '_tokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '_paymentReference', 'type': 'bytes'}], 'name': 'transferFromWithReference', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}]
request_ethereum_proxy = [{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'indexed': True, 'internalType': 'bytes', 'name': 'paymentReference', 'type': 'bytes'}], 'name': 'TransferWithReference', 'type': 'event'}, {'payable': True, 'stateMutability': 'payable', 'type': 'fallback'}, {'constant': False, 'inputs': [{'internalType': 'address payable', 'name': '_to', 'type': 'address'}, {'internalType': 'bytes', 'name': '_paymentReference', 'type': 'bytes'}], 'name': 'transferWithReference', 'outputs': [], 'payable': True, 'stateMutability': 'payable', 'type': 'function'}]