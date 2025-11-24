# backend/epr_calculations.py
# Simple EPR calculations for BookShelf-EPR project

# Versions and their stability
versions = {
    "v0.1": "unstable",
    "v0.2": "minor fixes",
    "v1.0": "stable"
}

# Count total versions
total_versions = len(versions)
print(f"Total versions: {total_versions}")

# List stable versions
stable_versions = [v for v, s in versions.items() if s == "stable"]
print(f"Stable versions: {stable_versions}")

# Bugs found in each version
bugs = {
    "v0.1": 5,
    "v0.2": 2,
    "v1.0": 1
}

# Total bugs
total_bugs = sum(bugs.values())
print(f"Total bugs found: {total_bugs}")

# Percentage of bugs fixed (compared to first version)
fixed_bugs = total_bugs - bugs["v1.0"]
percent_fixed = (fixed_bugs / total_bugs) * 100
print(f"Percent of bugs fixed: {percent_fixed:.1f}%")
