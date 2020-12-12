gcloud run deploy \
    --project $PROJECT_ID \
    --image $IMAGE \
    --region asia-northeast1 \
    --platform managed \
    --concurrency 1 \
    --max-instances 1 \
    --update-env-vars SPREADSHEET_ID=$SPREADSHEET_ID \
    --quiet \
    --service-account $SERVICE_ACCOUNT \
    covid19-status-of-medical-care-provision-in-japan
