

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
            -   coordinates other objects
                -   stores hashes of the user_id
                    -   hashes must have salt to ensure only that 
                    -   to ensure that every user_id gets one voter object
                -   calls validate and validates user_data
                -   calls anonymization and anonymizes the user_data turns it to token
                -   calls voter and creates instance
                -   calls vote and passes the user vote to it
                -   calls ballotbox and adds to it vote
                -   calls method in the validate to if election rules are maintaned
                -   
        -   voter
            -   is called by electionsystem
            -   receives token
            -   select_option()
        -   vote
            -   is called by electionsystem
            -   immutable
            -   gets passed voters vote through electionsystem
        -   ballotbox
            -   is called by electionsystem
            -   gets passed vote through the election system
            -   stores dictionary of options and list of votes
        -   electioncommision
            -   stores and electioncommitions report
            -   requests from electionsystem reports
        -   observer
            -   stores an observation report
            -   requests from electionsystem reports
        -   validation
            -   is called by electionsystem
            -   validates multiple objects
                -   validate_voter, validate_anonymity, validate_rules, validate_ballotbox, 
                -   stores array of rules and regulations for the election
        -   anonymization
            -   is called by the electionsystem
            -   anonymize_data()
                -   this anonymises user_data before creating voter instance