# Week 3 Content Summary

## Chapter 3: Program Inspections, Walkthroughs, and Reviews

### Key Ideas

Chapter 3 focuses on human-based testing techniques that help detect software defects before or alongside machine execution. The chapter argues that code should not be tested only by running it on a computer. Careful human review often reveals logic errors, interface mismatches, control-flow mistakes, and missing functionality that automated execution alone may miss.

The central idea is that structured review methods are more effective than informal checking. Inspections, walkthroughs, desk checking, and peer ratings all involve reading and evaluating code, but they differ in discipline, collaboration, and purpose.

### Common Error Areas in Inspections

The chapter provides inspection checklists that help reviewers search for defects systematically. Major categories include:

- Data reference errors, such as using uninitialized variables or out-of-bounds subscripts.
- Data declaration errors, such as wrong types, lengths, storage classes, or unclear default attributes.
- Computation errors, such as overflow, division by zero, incorrect operator precedence, or invalid mixed-type calculations.
- Comparison errors, such as incorrect Boolean expressions or invalid comparisons between inconsistent values.
- Control-flow errors, such as nonterminating loops, off-by-one mistakes, unmatched loop boundaries, or incomplete decision logic.
- Interface errors, such as mismatched parameters, incorrect argument order, altered input-only arguments, or inconsistent global-variable definitions.
- Input/output errors, such as unopened files, incorrect file attributes, bad format specifications, and failure to handle end-of-file or I/O exceptions.
- Other checks, such as compiler warnings, unused variables, missing functions, and weak input validation.

### Walkthroughs

A walkthrough is a structured group review in which participants mentally execute the program using a few simple test cases. Team members effectively “play computer” and trace program behavior step by step. The goal is not to run a large number of tests, but to expose flaws in reasoning, logic, and assumptions.

Walkthrough teams usually include three to five people, including the programmer, a moderator-like leader, a secretary to record errors, and a tester who brings paper test cases. The discussion and questioning process often reveals more defects than the test cases themselves. The chapter stresses that criticism should be directed at the code, not the programmer.

### Desk Checking

Desk checking is a one-person review process in which someone reads code, applies an error checklist, and may mentally trace test data through the program. The chapter presents desk checking as better than doing nothing, but generally less effective than inspections or walkthroughs.

Its weakness is that it is usually informal and undisciplined. It also conflicts with the principle that people are not very effective at testing their own work. Group review methods are stronger because they add multiple perspectives and a useful level of peer challenge.

### Peer Ratings

Peer rating is different from the other review methods because its main purpose is not defect detection. Instead, it is used for self-evaluation and professional growth. Programmers anonymously review one another’s code and score it on qualities such as clarity, maintainability, extensibility, and overall design quality.

Participants review several anonymous programs and answer questions about readability, design visibility, ease of modification, and professional quality. The results help programmers compare their work with that of peers and better understand their strengths and weaknesses.

### Important Takeaways

- Human review is an important part of software testing.
- Structured review methods are more effective than informal checking.
- Inspections use checklists to detect common error patterns systematically.
- Walkthroughs rely on group discussion and mental execution of simple test cases.
- Desk checking is limited because self-review is less effective than team-based review.
- Peer ratings improve programmer self-assessment even though they are not primarily for finding defects.

### Short Summary

Chapter 3 argues that effective software testing includes human-centered review techniques, not just machine execution. Code inspections, walkthroughs, desk checking, and peer ratings each contribute to software quality in different ways, but structured team-based reviews are presented as the most valuable for uncovering defects and improving development practices.


