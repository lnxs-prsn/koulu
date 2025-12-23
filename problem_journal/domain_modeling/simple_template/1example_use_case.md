# DOMAIN MODEL: Secure Voting System

## CORE DOMAIN

A system where eligible voters can cast exactly one secret ballot per election.

## KEY CONCEPTS

| Concept     | Definition                              | Type        |
|-------------|-----------------------------------------|-------------|
| Voter       | Registered participant with unique ID    | Entity      |
| Election    | Voting period with candidates            | Entity      |
| Vote        | Secret choice for one candidate          | Value Object|

## AGGREGATES

### Election

**Root:** Election  
**Purpose:** Ensure vote integrity and secrecy  
**Rules:**

- A voter can submit only one vote
- Votes cannot reveal voter identity
- Election can be closed (no more votes)

## USE CASES

### UC1: Cast Vote

**Actor:** Voter  
**Steps:**

1. Voter requests to vote in open election
2. System checks eligibility and prior voting
3. Voter selects candidate
4. System records anonymous vote
5. Voter is marked as having voted

## GLOSSARY

- **Eligible voter**: Registered before election start

- **Secret ballot**: No link between vote and voter ID
