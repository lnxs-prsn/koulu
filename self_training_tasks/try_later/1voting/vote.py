class VoteInterface:
    def __init__(self, voter):
        self.vote = Vote(voter)







class Vote:
    def __init__(self, voter):
        self.voter = voter
        