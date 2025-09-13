# Code-Tidy 🧹

> Find your giant functions and nested loops before they find you

A simple Python tool that spots the obvious code smells so you don't have to hunt through dozens of files looking for them.

```bash
>>> code-tidy scan .
Found 12 functions over 100 lines across 6 files:
  src/data_processor.py:45 - process_raw_data() (156 lines)
  src/api_handler.py:23 - handle_request() (134 lines)
⚠ Deep nesting detected:
  src/api_handler.py:47 'calculate_tax' (4 levels deep)
```

## What it does

- Finds functions that are way too long (100+ lines)
- Spots deeply nested loops (3+ levels) 
- Points you to the worst offenders first
- Suggests basic refactoring ideas

## What it doesn't do

- Change your code without asking
- Get fancy with subjective "code smells" 
- Slow you down with analysis paralysis

## Status

🚧 **Work in Progress** 🚧

This scratches my own itch from last semester when I spent hours manually hunting through files for refactoring targets. Figured others might want this too.

## Want to help build it?

Drop me a line: **24f2006078@ds.study.iitm.ac.in**

Looking for folks who've also been frustrated by manual code auditing and want to build something actually useful.

## License

GPL v3 - Free forever, contributions stay open source.

---

*"Why didn't someone build this already?"* - Me, after scanning 47 Python files by hand
