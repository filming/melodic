# This script automates the release process.
# It ensures a clean git status, runs the version bump, and pushes to origin.

# Exit immediately if a command exits with a non-zero status.
set -e

# Check if the working directory is clean
if ! git diff-index --quiet HEAD --; then
    echo "Error: Working directory is not clean. Please commit or stash your changes."
    exit 1
fi

# Check if pre-commit is installed (using uv run)
if ! uv run pre-commit --version &> /dev/null; then
    echo "Warning: pre-commit is not installed. Consider running 'uv sync --extra dev && uv run pre-commit install'."
fi

# Check if commitizen is installed (using uv run)
if ! uv run cz version &> /dev/null; then
    echo "Error: commitizen is not installed. Please run 'uv sync --extra dev'."
    exit 1
fi

echo "Starting the release process."

# Run 'cz bump' using uv run. This will:
# 1. Determine the new version number.
# 2. Update pyproject.toml and CHANGELOG.md.
# 3. Create a new commit (e.g., 'chore(release): v1.2.3').
# 4. Create a new git tag (e.g., 'v1.2.3').
# We are intentionally not using --yes to allow for a final review.
uv run cz bump

# Get the current branch name dynamically
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

echo "Pushing commit to '$CURRENT_BRANCH' and pushing tags..."

git push origin "$CURRENT_BRANCH"
git push --tags

echo "Release process complete!"
