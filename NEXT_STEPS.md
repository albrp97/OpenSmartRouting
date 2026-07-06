# OpenSmartRouting Next Steps

> Ordered list of what to do after the runtime baseline is in place.

This file is the immediate follow-up list.

It does **not** mean these steps should all be executed right now. It means the repository is now ready for them.

## Current state

The repo now has:

- root instructions
- Copilot instructions
- path-scoped rules
- local runtime overrides
- reusable workflow prompts
- reusable skill entrypoints
- review, security, hotspot, user-testing, pipeline, and eval workflow scaffolding

The project does **not** yet have:

- planning artifacts
- research documents
- experiments
- source code
- tests
- CI setup

## What to do next, in order

1. **Run the planning baseline**
   - repository map
   - project objective
   - problem / users / success
   - scope
   - capability map
   - epics
   - phases
   - tickets

2. **Research the free stack**
   - map data
   - geocoding
   - routing engines
   - optimization libraries
   - Python integration
   - later Android path

3. **Design the experiment harness**
   - sample datasets
   - route-quality metrics
   - comparison against the paid app
   - algorithm comparison method

4. **Decide the Python MVP boundary**
   - CLI input format
   - route output format
   - validation method
   - what is in scope for the first useful version

5. **Set up the delivery workflow**
   - branch and PR conventions
   - local quality commands
   - initial validation flow
   - CI only when the repo has enough code to justify it

6. **Start the first implementation ticket**
   - only after the planning and MVP boundary are clear

## Recommended first concrete actions

If the next session starts now, the best immediate sequence is:

1. run the objective and problem/users/success workflows
2. run the free-stack research workflow
3. define the experiment plan
4. only then move toward MVP scoping
