from hamcrest.core.base_matcher import BaseMatcher
import uuid


class IsUUID(BaseMatcher):

    def __init__(self):
        pass

    def _matches(self, item):
        try:
            uuid.UUID(item)
            return True
        except ValueError:
            return False

    def describe_to(self, description):
        description.append_text("Valid UUID string")


def is_uuid():
    return IsUUID()
