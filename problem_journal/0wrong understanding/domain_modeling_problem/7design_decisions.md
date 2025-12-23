 bring here
 -  the authority section  
 -  responsibility section
 -  participants section
 -  arrows section



If an object's job is to...	                            Then it should NOT...
- Store Data (Voter list, votes, rules)	                - Perform logic on that data. It should be a "dumb" data holder.
- Compute/Validate (Check eligibility, tally votes)	    - Permanently store the data it's checking. It should get data, check it, and return a result.
- Coordinate (Manage the process flow)	                - Know the internal details or hold sensitive data from the objects it coordinates.


When designing each class, ask:

What is this object's ONE reason to change? (SRP)

Example: VoterRegistry changes if registration laws change, NOT if vote storage format changes.

What does it need to do its job? Give it only that. (DIP/Demeter)

Example: Give Validation the Rules object, not access to the entire system.

Can I describe its purpose without using "and"? (SRP Test)

"Stores encrypted votes and validates them" → BAD

"Stores encrypted votes" → GOOD

"Validates vote format" → GOOD


there is function main() 
  -   this function passess the coordinator object to the initiator objects.


so system level coordinator needs to always know the participants 

but the orchesterator only needs to know the coordinator





### Social Media Post Manager  
**Purpose**: Simulate a minimal feed with users and posts.  
**Classes**:
- `User` (username, posts)
- `Post` (content, author: User, likes: int)
- `Feed` (aggregates posts; methods to display feed, like a post)

**Core Challenge**: Maintain referential integrity (e.g., a post must always have a valid author; liking updates both post and possibly user stats).


ACTIONS
  -   feed shows post
  -   user writes posts
  -   post are passive


PARTICIPANTS
  -   feed
  -   user
  -   post


RESPONSIBILITY
  -   Feed is the coordinator if there is no higher authority system
      -   stores the posts that users makes
      -   validates which can be shown 
      -   validates who can post etc
  -   to request for posting
      -   stores user data: username,age etc
  -   post storage
      -   knows only what is written to it, who has written


AUTHORITY
  -   if there is no higher authority 
      -   then feed is the coordinator
  -   user is the initiator
  -   post  passive participant


ARROWS
  - user > feed > post
    - user request from the feed

TASK CONSTRAINTS
  - posting a post to feed
    - there must be a post and there must be a user
    - there cannot be an post without user
    - post must be linkable to user



DESIGN DECISION
  - feed
    - all the logic happens in the feed
    - this imports the post and the user
    - all the validation happens in here
    - stores list of tuples or list of list or dict keys are users and values are list of posts
  - post
    - does not import object
    - the main() passess to it any object they need
  - user 
    - has method to request for posting a post
      - passes what it wants to be posted with the request to feed
      - stores the post content
        - might also store who posted data
  - 