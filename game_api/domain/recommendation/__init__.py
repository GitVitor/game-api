class Recommendation():
    def __init__(self, id, helpful, funny, date, is_recommended, user_id, review):
        self._id = id
        self._helpful = helpful
        self._funny = funny
        self._date = date
        self._is_recommended = is_recommended
        self._user_id = user_id
        self._review = review

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_helpful(self):
        return self._helpful

    def set_helpful(self, value):
        self._helpful = value

    def get_funny(self):
        return self._funny

    def set_funny(self, value):
        self._funny = value

    def get_date(self):
        return self._date

    def set_date(self, value):
        self._date = value

    def get_is_recommended(self):
        return self._is_recommended

    def set_is_recommended(self, value):
        self._is_recommended = value

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value

    def get_review(self):
        return self._review

    def set_review(self, value):
        self._review = value
