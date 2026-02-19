#!/usr/bin/env python3

import argparse
import json
import os

from modules.xss import generate_xss
from modules.sqli import generate_sqli
from modules.cmdi import generate_cmdi
from utils.encoder import encode_payload


# Export Function
def export_payloads(payloads, format, module):

    # Ensure outputs directory exists
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)


    # JSON Export
    if format == "json":

        filename = os.path.join(output_dir, f"{module}_payloads.json")

        with open(filename, "w") as f:
            json.dump(payloads, f, indent=4)

        print(f"\n[+] Payloads exported to {filename}")


    # TXT Export
    elif format == "txt":

        filename = os.path.join(output_dir, f"{module}_payloads.txt")

        with open(filename, "w") as f:

            for payload in payloads:
                f.write(payload + "\n")

        print(f"\n[+] Payloads exported to {filename}")



def main():

    parser = argparse.ArgumentParser(
        description="SecLearnz - Educational Payload Generator Framework"
    )


    parser.add_argument(
        "--module",
        choices=["xss", "sqli", "cmdi"],
        required=True,
        help="Select payload module"
    )


    parser.add_argument(
        "--encode",
        choices=["url", "base64", "hex"],
        help="Encode payloads"
    )


    parser.add_argument(
        "--db",
        choices=["mysql", "postgres", "mssql"],
        help="Database type (SQLi only)"
    )


    parser.add_argument(
        "--export",
        choices=["json", "txt"],
        help="Export payloads to outputs directory"
    )


    args = parser.parse_args()



    # Module selection
    if args.module == "xss":

        payloads = generate_xss()


    elif args.module == "sqli":

        payloads = generate_sqli(args.db)


    elif args.module == "cmdi":

        payloads = generate_cmdi()



    # Encoding
    if args.encode:

        payloads = encode_payload(payloads, args.encode)



    # Display
    print("\n===================================")
    print("   SecLearnz Payload Generator")
    print("===================================\n")

    print(f"[+] Module: {args.module.upper()}\n")


    for payload in payloads:

        print(f"[TEMPLATE] {payload}")



    # Export
    if args.export:

        export_payloads(payloads, args.export, args.module)



if __name__ == "__main__":

    main()
