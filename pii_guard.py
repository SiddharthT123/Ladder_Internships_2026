def redact_pii(text):
    return text.replace("@", "[REDACTED]")

