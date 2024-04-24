# Initialize high scores tracker
class ScoreTracker():
    def __init__(self): 
        self.score_tracker = []

    def submit_score(self, score):
        self.score_tracker.append(score)
        self.score_tracker.sort(reverse=True)
        return None

    def display_scores(self):
        print("Top 5 Scores:")
        top_5 = self.score_tracker[:5]
        for idx, item in enumerate(top_5):
            print(f"{idx+1}. {item}", end="\n")


score_tracker = ScoreTracker()

# Submit scores
score_tracker.submit_score(800)
score_tracker.submit_score(600)
score_tracker.submit_score(350)
score_tracker.submit_score(1000)
score_tracker.submit_score(950)
score_tracker.submit_score(700)
score_tracker.submit_score(900)

# Display current top 5 scores
score_tracker.display_scores()