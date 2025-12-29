### Social Media Post Manager  
**Purpose**: Simulate a minimal feed with users and posts.  
**Classes**:
- `User` (username, posts)
- `Post` (content, author: User, likes: int)
- `Feed` (aggregates posts; methods to display feed, like a post)

**Core Challenge**: Maintain referential integrity (e.g., a post must always have a valid author; liking updates both post and possibly user stats).

# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
bulletin board where users can pin messages to*
ai: I am modeling an social media platform where users can create posts 
see feed of posts by different users and interact with posts by likin or unliking.
the key is maintaining proper relationship between users and their content


What's the SIMPLEST possible version that would work?
user makes a post then it gets added to feed
ai:
  1.  users who can exist an make posts  
  2.  posts that belong to specific users and can be liked
  3.  a feed that shows posts in reverse chronological order(newest first)
  4.  basic liking functionality that updates the like count of post

What should users be able to DO?

1. :create user account
2. :create a post and publish it
3. :get the post added to feed
4. :interact with the post in the feed like/unlike
AI:
1. USER MANAGMENT: create user account view user profiles with their posts
2. POST MANAGEMENT: create new posts delete their own posts view posts by specific users
3. SOCIAL INTERACTION: like/unlike posts (any user can like any post) see total likes on posts
4. FEED VIEWING: see chronological feed of all posts possibly with filtering/sorting options


-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• feed (most important)
• user
• post

For EACH thing:
FEED

- What DATA does it need? post, user
- What ACTIONS can it do? it can add post to feed, it can ensure that rules are applied correctly
- How does it relate to others? it coordinates

For EACH thing:
USER

- What DATA does it need? username,bio
- What ACTIONS can it do? it can make post and request them to be added to feed, it can like post of other users
- How does it relate to others? it interacts throught the feed

For EACH thing:
POST

- What DATA does it need? user, content, like
- What ACTIONS can it do? it can store data
- How does it relate to others? its acted on by the coordinator
-

AI
What are the main "things" involved?
• user (most important)
• post
• feed

For EACH thing:

- What DATA does it need? ________________
- What ACTIONS can it do? ________________
- How does it relate to others? __________

### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Single class
[ ] Multiple independent classes  
[ ] Classes with inheritance (Parent→Child)
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Direct calls between objects
[ ] Through central coordinator
[ ] Events/messages

Data Storage:
[ ] In-memory only
[ ] Files
[ ] Database (later)

-

### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build ________________________
         (Test: Can it ________________?)

PHASE 2: Add _________________________
         (Connects via: _______________)

PHASE 3: Add _________________________
         (Completes: __________________)

STOP CRITERIA: _______________________

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
