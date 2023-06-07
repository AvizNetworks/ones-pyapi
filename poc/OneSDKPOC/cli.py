import argparse
from onseSDK.OnesClient.client import ONESClient

def main():
    parser = argparse.ArgumentParser(description='ONES POC SDK')
    parser.add_argument('--base-url', help='Base URL of the API', required=True)
    # parser.add_argument('endpoint', help='API endpoint')
    # parser.add_argument('--method', help='HTTP method', default='GET')
    parser.add_argument('--username', help='Username')
    parser.add_argument('--password', help='Password')

    args = parser.parse_args()

    sdk = ONESClient(args.base_url, args.username, args.password)
    response = sdk.connect()
    print(response)

if __name__ == '__main__':
    main()