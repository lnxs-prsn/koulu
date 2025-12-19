what is the action object or objects 
are doing

Translate task requirements into actions:
example 
    -   "Prevent double-voting" → "System validates single vote per voter"
-   




### Social Media Post Manager  
**Purpose**: Simulate a minimal feed with users and posts.  
**Classes**:
- `User` (username, posts)
- `Post` (content, author: User, likes: int)
- `Feed` (aggregates posts; methods to display feed, like a post)

**Core Challenge**: Maintain referential integrity (e.g., a post must always have a valid author; liking updates both post and possibly user stats).


ACTIONS
  -   have a wall(feed) where messages(posts) are added to by the users(users)
  -   create a user
  -   create a post
  -   send a post
  -   add post to wall(feed)