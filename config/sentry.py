import sentry_sdk
from dotenv import load_dotenv
import os

load_dotenv()

SENTRY_DSN = os.getenv("SENTRY_SDK")


def init_sentry():
    if SENTRY_DSN:
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            send_default_pii=True,
            traces_sample_rate=1.0,
        )
