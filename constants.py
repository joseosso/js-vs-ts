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
TOKEN3 = ""

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
