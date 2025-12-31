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

### **PART 2: IDENTIFY CORE COMPONENTS**  # I got this part wrong ai solution is what am using here

What are the main "things" involved?
• user (most important)
• post
• feed

For EACH thing:
USER

- What DATA does it need? username,list of post they created, (liked posts)
- What ACTIONS can it do? create_post(), like_post(), view_feed()
- How does it relate to others? user creates posts,likes posts and views the feed

For EACH thing:
POST

- What DATA does it need? content, author:User object,likes_count, time_stamp 
- What ACTIONS can it do? add_like(), view_post_info()
- How does it relate to others? post belongs to a User, appears in the feed, can be liked by Users

For EACH thing:
FEED

- What DATA does it need? collection/list of all posts, 
- What ACTIONS can it do? add_post(), display_feed(), sort_by_time(), sort_by_likes()
- How does it relate to others? feed contains posts from multiple Users and displays them to the Users

### **PART 3: DESIGN DECISIONS** # got this wrong

Structure:
[ ] Classes with composition (Container→Contained)
- user creates post, user likes a post

Communication:
[ ] Direct calls between objects

Data Storage:
[ ] In-memory only

-

### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build User and Post classes with basic relationships
         (Test: Can I create user, can user create post, does the post reference correctly user?)

PHASE 2: Add feed class to aggregate post (to add and store post)
         (Connects via: feed has an method that receives and post object any user can pass to it a post)

PHASE 3: Add like method to the post and ensure that no object exist without connection it was designed to have
         (Completes: users can like post, posts track likes, all relationships remain valid)

STOP CRITERIA: 
    1. users can create post that correctly remembers its author
    2. users can like other users posts, updating post like count
    3. the feed can display all posts with their author and like counts
    4. no post exists without a valid user author

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
