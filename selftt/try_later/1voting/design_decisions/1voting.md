 bring here
 -  the authority section  
 -  responsibility section
 -  participants section
 -  arrows section




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




DESIGN DECISIONS
    -   CLASSES
        -   election system 
            -   everything goes through this one
        -   election committee
            -   calls elections_system.validator.is_election_valid()
        -   observer
            -   calls elections_system.validator.is_election_valid()
        -   ballotbox
            -   is called by the election system to store the vote
            -   keeps count of the votes 
            -   keeps count of the valid and invalid votes
        -   voter
            -   is instantiated throught the anonymizer object so no one in the system knows the voter
                -   only if voter is valid or invalid is known
            -   calls election system to get vote instance
            -   calls election system to vote
            -   
        -   vote
            -   needs voter interface to be initiated by the voter
            -   vote cannot know who voted only store data of what was voted
        -   voteinterface
            -   voter initiates the vote through the voteinterface
            -   am assuming that real flow is voter requests > election system then election system > voteinterface > vote(voter)
        -   validator
            -   this one can contain multiple objects validation methods
                -   all stored in one place if later changes need to be done all can be found in one place
        -   anonymizer 
            -   this must be made an object so its integrity can allways be checked and if anonymization protocol changes 
            -   it can become an continuation so integrity of the whole system can be ensured 

    -   class methods 
        -   election system 
            -  initiate voter
            -  electionsystem.new_voter(user_id)
               -  Validate.validate_user(user_id) 
               -  if true
               -  Anonymize.user(user_id) retuns token
               -  token is passed to Voter(token) 
            -  validate user
               -  validate_user()
                  -  calls Validate.validate_user()
            -  new_vote()
               -  electionsystem calls 
                  -  voteinterface.new_vote(vote)
                  -  and voteinterface will return object
                     -  Vote(vote)
                        -  Vote has an mechanism that instance can only be created once and its immutable
                        -  it cannot be deleted after creation
            -  anonymize voter
               -  anonymize()
               -  this method  is called when creating voter
               -  after Validation return true
               -  d
            - observer access 
                - observe(self)
                  - this method returns 
                    - count of
                      - all the valid voters 
                      - invalid invalid voter
                      - valid votes
                      - invalid votes
                      - any system malfunctions 
                        - not details of problems but enough so observers can have either doubt ot not
                      - it gives in that moments leader or winner if the voting time is over
                      - if asked it can give demographics of the votes 
                        - not sure if I should implement this 
            -   commission access
                -   integrity_test
                    -   calls validator.validate_election(self)
                        -   method checks all the metrics set for the election
                        -   if there are anomalies in the numbers 
                            -   are there more people electing for example than known elector count
                        -   if there have been tampering with the rules set for election
                            -   returns time stamp of the latest change to rules
                                -   should probably make test to see if the rules are still as that time stamp 
                                    -   would they return this result
            -   initiate_ballotbox(list_of_regions)  
                -   initiates ballotbox
                    -   multiple   instances depending on the region
                    -   makes later easier to do statistics
            -   