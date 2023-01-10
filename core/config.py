import os

class Config:

    def __init__(self):
        self._sonar_url = os.environ['SONAR_URL']
        self._sonar_user = os.environ['SONAR_USER']
        self._sonar_password = os.environ['SONAR_PASSWORD']

    @property
    def sonar_url(self):
        return self._sonar_url

    @property
    def sonar_user(self):
        return self._sonar_user

    @property
    def sonar_password(self):
        return self._sonar_password

    @property
    def supported_keys(self):
        return SUPPORTED_KEYS

SUPPORTED_KEYS = [
    {
        "domain" : "Reliability",
        "keys" : [
            "bugs",
            "reliability_rating",
            "reliability_remediation_effort"
        ]
    },
    {
        "domain": "SecurityReview",
        "keys": [
            "security_hotspots",
        ]
    },
    {
        "domain" : "Security",
        "keys" : [
            "security_rating",
            "security_remediation_effort",
            "security_review_rating",
            "vulnerabilities"
        ]
    },
    {
        "domain" : "Maintainability",
        "keys" : [
            "code_smells",
            "development_cost",
            "effort_to_reach_maintainability_rating_a",
            "sqale_rating",
            "sqale_index",
            "sqale_debt_ratio"
        ]
    },
    {
        "domain" : "Duplications",
        "keys" : [
            "duplicated_blocks",
            "duplicated_files",
            "duplicated_lines",
            "duplicated_lines_density",
            "duplications_data"
        ]
    },
    {
        "domain" : "Coverage",
        "keys" : [
            "branch_coverage",
            "conditions_to_cover",
            "executable_lines_data",
            "line_coverage",
            "lines_to_cover",
            "skipped_tests",
            "uncovered_conditions",
            "test_failures,tests",
            "test_errors",
            "skipped_tests",
            "test_success_density",
            "test_execution_time"
        ]
    },
    {
        "domain" : "Size",
        "keys" : [
            "classes",
            "comment_lines",
            "comment_lines_data",
            "comment_lines_density",
            "directories",
            "files",
            "functions",
            "generated_lines",
            "generated_ncloc",
            "lines",
            "ncloc",
            "ncloc_data",
            "projects",
            "statements"
        ]
    },
    {
        "domain" : "Issues",
        "keys" : [
            "violations",
            "open_issues",
            "reopened_issues",
            "confirmed_issues",
            "false_positive_issues",
            "wont_fix_issues"
        ]
    }
]