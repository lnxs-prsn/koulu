Here's a comprehensive **Domain Modeling Template** that separates analysis, design, and implementation concerns:

# DOMAIN MODELING TEMPLATE
**Project:** [Project Name]
**Version:** [Version]
**Date:** [Date]

---

## 1. BUSINESS CONTEXT
**Vision Statement:** [1-2 sentence vision]
**Core Problem:** [What problem are we solving?]
**Business Value:** [Why does this matter?]
**Stakeholders:** [Who cares about this system?]
- [Role 1]: [Their concerns]
- [Role 2]: [Their concerns]

## 2. DOMAIN OVERVIEW
**Primary Domain:** [e.g., E-commerce, Healthcare, Banking]
**Subdomains:**
1. **[Core]**: [Most valuable, complex, business-differentiating]
2. **[Supporting]**: [Supports core but not differentiating]
3. **[Generic]**: [Common, can be bought/outsourced]

**Domain Experts:** [Key people who understand the domain]
- [Name/Role]: [Their expertise]

## 3. BOUNDED CONTEXTS
| Context Name | Responsibility | Key Relationships |
|-------------|---------------|-------------------|
| [Context 1] | [What it does] | [Related contexts] |
| [Context 2] | [What it does] | [Related contexts] |

**Context Map:**
```
[Context A] ---(Partnership)---> [Context B]
[Context B] ---(Customer/Supplier)---> [Context C]
[Context D] ---(Conformist)---> [Context E]
```

## 4. UBIQUITOUS LANGUAGE
**Glossary of Key Terms:**
| Term | Definition | Context |
|------|------------|---------|
| [Term 1] | [Clear definition] | [Which context] |
| [Term 2] | [Clear definition] | [Which context] |

**Business Rules:**
- [Rule 1: e.g., "Order cannot be shipped without payment"]
- [Rule 2: e.g., "User must be verified to perform transaction"]

## 5. CORE DOMAIN MODEL
### Context: [Context Name]
**Entities (have identity):**
```
[Entity Name]
- Identity: [How it's identified]
- Attributes: [key attributes]
- Invariants: [business rules that must always be true]
- Responsibilities: [what it can do]
```

**Value Objects (immutable, no identity):**
```
[Value Object Name]
- Attributes: [all attributes]
- Invariants: [validation rules]
- Operations: [what it can calculate/derive]
```

**Aggregates (consistency boundaries):**
```
[Aggregate Name]
- Root Entity: [Root entity]
- Child Entities: [Children]
- Value Objects: [VOs]
- Invariants: [consistency rules across the aggregate]
- Factory Methods: [how it's created]
```

**Domain Services (stateless operations):**
```
[Service Name]
- Purpose: [what it does]
- Parameters: [what it needs]
- Returns: [what it produces]
```

**Repositories (persistence abstraction):**
```
[Repository Name]
- Returns: [What type of aggregate/entity]
- Key Methods: [save, findById, findByCriteria]
```

**Domain Events (something happened):**
```
[Event Name]
- Triggered when: [what causes it]
- Carries: [what data]
- Consumers: [who cares about it]
```

## 6. USE CASES / USER STORIES
### Actor: [Actor Role]
**Goal:** [What they want to achieve]
**Preconditions:** [What must be true before]
**Main Flow:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Postconditions:** [What must be true after]
**Business Rules Applied:**
- [Rule 1]
- [Rule 2]

## 7. INVARIANTS & VALIDATION RULES
**Aggregate-Level Invariants:**
- [Aggregate]: [Rule that must be true within the aggregate]

**Cross-Aggregate Consistency Rules:**
- [Rule that spans multiple aggregates, eventual consistency]

## 8. SUPPLEMENTARY MODELS
**State Diagrams:**
```
[Entity] States: [State1] → [State2] → [State3]
Transitions:
- [Event1] causes [State1] → [State2]
- [Event2] causes [State2] → [State3]
```

**Process Flows:**
```
[Process Name]:
[Step1] → [Step2] → [Decision] → [Step3a/Step3b]
```

## 9. INTEGRATION PATTERNS
**Between Bounded Contexts:**
- [Context A] → [Context B]: [Pattern: e.g., REST API, Event, Shared Kernel]
- [Context B] → [Context C]: [Pattern: e.g., Anti-corruption Layer]

**External Systems:**
- [System Name]: [Integration approach]

## 10. EVOLUTION & VARIABILITY
**Anticipated Changes:**
- [Change 1]: [How model accommodates it]
- [Change 2]: [How model accommodates it]

**Variation Points:**
- [Where different implementations might be needed]
- [Configuration points]

## 11. NON-FUNCTIONAL CONSIDERATIONS
**Performance:**
- [Critical paths]
- [Expected volumes]

**Consistency Requirements:**
- [Where strong consistency is needed]
- [Where eventual consistency is acceptable]

## 12. OPEN QUESTIONS & RISKS
**Unclear Areas:**
- [Question 1]
- [Question 2]

**Risks:**
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

---

## QUICK-START MINIMAL TEMPLATE
For smaller projects:

```markdown
# DOMAIN MODEL: [Project Name]

## CORE DOMAIN
[2-3 sentence description]

## KEY CONCEPTS
| Concept | Definition | Type (Entity/VO/Service) |
|---------|------------|--------------------------|
| [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] |

## AGGREGATES
### [Aggregate Name]
**Root:** [Root Entity]
**Purpose:** [What it protects]
**Rules:**
- [Invariant 1]
- [Invariant 2]

## USE CASES
### UC1: [Use Case Name]
**Actor:** [Who]
**Steps:**
1. [Step]
2. [Step]
3. [Step]

## GLOSSARY
- [Term]: [Definition]
```

---

## TEMPLATE USAGE GUIDELINES

### When to Use Which Sections:
- **Startups/New Projects:** Use Quick-Start template
- **Medium Complexity:** Use Sections 1-6, 8
- **Enterprise/Legacy Integration:** Use all sections

### Fill Order (Recommended):
1. **Business Context & Domain Overview** (Understand the why)
2. **Ubiquitous Language** (Establish common terms)
3. **Bounded Contexts** (Divide the problem space)
4. **Core Domain Model** (Model within each context)
5. **Use Cases** (Validate the model)
6. **Integration Patterns** (Connect contexts)

### Common Pitfalls to Avoid:
1. **Don't** model implementation details (databases, frameworks)
2. **Don't** create "God" objects/aggregates
3. **Do** validate with domain experts
4. **Do** iterate - domain models evolve
5. **Do** separate what changes frequently from what's stable

### Validation Questions:
- [ ] Can a domain expert understand this model?
- [ ] Does it reflect the real business, not just the software?
- [ ] Are bounded contexts cohesive and loosely coupled?
- [ ] Are aggregates the right size (not too big, not too small)?
- [ ] Is the ubiquitous language consistent throughout?

---

## EXAMPLE: E-COMMERCE ORDER PROCESSING (Partial)

```markdown
## 5. CORE DOMAIN MODEL
### Context: Order Management

**Aggregate: Order**
```
Root Entity: Order
- Identity: OrderId (UUID)
- Attributes: customerId, status, totalAmount
- Invariants:
  - Order must have at least one item
  - Total must equal sum of item prices
  - Cannot modify after shipment
- Responsibilities:
  - addItem(productId, quantity, price)
  - calculateTotal()
  - confirm()
  - ship()

Child Entities:
  - OrderItem (productId, quantity, unitPrice)

Value Objects:
  - Money (amount, currency)
  - Address (street, city, zip)

Factory Method:
  - Order.create(customerId, items)
```

**Domain Service: OrderValidator**
```
Purpose: Validate order against business rules
Parameters: Order, InventoryService
Returns: ValidationResult
Rules:
  - All items must be in stock
  - Customer must not be blocked
  - Order total < credit limit
```

**Domain Event: OrderConfirmed**
```
Triggered when: Order.confirm() succeeds
Carries: orderId, customerId, totalAmount, items
Consumers: PaymentContext, ShippingContext, NotificationContext
```
```

This template gives you structure while remaining flexible. The key is to **start simple** and **add detail only as needed** for your specific domain complexity.