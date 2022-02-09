import pytest
from labs.ideas.ratifier.tests.service.sync_ssr.utils import ingest_service as utils_ingest


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_ingest_falcon_service_happy():
    """Title: Validates ingestion of new falcon service

    Description:

    Steps:
        1. Create a new falcon service definition
        2. Run the sync-ssr
        3. Wait for ingestion of data i.e. sync-ssr to complete
        4. Get data from USD core API
        5. Verify correctness
    """
    utils_ingest.create_falcon_service()
    utils_ingest.run_sync_job()
    utils_ingest.wait_for_sync_job()
    utils_ingest.cook_test_result_data()
    utils_ingest.verify_ingestion()


@pytest.mark.fullqual
def test_ingest_falcon_service_incorrectly():
    """Title: Validates ingestion of new falcon service but with incorrect dataset

    Description:

    Steps:
        1. Create a new but incorrect falcon service definition
        2. Run the sync-ssr
        3. Wait for ingestion of data i.e. sync-ssr to complete
        4. Get data from USD core API
        5. Verify expectation
    """
    utils_ingest.create_falcon_service_incorrect()
    utils_ingest.run_sync_job()
    utils_ingest.wait_for_sync_job()
    utils_ingest.cook_test_result_data()
    utils_ingest.verify_ingestion()
