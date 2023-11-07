from Game import GameRelease
from validate_decorators import validate_email, validate_non_empty_string

class Publisher:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.releases = []

    def manage_release(self, game, release_date):
        release = GameRelease(game, release_date)
        self.releases.append(release)
