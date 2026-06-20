from collections import defaultdict
from math import sqrt


class RecommendationSystem:
    
    def __init__(self):
        # Store user ratings: {user_id: {item_id: rating}}
        self.user_ratings = defaultdict(dict)
        
    def add_rating(self, user_id, item_id, rating):
        self.user_ratings[user_id][item_id] = rating
    
    def calculate_similarity(self, user1, user2):
        user1_ratings = self.user_ratings[user1]
        user2_ratings = self.user_ratings[user2]
        
        common_items = set(user1_ratings.keys()) & set(user2_ratings.keys())
        
        if not common_items:
            return 0
        
        # Calculate Euclidean distance
        sum_of_squares = sum(
            (user1_ratings[item] - user2_ratings[item]) ** 2 
            for item in common_items
        )
        distance = sqrt(sum_of_squares)
        
        # Convert distance to similarity (inverse relationship)
        similarity = 1 / (1 + distance)
        return similarity
    
    def get_similar_users(self, user_id, n=3):
        if user_id not in self.user_ratings:
            return []
        
        similarities = []
        for other_user in self.user_ratings:
            if other_user != user_id:
                similarity = self.calculate_similarity(user_id, other_user)
                if similarity > 0:
                    similarities.append((other_user, similarity))
        
        # Sort by similarity score (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:n]
    
    def recommend_items(self, user_id, n=3):
        if user_id not in self.user_ratings:
            return []
        
        similar_users = self.get_similar_users(user_id, n=5)
        
        if not similar_users:
            return []
        
        user_rated_items = set(self.user_ratings[user_id].keys())
        recommendations = defaultdict(list)
        
        # Collect ratings from similar users for items the target user hasn't rated
        for similar_user, similarity in similar_users:
            for item_id, rating in self.user_ratings[similar_user].items():
                if item_id not in user_rated_items:
                    # Weight the rating by similarity
                    recommendations[item_id].append(rating * similarity)
        
        # Calculate average weighted rating for each recommended item
        scored_recommendations = []
        for item_id, weighted_ratings in recommendations.items():
            avg_score = sum(weighted_ratings) / len(weighted_ratings)
            scored_recommendations.append((item_id, avg_score))
        
        # Sort by score (descending)
        scored_recommendations.sort(key=lambda x: x[1], reverse=True)
        return scored_recommendations[:n]

if __name__ == "__main__":
    rec_system = RecommendationSystem()
    
    ratings_data = [
        ("Alice", "Movie A", 5),
        ("Alice", "Movie B", 4),
        ("Alice", "Movie C", 3),
        
        ("Bob", "Movie A", 5),
        ("Bob", "Movie B", 3),
        ("Bob", "Movie D", 4),
        
        ("Charlie", "Movie B", 4),
        ("Charlie", "Movie C", 5),
        ("Charlie", "Movie D", 2),
        
        ("David", "Movie A", 4),
        ("David", "Movie C", 5),
        ("David", "Movie E", 3),
    ]
    for user_id, item_id, rating in ratings_data:
        rec_system.add_rating(user_id, item_id, rating)
    
    print("=" * 50)
    print("RECOMMENDATION SYSTEM DEMO")
    print("=" * 50)
    
    target_user = "Alice"
    print(f"\nFinding recommendations for {target_user}...")
    print(f"\nItems {target_user} has already rated:")
    for item, rating in rec_system.user_ratings[target_user].items():
        print(f"  - {item}: {rating}/5")
    
    # Find similar users
    print(f"\nMost similar users to {target_user}:")
    similar_users = rec_system.get_similar_users(target_user)
    for user, similarity in similar_users:
        print(f"  - {user}: {similarity:.2f} similarity")
    
    # Get recommendations
    recommendations = rec_system.recommend_items(target_user, n=3)
    print(f"\nTop 3 recommendations for {target_user}:")
    for item, score in recommendations:
        print(f"  - {item}: {score:.2f} predicted rating")
    
