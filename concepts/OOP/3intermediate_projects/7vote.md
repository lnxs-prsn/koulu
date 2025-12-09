### **1. **Distributed Voting System** 🇺🇸**
Requirements:
- Voters can vote online or in-person
- Votes must be anonymous but verifiable
- System must prevent double-voting
- Election commission can audit
- Political parties can observe (but not identify voters)
- Results should be real-time but can't leak early

Analysis Questions:
1. Who creates a Vote object? Voter or System?
   -   system
2. How does anonymity work with verification?
   -   anonymity links the id to vote but does not store raw data
   -   so verification never directly access the id or the vote
   -   anonymity asks id and the vote if its valid according to system rules
   -   then returns result to verification
3. What prevents someone from voting twice?
   -   system rules and verification
4. Who has authority to finalize results?
   -   system

Implementation Task:
Design Python classes for:
- Voter (with authentication)
- Vote (anonymous but traceable)
- BallotBox (collects votes)
- Auditor (validates without breaking anonymity)
- ResultsPublisher (releases at specific time)





outcome of thinking it before doing

### **1. **Distributed Voting System** 🇺🇸**
Requirements:
- Voters can vote online or in-person
- Votes must be anonymous but verifiable
- System must prevent double-voting
- Election commission can audit
- Political parties can observe (but not identify voters)
- Results should be real-time but can't leak early


ACTIONS
  -   voters can vote
  -   votes must be anonymous but verifiable # this appears to be static state rather than verb
  -   system must prevent double-voting # this too appears to be static rather than verb but prevent is also a verb
  -   election commission can audit
  -   political parties can observe
  -   result should be real-time but cant leak early  # this too appears to be state rather than verb


PARTICIPANTS
  -   Voter
  -   vote
  -   ballotbox
  -   anonymization
  -   validation
  -   election system
  -   election commision
  -   politicalobserver


RESPONSIBILITIES
  -   voter
      -   fills an vote
  -   vote 
      -   stores and vote
  -   ballotbox
      -   receives an vote
      -   might call validation check on vote and voter
  -   election system
      -   coordinates everything
  -   anonymization
      -   anonymization is applied on creation of voter object if data of creation is valid
      -   its applied again when creating vote object
  -   validation 
      -   called everytime when checking if system rules are applied correctly
  -   election commision
      -   checks if system works according to rules set for the system
      -   declare the result received from the election system
  -   political observer
      -   can check superfiacially if there is anomalies 


AUTHORITY
  -   election system
      -   coordinator
      -   has full authority as long as passes validation checks of  the election commision
      -   everything goes through it in the voting process
  -   election commision
      -   declaration authority
      -   has full authority as long as not challenged by the political observer
  -   political observer
      -   validation authority
          -   validates result by agreeing with it
      -   gains authority only if anomalies in the process else passive observer
  -   vote 
      -   participant/storage
  -   voter
      -   initiator
      -   participant/storage
  -   ballotbox
      -   participant/storage
  -   anonymization
      -   data scrambler/ not storage
  -   validation
      -   state validator/not storage


ARROWS
  -   election system > (vote,voter,ballotbox,anonymization, validation)
  -   electioncommittee > election system and election system > election committee
  -   political oberver > election system and election system > political observer  
      -   above is for getting obervation access
      -   also political observer > electioncommitee and electioncommitee > political observer


TASK CONSTRAINTS 
  -   the anonymizatino is one constrains 
  -   other is organizing limited access to those in need of limited.
  -   legal requirements are also an constraint