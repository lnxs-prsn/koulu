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

