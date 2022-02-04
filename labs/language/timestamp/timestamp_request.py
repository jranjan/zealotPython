# (c) Copyright 2018 Hewlett Packard Enterprise Development LP
"""request module."""

import logging
import uuid


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import time


class RequestTimestamp(object):
    """A class to hold timestamp related information.

    A class to hold various fields used to track timing aspect of request
    during its processing. In long run, it will be innovated to give end
    user a perspective of status of ongoing task, something like time
    progress details
    """

    def __init__(self):
        """Class initializer."""
        self.createAt = time.time()
        self.startedFlightAt = None
        self.completedAt = None

    def get_creation_time(self):
        return self.createAt

    def set_flight_time(self):
        """Set the flight time when called."""
        self.startedFlightAt = time.time()

    def set_completion_time(self):
        """Set the request completion time when called."""
        self.completedAt = time.time()

    def get_elabsed_time_since_creation(self):
        """Get total time elapsed since request was created."""
        return time.time() - self.createAt

    def get_elapsed_time_since_flighted(self):
        """Get total time elapsed since request was in-flight."""
        if self.startedFlightAt:
            return time.time() - self.startedFlightAt
        return 0

    def get_flight_time_onnly(self):
        """Get total time elapsed only when request was in-flight."""
        if self.completedAt and self.startedFlightAt:
            return self.completedAt - self.startedFlightAt
        return 0

    def get_completion_time(self):
        """Get total time elapsed to process the request."""
        if self.completedAt:
            return self.completedAt - self.startedFlightAt
        return 0


class Request(object):
    """A base class for any request. It defines language-field."""

    def __init__(self, code, payload, receiver, parent=None):
        """Class initializer."""
        self.code = code
        self.payload = payload
        self.receiver = receiver

        self._serial = True
        self._synchronous = True
        self._status = 1 #RequestStatus.CREATED
        self._id = uuid.uuid1()

        self.child_request = None
        self.prev_state = None
        self.current_state = None
        self.timestamp = RequestTimestamp()
        self.response = None
        self.parent_request = parent

    def set_child_request(self, r):
        print(r)
        self.child_request = r

    def __str__(self):
        d = dict()
        d['id'] = self._id
        d['code'] = self.code
        d['payload'] = self.payload
        d['is_serial'] = self._serial
        d['is_synchronous'] = self._synchronous
        d['parent'] = self.parent_request
        d['child'] = self.child_request
        d['status'] = self._status
        d['prev_state'] = self.prev_state
        d['curr_state'] = self.current_state
        d['receiver'] = self.receiver
        d['timestamp'] = dict()
        d['timestamp']['created_at'] = time.ctime(self.timestamp.get_creation_time())
        temp = self.timestamp.get_elabsed_time_since_creation()
        d['timestamp']['elapsed_flight_time'] = temp if temp != 0 else -1
        d['timestamp']['elapsed_time'] = self.timestamp.get_elabsed_time_since_creation()
        temp = self.timestamp.get_completion_time()
        d['timestamp']['completed_at'] = temp if temp != 0 else -1
        temp = self.timestamp.get_completion_time()
        d['timestamp']['total_elapsed_time'] = temp if temp != 0 else -1
        return str(d)



    def set_response(self, response):
        """Set response, to be called after processing request."""
        self.response = response

    def get_response(self):
        """Get response."""
        return self.response

    def get_status(self):
        """Get the current status of request."""
        return self._status

    def set_status(self, status):
        """Set the status of the request.

        This function raises exception if the status transition is not as
        per design (or pre-defined algorithm). Caller of the function needs
        to handle the exception.
        """
        try:
            possible_status = REQUEST_STATUS_TRANSITION_MAP[self._status]
            if not possible_status:
                msg = ("Already in the terminal status %s, asked to "
                       "set status to %s" % (self._status, status))
                logger.error(msg)
                raise InvalidRequestStatusTransitionException(msg)
            else:
                valid_transition = False
                for s in possible_status:
                    if status == s:
                        valid_transition = True
                        break
                if valid_transition:
                    self._status = status
                else:
                    msg = ("Invalid status transition "
                           "from %s to %s" % (self._status, status))
                    logger.error(msg)
                    raise InvalidRequestStatusTransitionException(msg)
        except KeyError:
            msg = ("Status is not valid %s" % (status))
            logger.error(msg)
            raise InvalidRequestStatusTransitionException(msg)

    def is_serial_type(self):
        """Check if request needs to be procesed in serial order or not."""
        return self._serial

    def set_serial_type(self, serial=True):
        """Set request order."""
        self._serial = serial

    def get_id(self):
        """Get ID of request."""
        return self._id

    def is_synchronous_type(self):
        """Check if request needs to be procesed in synchronously or not."""
        return self._synchronous

    def set_synchronous_type(self, synchronous=True):
        """Set request type."""
        self._synchronous = synchronous

    def execute(self, r):
        """Invoke receiver to process the request."""
        self.receiver.do(r)



if __name__ == "__main__":
    r1 = Request(None, None, None, None)
    r2 = Request(None, None, None, r1)
    r1.set_child_request(r2)
    print("r1" + "." * 79)
    print(r1)
    print("r2" + "." * 79)
    print(r2)
