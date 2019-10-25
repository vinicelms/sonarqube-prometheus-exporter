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
            "new_bugs",
            "reliability_rating",
            "new_reliability_rating",
            "reliability_remediation_effort",
            "new_reliability_remediation_effort"
        ]
    },
    {
        "domain" : "Security",
        "keys" : [
            "new_security_hotspots",
            "new_vulnerabilities",
            "security_hotspots",
            "security_rating",
            "new_security_rating",
            "security_remediation_effort",
            "new_security_remediation_effort",
            "security_review_rating"
        ]
    },
    {
        "domain" : "Maintainability",
        "keys" : [
            "new_technical_debt",
            "code_smells",
            "development_cost",
            "effort_to_reach_maintainability_rating_a",
            "Maintainability - sqale_rating"
            "new_maintainability_rating",
            "new_code_smells"
            "sqale_index",
            "sqale_debt_ratio",
            "new_sqale_debt_ratio",
            # "new_development_cost"
        ]
    },
    {
        "domain" : "Duplications",
        "keys" : [
            "duplicated_blocks",
            "new_duplicated_blocks",
            "duplicated_files",
            "duplicated_lines",
            "duplicated_lines_density",
            "new_duplicated_lines",
            "new_duplicated_lines_density",
            "duplications_data"
        ]
    },
    {
        "domain" : "Coverage",
        "keys" : [
            "branch_coverage",
            "new_branch_coverage",
            "conditions_to_cover",
            "new_conditions_to_cover",
            "coverage",
            "new_coverage",
            "executable_lines_data",
            "line_coverage",
            "new_line_coverage",
            "lines_to_cover",
            "new_lines_to_cover",
            "skipped_tests",
            "uncovered_conditions"
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
            "ncloc_language_distribution",
            "ncloc_data",
            "new_lines",
            "projects",
            "statements"
        ]
    }
]