# Week 4 Content Summary

## Chapter 4: Test-Case Design

### Key Ideas

Chapter 4 explains how to design test cases systematically instead of selecting them randomly or relying only on intuition. The chapter emphasizes that no single testing method is sufficient by itself. Strong testing combines black-box and white-box techniques so that test cases cover likely defects, edge conditions, and important logic paths.

The main goal is to create a small but powerful set of test cases that has a high chance of uncovering errors. The chapter shows that disciplined test-case design improves testing efficiency while still revealing specification problems, boundary issues, and unexpected behaviors.

### Cause-Effect Graphing

Cause-effect graphing is presented as a systematic method for generating test cases from combinations of input conditions. It translates the specification into a Boolean-style logic network and then into a decision table. This process helps testers identify meaningful combinations that might be missed through ad hoc selection.

The chapter also notes that cause-effect graphing gives deeper insight into the specification itself. While building the graph, testers may discover ambiguity, incompleteness, or contradictions in the requirements. However, cause-effect graphing alone is not enough because it does not fully address all boundary cases or every useful correctness check.

### Boundary Value Analysis

Boundary value analysis is used to focus on edge conditions, where errors are especially common. The chapter shows that testers should examine limits such as minimum and maximum values, values just below and above limits, and transitions that change system behavior.

Rather than treating boundary analysis as separate from other methods, the chapter recommends blending it into the test cases derived from cause-effect graphing whenever possible. This produces a compact set of tests that still covers both combinations of conditions and critical edge cases.

### Error Guessing

Error guessing is described as an intuitive technique based on experience. Some testers are especially effective because they instinctively anticipate likely defects and design test cases to expose them. Although this method is informal, it is still valuable when used alongside more structured approaches.

Typical error-guessing situations include empty inputs, single-item inputs, repeated values, already sorted data, malformed commands, extra operands, leading zeros, or assumptions the programmer may have made without realizing it. The method helps expose special cases that formal techniques may not highlight directly.

### Recommended Test-Case Strategy

The chapter recommends combining multiple techniques into one practical strategy:

1. Start with cause-effect graphing when the specification includes combinations of input conditions.
2. Apply boundary value analysis to important input and output limits.
3. Identify valid and invalid equivalence classes and add tests if needed.
4. Use error guessing to add experience-based test cases.
5. Review program logic with coverage criteria such as decision, condition, decision/condition, or multiple-condition coverage, and add tests where coverage is missing.

### Important Takeaways

- Good test-case design is deliberate, not random.
- Cause-effect graphing helps generate tests for meaningful combinations of conditions.
- Boundary value analysis is essential because many defects occur at edges and limits.
- Error guessing adds practical value by targeting special cases and likely programmer assumptions.
- Combining several methods produces a more effective test suite than relying on one technique alone.
- Even strong test-case design cannot guarantee that all defects will be found.

### Short Summary

Chapter 4 presents test-case design as a structured process that combines formal methods with practical judgment. Cause-effect graphing, boundary value analysis, equivalence partitioning, logic coverage, and error guessing each contribute different strengths. Together, these techniques help testers build efficient, rigorous test suites that improve the chances of finding important software defects.