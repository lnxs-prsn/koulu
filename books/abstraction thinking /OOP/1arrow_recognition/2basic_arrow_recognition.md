
# 1. Car and GPS # SUCCESS !!
#    Car → GPS? (Car uses GPS for directions)
#    GPS → Car? (GPS needs car location)

# 2. Student and ExamPaper # FAIL !!
#    Student → ExamPaper? (Student takes exam)
#    ExamPaper → Student? (Exam knows whose it is)

# 3. FacebookUser and FriendRequest SUCCESS !!
#    Sender → Request? (Sender creates request)
#    Request → Sender? (Request knows who sent it)
#    Request → Receiver? (Request knows who receives it)
#    Receiver → Request? (Receiver can accept/decline)

# 4. ShoppingCart and DiscountCoupon SUCCESS !!
#    Cart → Coupon? (Cart applies coupon)
#    Coupon → Cart? (Coupon needs cart total to calculate discount)

# Write minimal class sketches showing only the arrows (references)




OUTCOMES
1.student returned this 

ACTION
    -   car asks gps for location
AUTHORITY
# 1. Car and GPS
#    Car → GPS? (Car uses GPS for directions)
#    GPS → Car? (GPS needs car location)
    -   car is the authority 
        -   car tells gps to locate 
-   

PARTICIPANTS ARE 
    -   car and gps 
-   


RESPOSIBILITIES
    -   car orders the gps 
    -   gps stores data

ARROWS
    -   car > gps

2. 

AUTHORITY
# 2. Student and ExamPaper
#    Student → ExamPaper? (Student takes exam)
#    ExamPaper → Student? (Exam knows whose it is)
    -   student is the authority

RESPONSIBILITY
    -   student writes on examp paper
    -   exampaper stores the student writing

PARTICIPANTS 
    -   studen 
    -   exampaper

ACTION
    -   student takes an exam
-   

3.  


PARTICIPANTS 
    -   unmentioned coordinator
    -   sender
    -   request
    -   receiver

AUTHORITY
# 3. FacebookUser and FriendRequest
#    Sender → Request? (Sender creates request)
#    Request → Sender? (Request knows who sent it)
#    Request → Receiver? (Request knows who receives it)
#    Receiver → Request? (Receiver can accept/decline)


    -   it this limited contex ignoring the unmentioned real authority that coordinates and orders
        -   request knows who initiated it only if the initiator passed that information to it and it knows where to send to only if that info was passed to it so its passive actor
        -   sender knows the receiver but has no authority on the receiver so its initiator
            -   it can only send or unsend the invitation
        -   receiver has the authority to accept or refuse 
            -   it knows the request 
            -   it knows the sender
            -   it can take action to turn all participants irrelevant 
            -   or wait indefinitely if it chooses so


RESPONSIBILITIES
    -   sender
        -   tells request to initiate itself
    -   request 
        -   stores its state 
    -   receiver
        -   active one of the all 3 participants 

4.


# 4. ShoppingCart and DiscountCoupon
#    Cart → Coupon? (Cart applies coupon)
#    Coupon → Cart? (Coupon needs cart total to calculate discount)

PARTICIPANTS 
    -   unmentioned shop
        -   within it 
            -   cart
            -   coupon

ACTION
-   cart call coupon to know how much is the discount of its content


AUTHORITY
    -   real authority is unmentiond shop
    -   cart can exist without coupon 
    -   but coupon cannnot exist without cart
    -   so in this limited interaction of the cart and coupon 
        -   active is the cart and passive is the coupon


RESPONSIBILITIES
    -   cart
        -   stores products 
        -   calls coupon its action taker / initiator
    -   coupon 
        -   is passive data storage/ computation location

ARROWS
    -   cart>coupon
    -   cart calls coupon 
    -   coupon returns value