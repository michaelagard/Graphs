import sys
import random

from queue import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}  # Verticies
        self.friendships = {}  # Dictionary of users and their edges

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for num in range(numUsers):
            self.addUser(f"User {num}")
        # Declare friend list array variable
        friend_list = []
        # Iterate over the range of numUsers + 1 for i, j
        for user_id in range(numUsers + 1):
            for friend_id in range(numUsers + 1):
                # Check if
                if user_id + 1 != friend_id and user_id < friend_id:
                    friend_list += [[user_id + 1, friend_id]]
        random.shuffle(friend_list)
        friend_list = friend_list[:numUsers]
        for x, y in friend_list:
            self.addFriendship(x, y)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        visited = {userID: [userID]}
        queue = Queue()
        queue.enqueue([userID])

        while queue.len() > 0:

            path = queue.dequeue()

            node = path[-1]

            for friend in self.friendships[node]:
                if friend not in visited:

                    upath = path + [friend]

                    visited[friend] = upath

                    queue.enqueue(upath)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
