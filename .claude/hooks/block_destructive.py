"""PreToolUse hook: block shell commands that could destroy or bulk-modify data.

Enforces the "Data Safety" section of CLAUDE.md for the Bash and PowerShell tools.
Reads the hook payload from stdin and, on a match, prints a JSON deny decision.
It is a backstop, not a guarantee: SQL run from inside compiled code or a script
file the command merely references is not visible here.

Add project-specific patterns (for example endpoints that wipe a table) to
PROJECT_RULES at the bottom of the rule list.
"""

import json
import re
import sys

FLAGS = re.IGNORECASE | re.DOTALL

RULES = [
    # SQL statements (match anywhere in the command text, including inline -Q / -Query / -c strings)
    (r"\bDROP\s+(TABLE|DATABASE|SCHEMA|VIEW|PROC|PROCEDURE|FUNCTION|INDEX|TRIGGER|LOGIN|USER|SYNONYM|TYPE|COLLECTION)\b", "SQL DROP"),
    (r"\bTRUNCATE\s+TABLE\b", "SQL TRUNCATE"),
    (r"\bDELETE\s+(TOP\s*\([^)]*\)\s*)?(FROM\s+\S|\[?\w+\]?\.)", "SQL DELETE"),
    (r"\bUPDATE\s+(TOP\s*\([^)]*\)\s*)?\S+\s+SET\b", "SQL UPDATE"),
    (r"\bMERGE\s+(INTO\s+)?\S+.*?\bUSING\b", "SQL MERGE"),
    (r"\bALTER\s+TABLE\b.*?\bDROP\b", "SQL ALTER TABLE ... DROP"),
    (r"\bRESTORE\s+(DATABASE|LOG)\b", "SQL RESTORE"),
    (r"\bsp_detach_db\b|\bsp_MSforeachtable\b|\bxp_cmdshell\b", "dangerous system procedure"),
    # Database clients running a script file the hook cannot inspect, and whole-database drops
    (r"\bsqlcmd\b.*?\s-i\s", "sqlcmd running an input file"),
    (r"\bInvoke-Sqlcmd\b.*?-InputFile\b", "Invoke-Sqlcmd running an input file"),
    (r"\bpsql\b.*?\s(-f|--file)\s", "psql running an input file"),
    (r"\bbcp\b\s+\S+\s+in\b", "bcp bulk import"),
    (r"\bdropdb\b|\bmysqladmin\b.*?\bdrop\b|\bdropDatabase\s*\(", "database drop"),
    # Schema and migration tooling
    (r"\bdotnet\s+ef\s+database\s+(drop|update)\b", "EF Core database drop/update"),
    (r"\bdotnet\s+ef\s+migrations\s+remove\b", "EF Core migration removal"),
    (r"\bprisma\s+migrate\s+reset\b|\bprisma\s+db\s+push\b.*?--(force-reset|accept-data-loss)\b", "Prisma reset / destructive push"),
    (r"\bsequelize(-cli)?\s+db:(drop|migrate:undo)", "Sequelize drop / undo migration"),
    (r"\bknex\s+migrate:(rollback|down)\b", "Knex migration rollback"),
    (r"\balembic\s+downgrade\b", "Alembic downgrade"),
    (r"\bmanage\.py\s+(flush|sqlflush|reset_db)\b|\bmanage\.py\s+migrate\s+\S+\s+zero\b", "Django flush / migrate to zero"),
    # HTTP requests that delete
    (r"(-X\s*|--request\s+)DELETE\b|-Method\s+['\"]?Delete\b", "HTTP DELETE request"),
    # Cloud resource deletion
    (r"\baz\s+.*?\bdelete\b", "Azure CLI delete"),
    (r"\bRemove-Az\w*", "Azure PowerShell Remove-Az*"),
    (r"\baws\s+.*?\b(delete-\w+|rb|terminate-instances)\b", "AWS CLI delete"),
    (r"\bgcloud\s+.*?\bdelete\b", "gcloud delete"),
    (r"\bterraform\s+destroy\b", "terraform destroy"),
    # Git history rewrites
    (r"\bgit\s+push\b.*?(\s--force\b|\s--force-with-lease\b|\s-f\b|\s\+\S)", "git force push"),
    (r"\bgit\s+reset\b.*?--hard\b", "git reset --hard"),
]

# Project-specific rules: endpoints, scripts or jobs that wipe or overwrite data in this repo.
# Example: (r"/api/Calendar/(reset|update)\b", "calendar reset/update endpoint"),
PROJECT_RULES = [
]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not command:
        return 0

    for pattern, label in RULES + PROJECT_RULES:
        if re.search(pattern, command, FLAGS):
            reason = (
                f"Blocked by the Data Safety hook ({label}). CLAUDE.md forbids Claude from running "
                "destructive or bulk-modifying operations. Write the script or command to a file, "
                "explain exactly what it affects, and ask the human to run it themselves."
            )
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }))
            return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
