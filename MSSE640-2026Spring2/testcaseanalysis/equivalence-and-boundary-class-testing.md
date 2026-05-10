# Equivalence Class Testing and Boundary Class Testing

## Overview

Equivalence class testing and boundary class testing are black-box test design techniques. They help reduce the total number of test cases while still covering important behavior in an input domain.

- Equivalence class testing groups inputs that should be handled the same way.
- Boundary class testing focuses on values at the edges of those groups, where defects are more likely.

These techniques are most useful when a system accepts inputs with clear rules, ranges, formats, or categories.

## Equivalence Class Testing

### What It Is

Equivalence class testing, often called equivalence partitioning, divides possible inputs into classes that the software should treat as equivalent. Instead of testing every value in a class, you select one representative value from each class.

For example, if an input field accepts ages from 18 to 65, you can divide the input space into these classes:

- Invalid class: values less than 18
- Valid class: values from 18 to 65
- Invalid class: values greater than 65

The assumption is that if one value from a class works or fails correctly, the other values in the same class are likely to behave the same way.

### When To Use It

Use equivalence class testing when:

- Inputs fall into clear categories or ranges
- Testing every input would be impractical
- You want a compact set of representative tests
- Requirements define valid and invalid groups clearly

### Example

Assume a function accepts a student score from 0 to 100.

Equivalence classes:

- Invalid: score less than 0
- Valid: score from 0 to 100
- Invalid: score greater than 100

Representative tests might be:

- `-5` for the invalid low class
- `75` for the valid class
- `120` for the invalid high class

## Boundary Class Testing

### What It Is

Boundary class testing, commonly called boundary value analysis, targets the edges of input classes. Errors often occur at boundaries because developers make mistakes with comparison operators such as `<`, `<=`, `>`, and `>=`.

Using the same score range of 0 to 100, the most interesting values are usually:

- Just below the boundary
- At the boundary
- Just above the boundary

That gives boundary-focused tests such as:

- `-1`, `0`, `1`
- `99`, `100`, `101`

### When To Use It

Use boundary class testing when:

- Inputs have minimum or maximum limits
- The logic depends on thresholds or cutoffs
- You want to catch off-by-one errors
- Rules are based on ranges, sizes, counts, or dates

### Example

For a password length requirement of 8 to 20 characters, useful boundary tests include:

- `7` characters: invalid
- `8` characters: valid
- `9` characters: valid
- `19` characters: valid
- `20` characters: valid
- `21` characters: invalid

## Code Snippet Example

The example below shows a Python function that validates an exam score and a small test set that applies both techniques.

```python
def validate_score(score: int) -> str:
    if score < 0 or score > 100:
        return "invalid"
    return "valid"


# Equivalence class tests
assert validate_score(-5) == "invalid"   # representative of scores below 0
assert validate_score(50) == "valid"     # representative of scores from 0 to 100
assert validate_score(120) == "invalid"  # representative of scores above 100

# Boundary class tests
assert validate_score(-1) == "invalid"
assert validate_score(0) == "valid"
assert validate_score(1) == "valid"
assert validate_score(99) == "valid"
assert validate_score(100) == "valid"
assert validate_score(101) == "invalid"
```

## Comparison

### Equivalence Class Testing Focus

- Selects one or a few representative values per class
- Reduces the number of tests significantly
- Good for broad input coverage

### Boundary Class Testing Focus

- Selects values at and around class edges
- Targets error-prone areas directly
- Good for finding threshold and off-by-one defects

## Limitations

### Limitations of Equivalence Class Testing

- It may miss defects that occur only at edge values
- It assumes all values in a class behave the same way
- It is less effective when internal state or workflow matters more than simple input categories

### Limitations of Boundary Class Testing

- It focuses heavily on edges and may overlook non-boundary combinations
- It is less useful when inputs do not have clear numeric, size, or ordered limits
- It does not replace broader scenario, workflow, or integration testing

## When Not To Use Them Alone

Do not rely on these techniques alone when:

- Business rules depend on combinations of multiple fields
- System behavior depends on sequence, timing, or state transitions
- Testing involves user workflows rather than isolated inputs
- Risk is tied to integrations, security, concurrency, or performance

In those cases, combine them with other techniques such as decision table testing, state transition testing, use case testing, integration testing, and exploratory testing.

## Practical Guidance

Use equivalence class testing first to identify the main valid and invalid groups. Then apply boundary class testing to the edges of the most important groups. Together, they provide efficient coverage for input validation and business rule checks without requiring exhaustive testing.