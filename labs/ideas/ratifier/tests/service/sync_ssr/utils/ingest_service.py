from labs.ideas.ratifier.associates.ssr import SalesforceServiceRegistry
from labs.ideas.ratifier.associates.sync_job import SyncJob


def create_falcon_service():
    SalesforceServiceRegistry.create_service_defintion('falcon-service-definition', 'test_service.yaml')
    print('Creating a falcon service')


def run_sync_job():
    SyncJob.schedule('air-batch.sync-ssr')
    print('Run sync job')


def wait_for_sync_job():
    print("Waiting for sync job to complete")


def cook_test_result_data():
    print("Cook test result data")


def verify_ingestion():
    print("Verify test data")
