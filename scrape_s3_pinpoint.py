from flask import json
from collections import defaultdict

from app.models.campaign import PinpointEmailCampaign
from app.utils.aws import get_s3_bucket
from datetime import datetime, timedelta

cpn_id = "6552678d21e7d914d8e10724"
cpn_obj = PinpointEmailCampaign.objects.with_id(cpn_id)
pp_campaign = cpn_obj.pp_campaign
dt = cpn_obj.date_first_published

events = defaultdict(lambda: [])

bucket = get_s3_bucket("feathr-pinpoint-events")

continue_flag = True

while continue_flag and dt < datetime.utcnow():
    print(dt)
    dt_prefix = f'events{datetime.strftime(dt, "%Y/%m/%d/%H")}'
    for item in bucket.objects.filter(Prefix=dt_prefix):
        decoded = item.get()["Body"].read().decode("utf8").splitlines()
        for event in decoded:
            try:
                event = json.loads(event)
            except Exception:
                continue
            if event.get("attributes", {}).get("campaign_id") == pp_campaign:
                mail_event = (
                    event.get("facets", {})
                    .get("email_channel", {})
                    .get("mail_event", {})
                )
                event_type = event.get("event_type", "")
                events[event_type].append(event)
    dt += timedelta(hours=1)
