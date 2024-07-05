import heapq
class Twitter(object):

    def __init__(self):
        self.users = {}

    def first_user_action(self, userId):
        self.users[userId] = {
                'followees': set(),
                'tweets': [],
            } 

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if not userId in self.users:
            self.first_user_action(userId)
        self.users[userId]['tweets'].append(tweetId)


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        all_followees_tweets = []
        for followeesId in [*self.users[userId]['followees'], userId]:
            followee_tweets = self.users[followeesId]['tweets']
            if not followee_tweets:
                continue
            elif len(followee_tweets) >= 10:
                followee_tweets = followee_tweets[-10:]
            all_followees_tweets = [*all_followees_tweets, *followee_tweets]
        # all_followees_tweets = [-tweetId for tweetId in all_followees_tweets]
        all_followees_tweets = sorted(all_followees_tweets, reverse=True)
        if len(all_followees_tweets) >= 10:
            all_followees_tweets = all_followees_tweets[:10]
        return all_followees_tweets


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if not followerId in self.users:
            self.first_user_action(followerId)
        self.users[followerId]['followees'].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.users[followerId]['followees'].remove(followeeId)
        

["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 10)
obj.postTweet(1, 2)
obj.postTweet(1, 13)
obj.postTweet(2, 11)
obj.postTweet(2, 3)
obj.follow(1, 2)
obj.follow(2, 1)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.unfollow(2,1)
param_2 = obj.getNewsFeed(2)
print(param_2)