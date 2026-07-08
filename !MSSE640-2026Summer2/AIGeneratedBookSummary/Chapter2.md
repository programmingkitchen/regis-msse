# Week 2 Content Summary

## Chapter 2: The Psychology and Economics of Software Testing

### Key Ideas

Chapter 2 explains why exhaustive testing is not a practical way to prove software correctness. Even a small program can have an enormous number of execution paths, making it unrealistic to test every possible path or input. The chapter argues that both exhaustive path testing and exhaustive input testing are infeasible in real systems.

The text also shows that even if every path in a program were executed, the software could still contain defects. A program may fail because it does not match the specification, because necessary logic paths are missing, or because errors depend on specific data values rather than control flow alone.

Because of these limits, software testing must be approached as a disciplined, thoughtful activity rather than an attempt to prove perfection. The chapter emphasizes that testing is as much about psychology and judgment as it is about technique.

### Why Exhaustive Testing Fails

- Real programs have too many possible paths to test completely.
- Testing every path still does not prove that the program satisfies its requirements.
- Missing logic cannot be discovered by only testing existing paths.
- Some defects are data-sensitive and only appear with certain values.

### The 10 Software Testing Principles

1. Every test case must define the expected result before execution.
2. Programmers should avoid testing their own programs when possible.
3. A programming organization should not be the only group testing its own software.
4. Every test result should be inspected carefully.
5. Test cases should include invalid and unexpected inputs, not just valid ones.
6. Testing must check both whether the program does what it should and whether it does what it should not do.
7. Test cases should be saved and reused unless the software itself is disposable.
8. Testing should be planned with the expectation that errors will be found.
9. Sections with many discovered errors are likely to contain even more defects.
10. Testing is a creative and intellectually demanding task.

### Important Takeaways

- Testing is intended to find errors, not to prove the absence of them.
- Good test cases have a strong chance of revealing previously unknown defects.
- Effective testing requires clearly defined inputs and expected outputs.
- Independent testing is usually more reliable than self-testing.
- Regression testing is important because saved test cases help detect failures introduced by later changes.

### Short Summary

Chapter 2 presents testing as a practical search for defects rather than a guarantee of correctness. It argues that exhaustive testing is impossible in meaningful software systems, so testers must rely on sound principles, independent judgment, carefully designed test cases, and close inspection of results to improve software quality.