import os
default_scaledown_api="https://api.scaledown.ai/v1/compress"
def get_api_url():
    return os.getenv("SCALEDOWN_API_URL", default_scaledown_api)