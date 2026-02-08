# Gitmoji Commits

Create high-quality git commits with semantic gitmoji emojis that make your commit history readable and visually organized.

## About This Skill

This skill extends AI agent capabilities to:
- **Automatically suggest** appropriate gitmojis for commit types
- **Write meaningful** Conventional Commits with emoji prefixes
- **Organize commits** logically with proper scoping
- **Review changes** before staging to ensure quality

Perfect for making commit history that tells a story and enables automated versioning with semantic gitmojis.

## Installation

```bash
# Install using npx skills CLI
npx skills add <repo-url> --skill gitmoji-commits

# Or list all available skills
npx skills add <repo-url> --list
```

## Features

### Semantic Gitmoji Selection
- 40+ categorized gitmojis
- Automatic pattern matching for commit types
- Decision tree for choosing the right emoji

### Smart Commit Workflow
- Inspect working tree before staging
- Split commits by logical boundaries
- Review staged changes before committing
- Verify with tests/build

### Conventional Commits Format
```
✨ feat(scope): Add new feature

- Implementation details
- More details

Closes #123
```

### Python Script Helper
```bash
# Analyze message and suggest gitmoji
python3 scripts/gitmoji_selector.py "fix critical bug"

# Generate Conventional Commits
python3 scripts/gitmoji_selector.py --conventional feat auth "Add authentication"
```

## Gitmoji Quick Reference

This skill uses the official [Gitmoji](https://gitmoji.dev/) specification as its primary reference. Here are some common gitmojis and their meanings:

| Type | Emoji | Example |
|------|-------|---------|
| Feature | ✨ | Add new functionality |
| Bug Fix | 🐛 | Fix error or issue |
| Documentation | 📝 | Add/update docs |
| Tests | 🧪 | Add/update tests |
| Refactor | ♻️ | Reorganize code |
| Performance | ⚡ | Optimize speed |
| Security | 🔐 | Fix vulnerability |
| Style | 💄 | Update UI/styling |
| Dependencies | 📦 | Update libraries |
| Build/Config | ⚙️ | Config changes |
| Cleanup | 🗑️ | Remove code |

See `references/gitmoji-guide.md` for complete reference with 40+ emojis.

## Usage Example

```bash
# Stage your changes
git add .

# Get gitmoji suggestion
python3 scripts/gitmoji_selector.py "added user authentication"
# Output: ✨ feat: added user authentication

# Commit with gitmoji
git commit -m "✨ feat(auth): Add user authentication

- Implement JWT tokens
- Add login endpoint  
- Update user model

Closes #42"
```

## Key Components

### SKILL.md
Complete skill documentation with workflow steps and best practices.

### scripts/gitmoji_selector.py
Python utility for automatic gitmoji suggestion and Conventional Commits generation.

### references/gitmoji-guide.md
Comprehensive gitmoji reference with categories, examples, and decision tree.

## Best Practices

1. **One gitmoji per commit** - Each commit has exactly one primary emoji
2. **Be specific** - Choose the most appropriate emoji for your change
3. **Atomic commits** - Each commit should be independently buildable
4. **Clear messages** - Subject line should make sense without the body
5. **Consistent scopes** - Use consistent scope names across commits

## Repository Information

- **Format**: [Agent Skills](https://agentskills.io/)
- **License**: MIT
- **Version**: 1.0.0

See `AGENTS.md` for repository structure and contribution guidelines.
