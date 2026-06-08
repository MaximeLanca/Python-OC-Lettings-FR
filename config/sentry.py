import sentry_sdk

sentry_sdk.init(
    dsn="https://13280831cc703453e5817aaf6db2249a@o4511416012308480.ingest.de.sentry.io/4511531362025552",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)