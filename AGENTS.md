# AGENTS.md - Gitmoji Commits Skill

This is an AI agent skill following the [Agent Skills format](https://agentskills.io/).

## Repository Structure

```
gitmoji-commits/
  SKILL.md                      # Skill definition with YAML frontmatter
  scripts/
    gitmoji_selector.py         # Python script to suggest gitmojis
  references/
    gitmoji-guide.md            # Complete gitmoji reference and decision tree
```

## Validation

Skills can be validated using the `skills-ref` validator:

```bash
# Install the validator
pip install git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref

# Validate this skill
skills-ref validate .
```

## Code Style Guidelines

### SKILL.md File

**Frontmatter** (required at the top):
```yaml
---
name: gitmoji-commits
description: Create high-quality git commits with semantic gitmoji emojis...
license: MIT
metadata:
  version: "1.0.0"
---
```

- **name**: kebab-case, matches directory name
- **description**: One sentence, explains when to use and what it does
- **license**: MIT
- **metadata.version**: Semantic version

**Content Guidelines**:
- Use clear headings (`#`, `##`, `###`)
- Include code examples in fenced blocks with language tags
- Keep all lines under 100 characters
- Use tables for structured data
- Link to references for detailed information

### File Naming

- **Skill directory**: `gitmoji-commits` (kebab-case)
- **Main file**: `SKILL.md` (uppercase)
- **Scripts directory**: `scripts/` (lowercase)
- **References directory**: `references/` (lowercase)
- **Python scripts**: snake_case (e.g., `gitmoji_selector.py`)

### Writing Style

- Use **imperative mood** for instructions ("Add files", not "You should add files")
- Include **code examples** in fenced blocks with language specification
- Explain **what** and **why**, not just how
- Use **present tense** throughout
- Focus on practical, actionable guidance

### Git Conventions

All commits follow [Conventional Commits](https://www.conventionalcommits.org/) with gitmoji prefixes:

```
✨ feat(scope): Add new feature
🐛 fix(scope): Fix bug
📝 docs(scope): Update documentation
```

## Skill Components

### SKILL.md
The main skill file containing:
- Workflow (step-by-step checklist)
- Gitmoji quick reference
- Best practices
- Links to detailed references

### scripts/gitmoji_selector.py
Python utility script for:
- Analyzing commit messages
- Suggesting appropriate gitmojis
- Generating Conventional Commits format
- Regex-based pattern matching for commit types

Usage:
```bash
python3 scripts/gitmoji_selector.py "your commit message"
python3 scripts/gitmoji_selector.py --conventional feat auth "Your subject"
```

### references/gitmoji-guide.md
Complete reference guide with:
- 40+ gitmojis categorized by type
- Usage descriptions and examples
- Selection decision tree
- Format specifications
- Tips for consistent usage

## Workflow Overview

The skill provides:
1. **Working tree inspection** - Check git status and diff
2. **Commit boundary planning** - Decide what goes in each commit
3. **Gitmoji selection** - Use reference or script to pick emoji
4. **Change staging** - Stage only intended changes
5. **Review** - Verify staged changes
6. **Message writing** - Conventional Commits with gitmoji
7. **Verification** - Run tests before committing
8. **Repetition** - Continue until working tree is clean

## Distribution

This skill can be distributed via:
- **Direct installation**: Copy `gitmoji-commits/` directory
- **NPX**: `npx skills add <github-url> --skill gitmoji-commits`
- **Package format**: `.skill` file (zip archive with skill contents)

## Contributing

When improving this skill:
1. Update `SKILL.md` for workflow changes
2. Update `references/gitmoji-guide.md` for gitmoji additions
3. Improve `scripts/gitmoji_selector.py` for better matching
4. Follow Conventional Commits with gitmojis
5. Validate with skills-ref before publishing
