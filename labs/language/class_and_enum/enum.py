# (c) Copyright 2018 Hewlett Packard Enterprise Development LP
"""request status module."""

from enum import Enum


class RequestStatus(Enum):
    """Enumerated list of request status.

    It defines generic status which a request will have transition
    through. It should be good enough to cover most of cases but
    if there is specialized status is needed then one can define
    new one by inheriting this class (in the worst case by creating
    a new one).
    """

    CREATED = 1
    QUEUED = 2
    DROPPED = 3
    PRE_PROCESSING = 4
    PROCESSING = 5
    WAITING_FOR_CHILD_PROCESSING = 6
    POST_PROCESSING = 7
    PARTIAL_SUCCESS = 8
    ERRORED = 9
    SUCEESS = 10
    ROLLING_BACK = 11
    WAITING_FOR_CHILD_ROLLING_BACK = 12
    ROLLBACK_ERRORED = 13
    ROLLED_BACK_PARTIALLY = 14
    ROLLED_BACK = 15


REQUEST_STATUS_TRANSITION_MAP = [
    {RequestStatus.CREATED: [RequestStatus.QUEUED, RequestStatus.DROPPED]},
    {RequestStatus.QUEUED: [
        RequestStatus.DROPPED,
        RequestStatus.PRE_PROCESSING]},
    {RequestStatus.DROPPED: []},
    {RequestStatus.PRE_PROCESSING: [
        RequestStatus.DROPPED,
        RequestStatus.PROCESSING,
        RequestStatus.ERRORED]},
    {RequestStatus.PROCESSING: [
        RequestStatus.POST_PROCESSING,
        RequestStatus.PROCESSING,
        RequestStatus.ERRORED]},
    {RequestStatus.WAITING_FOR_CHILD_PROCESSING: [RequestStatus.PROCESSING]},
    {RequestStatus.POST_PROCESSING: [
        RequestStatus.PARTIAL_SUCCESS,
        RequestStatus.SUCEESS,
        RequestStatus.ERRORED,
        RequestStatus.ROLLING_BACK]},
    {RequestStatus.PARTIAL_SUCCESS: []},
    {RequestStatus.ERRORED: []},
    {RequestStatus.SUCEESS: []},
    {RequestStatus.ROLLING_BACK: [
        RequestStatus.ROLLED_BACK,
        RequestStatus.ROLLED_BACK_PARTIALLY,
        RequestStatus.WAITING_FOR_CHILD_ROLLING_BACK,
        RequestStatus.ROLLBACK_ERRORED]},
    {RequestStatus.WAITING_FOR_CHILD_ROLLING_BACK: [
        RequestStatus.ROLLING_BACK]},
    {RequestStatus.ROLLED_BACK_PARTIALLY: []},
    {RequestStatus.ROLLBACK_FAILED: []},
    {RequestStatus.ROLLED_BACK: []},
]


if __name__ == "__main__":
    print REQUEST_STATUS_TRANSITION_MAP
    val == 1
    if value == RequestStatus.CREATED:
        print("Helllo")