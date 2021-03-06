#!/usr/bin/env python3
from trezorlib.client import TrezorClient
from trezorlib.transport import get_transport
from trezorlib.tools import parse_path


def main():
    # Use first connected device
    transport = get_transport()

    # Creates object for manipulating TREZOR
    client = TrezorClient(transport)

    # Print out TREZOR's features and settings
    print(client.features)

    # Get the first address of first BIP44 account
    # (should be the same address as shown in wallet.trezor.io)
    bip32_path = parse_path("44'/0'/0'/0/0")
    address = client.get_address('Bitcoin', bip32_path)
    print('Bitcoin address:', address)

    client.close()


if __name__ == '__main__':
    main()
