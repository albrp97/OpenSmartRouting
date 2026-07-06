# OpenSmartRouting Hotspot Review Guide

> Lightweight hotspot review guidance for a routing and experiment-heavy repository.

## Purpose

Use hotspot review to decide where extra scrutiny is needed.

## High-risk areas in this repo

- route-computation core
- optimization logic
- geocoding normalization
- input parsing
- export generation

## Risk signals

1. large files
2. files edited repeatedly in short time windows
3. files mixing routing, parsing, and output concerns
4. files where a small bug can invalidate route quality

## Output format

For each hotspot, record:

- file path
- dominant risk signal
- why it matters
- what extra review action is needed
