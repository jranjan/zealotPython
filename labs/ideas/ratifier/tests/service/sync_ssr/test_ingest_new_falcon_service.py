import pytest

@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_ingest_falcon_service_happy():
    '''Title: Validates ingestion of new falcon service

    Description:

    Steps:
        1. Create a new falcon service definition
        2. Run the sync-ssr
        3. Wait for ingestion of data i.e. sync-ssr to complete
        4. Get data from USD core API
        5. Verify correctness
    '''
    create_falcon_service()
    run_sync_job()
    wait_for_sync_job()
    cook_test_result_data()
    verify_ingestion()
