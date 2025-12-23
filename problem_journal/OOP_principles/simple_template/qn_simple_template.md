
# OOP DESIGN: [Project Name]

## What’s the point?  

Build objects that **do their job** without needing others to poke inside them.

## Keep it simple  

- **One reason to change** → one job per class  
- **No digging into other objects’ data** → ask them to act, don’t inspect  
- **Need a service? Get it handed to you** → never reach out (no `import` inside logic)

## Your classes  

```

[Name] – [action-focused description]  
  uses: [only what it can’t do itself]  
  actions: [verbs that match real behavior]
```

_Example:_  

```

Thermostat – maintains room temperature  
  uses: Heater, Sensor  
  actions: check_temperature(), turn_on_heater(), decide_if_comfortable()
```

## Guardrail  

**“Never let [X] happen.”**  

_Example: “Never let the thermostat read the heater’s internal state—only tell it to turn on or off.”_

## Test like a builder  

- Swap real helpers with fakes  
- Trigger actions, then observe outcomes  
- If you’re checking private fields, you’ve gone too far

---

This version:

- Uses **different phrasing** (“What’s the point?”, “Guardrail”, “Test like a builder”)  
- Avoids repeating your exact section names  
- Keeps the **essence** (simplicity, behavior, collaboration) but expresses it freshly  
- Stays **project-agnostic** and **beginner-clear**

