# Token 1 from GitHub
TOKEN = "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"

# Token 2 from GitHub
TOKEN1 = "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"

# Token 3 from GitHub
TOKEN2 = "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"

# Token 4 from GitHub
TOKEN4 = "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"

# Token 5 from GitHub
TOKEN5 = "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"

# Token 6 from GitHub
TOKEN6 = "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"


# Token 1 from SonarQube
TOKEN3 = "squ_a8212cd16276f5ccf4c8eb046f154c9f8a79cf05"

REPOSCHARACTERISTICS = [
    "index",
    "repo_name",
    "ncloc",
    "code_smells",
    "any-type_count",
    "cognitive_complexity",
    "framework",
    "bug_issues_count",
    "bug-fix_commits_count",
    "commits_count",
]

METRICS = [
    "index",
    "repo_name",
    "code-smells_ncloc",
    "bug-fix-commits_ratio",
    "avg_bug-issue_time",
    "cognitive-complexity_ncloc",
]

CALCULATEDVALS = ["", "react", "angular", "vue", "others"]

ESLINTFILES = ["./eslint/.eslintignore", "./eslint/.eslintrc.js"]

URLCREATEPROJECT = "http://localhost:9000/api/projects/create"
URLGENERATETOKEN = "http://localhost:9000/api/user_tokens/generate"
URLISSUES = "http://localhost:9000/api/issues/search"
URLCOMPONENTREE = "http://localhost:9000/api/measures/component_tree"

ESLINTPATHS = [
    ".eslintrc",
    ".eslintrc.json",
    ".eslintrc.js",
    ".eslintignore",
    ".eslintrc.yml",
    ".eslintrc.yaml",
]
