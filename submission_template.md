# AI Code Review Assignment (Python)

## Candidate
- Name: Semhal Estifanos
- Approximate time spent: 40-60 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Divides by `len(orders)` instead of counting only valid non-cancelled orders.
- Non-numeric or missing amounts can raise exceptions.
- Empty list or all cancelled orders → ZeroDivisionError.

### Edge cases & risks
- Orders missing `"amount"` or `"status"` keys.
- Orders that are not dictionaries.
- Mixed types in `"amount"` field (string, int, None).

### Code quality / design issues
- No input validation.
- Function not robust to malformed data.
- Poor error signaling (may return misleading averages).

## 2) Proposed Fixes / Improvements
### Summary of changes
- Validated `orders` is iterable; raises `TypeError` otherwise.
- Skipped non-dict entries.
- Skipped orders with `"status": "cancelled"`.
- Converted `"amount"` to float safely; skipped if conversion fails.
- Denominator = count of valid non-cancelled orders.
- Returns `None` if no valid data exists.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
- Empty list → returns `None`.
- All cancelled orders → returns `None`.
- Mixed valid/invalid orders → only averages valid numeric, non-cancelled orders.
- Non-dict orders → safely ignored.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Misleading denominator description.
- Does not mention skipping invalid amounts or non-dict orders.
- Ignores potential ZeroDivisionError.

### Rewritten explanation
- Calculates average of non-cancelled orders only.
- Skips non-dict entries and invalid/missing amounts.
- Returns `None` if no valid orders exist.

## 4) Final Judgment
- Decision: Approve
- Justification: Critical issues fixed; function now robust and safe.
- Confidence & unknowns: High confidence; all edge cases handled.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Original counts any string with `"@"` → many false positives.
- Non-string entries cause `TypeError`.
- Accepts invalid domains or spaces.

### Edge cases & risks
- Empty list → must return 0.
- Mixed types in list (None, numbers, dicts) → must skip.
- Emails missing local part or domain → should not count.

### Code quality / design issues
- No clear validation rules.
- Function not defensive against malformed input.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Validated `emails` is iterable; raises `TypeError` otherwise.
- Skipped non-string items.
- Used regex to check:
  - Non-empty local part
  - Single `"@"` symbol
  - Domain contains at least one dot
  - No spaces
- Counted only valid matches.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations
- Empty list → returns 0.
- Invalid emails without `"@"` → ignored.
- Emails with spaces or bad domains → ignored.
- Valid emails with subdomains or tags → counted correctly.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Too simplistic; original misclassifies invalid emails.
- No mention of type checks or skipping non-strings.

### Rewritten explanation
- Iterates over input, skipping non-strings.
- Uses regex to check basic email validity.
- Returns count of strings matching the pattern.

## 4) Final Judgment
- Decision: Approve
- Justification: Over-permissiveness corrected; robust against mixed input.
- Confidence & unknowns: High confidence; regex sufficient for assignment.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by `len(values)` including invalid/None → wrong average.
- Non-numeric strings cause `ValueError`.
- Includes NaN → pollutes average.
- Empty list → ZeroDivisionError.

### Edge cases & risks
- Mixed numeric types (int, float, string)
- NaN values must be ignored.
- No valid data → should return `None`.

### Code quality / design issues
- No input validation.
- Function not robust to real-world measurement lists.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Validated `values` is iterable; raises `TypeError` otherwise.
- Skipped `None` values.
- Converted to float safely; skipped if fails.
- Ignored NaN values.
- Sum valid numbers; divide by count of valid entries.
- Returns `None` if no valid numeric values exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
- Mixed types → safely convert to float if possible.
- NaN or None → skipped.
- Empty list or all invalid → returns `None`.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation
- Does not mention NaN handling.
- Ignores invalid strings that may raise exceptions.

### Rewritten explanation
- Calculates mean of valid numeric entries.
- Skips None, non-convertible strings, and NaN values.
- Returns `None` if no valid data exists.

## 4) Final Judgment
- Decision: Approve
- Justification: Function now handles all edge cases and invalid inputs safely.
- Confidence & unknowns: High confidence; robust for real measurement lists.
