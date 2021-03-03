from utils import Date
import base64
import datetime


def tic_5_sec():
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
#     pubsub_message = base64.b64decode(event['data']).decode('utf-8')
#     print(pubsub_message)
#     print('Hellog 5 sec')
    print(Date.print_date_iso())
