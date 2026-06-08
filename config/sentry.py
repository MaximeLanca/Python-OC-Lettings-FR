import sentry_sdk
from dotenv import load_dotenv
import os

load_dotenv()

SENTRY_SDK = os.getenv("SENTRY_SDK")

sentry_sdk.init(
    dsn="",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)