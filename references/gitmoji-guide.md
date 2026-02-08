# Gitmoji Guide

Complete reference of gitmojis for semantic commit messages.

## Semantic Gitmoji Mapping

### Features & Enhancement
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| ✨ | `:sparkles:` | Introduce new features | `✨ Add user authentication module` |
| 🎨 | `:art:` | Improve structure/format of code | `🎨 Refactor API response handler` |
| ⚡ | `:zap:` | Improve performance | `⚡ Optimize database queries` |
| 🚀 | `:rocket:` | Deploy to production | `🚀 Release v2.0.0` |
| 💄 | `:lipstick:` | Add/update UI or styles | `💄 Update button styling` |

### Bug Fixes & Issues
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| 🐛 | `:bug:` | Fix a bug | `🐛 Fix null pointer exception` |
| 🔧 | `:wrench:` | Fix configuration files | `🔧 Update environment variables` |
| 🩹 | `:adhesive_bandage:` | Simple bug fix (one-liner) | `🩹 Fix typo in config` |
| 🔨 | `:hammer:` | Major refactoring/rewrite | `🔨 Rewrite authentication system` |

### Code Quality
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| ♻️ | `:recycle:` | Refactor code | `♻️ Extract common utilities` |
| 📝 | `:memo:` | Add/update documentation | `📝 Add API documentation` |
| 🧪 | `:test_tube:` | Add/update tests | `🧪 Add integration tests` |
| ✅ | `:white_check_mark:` | Pass tests/CI checks | `✅ All tests passing` |
| 📊 | `:bar_chart:` | Add/update analytics | `📊 Add performance metrics` |

### Dependencies & Build
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| 📦 | `:package:` | Add/update dependencies | `📦 Update npm packages` |
| 🔐 | `:lock:` | Fix security vulnerability | `🔐 Patch XSS vulnerability` |
| ⬆️ | `:arrow_up:` | Upgrade dependencies | `⬆️ Upgrade React to v18` |
| ⬇️ | `:arrow_down:` | Downgrade dependencies | `⬇️ Revert lodash version` |
| 🔨 | `:hammer:` | Build system changes | `🔨 Update webpack config` |

### Releases & Versions
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| 🏷️ | `:label:` | Release/version tag | `🏷️ Release v1.0.0` |
| 📈 | `:chart_with_upwards_trend:` | Add/update benchmarks | `📈 Performance improvement` |

### Documentation & Comments
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| 📚 | `:books:` | Add documentation files | `📚 Add developer guide` |
| 💬 | `:speech_balloon:` | Update/add comments | `💬 Add function documentation` |
| 🗣️ | `:speaking_head:` | Update translations | `🗣️ Add Spanish translations` |

### Cleanup & Maintenance
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| 🗑️ | `:wastebasket:` | Remove files/code | `🗑️ Remove deprecated API` |
| 🧹 | `:broom:` | Clean up code/files | `🧹 Remove unused imports` |
| 🎯 | `:dart:` | Focus/target specific task | `🎯 Focus on core features` |

### Config & CI/CD
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| ⚙️ | `:gear:` | Configuration changes | `⚙️ Update CI/CD pipeline` |
| 🔄 | `:repeat:` | Recurring task/automation | `🔄 Auto-format on save` |
| 🚀 | `:rocket:` | Deployment | `🚀 Deploy to staging` |

### Special Cases
| Emoji | Code | Use Case | Example |
|-------|------|----------|---------|
| 💡 | `:bulb:` | Add/update ideas/comments | `💡 Add performance tips` |
| 🎭 | `:performing_arts:` | Mock implementations | `🎭 Add mock API responses` |
| 🚨 | `:rotating_light:` | Remove linter warnings | `🚨 Fix ESLint errors` |
| 🔍 | `:mag:` | SEO improvements | `🔍 Improve SEO metadata` |

## Selection Algorithm

When selecting a gitmoji, follow this decision tree:

1. **Is this a new feature?** → ✨ `:sparkles:`
2. **Is this a bug fix?** → 🐛 `:bug:` (or 🩹 if simple)
3. **Is this documentation?** → 📝 `:memo:` or 📚 `:books:`
4. **Is this a refactor?** → ♻️ `:recycle:` or 🎨 `:art:` (style-focused)
5. **Is this a performance improvement?** → ⚡ `:zap:`
6. **Is this dependency-related?** → 📦 `:package:` or ⬆️/⬇️
7. **Is this security-related?** → 🔐 `:lock:`
8. **Is this testing?** → 🧪 `:test_tube:`
9. **Is this a major rewrite?** → 🔨 `:hammer:`
10. **Is this cleanup?** → 🗑️ or 🧹 `:broom:`

## Format

Standard format: `emoji type(scope): subject`

```
✨ feat(auth): Add two-factor authentication

- Implement TOTP support
- Update user model
- Add verification endpoint

Closes #123
```

## Tips

- **One gitmoji per commit**: Each commit should have exactly one primary emoji
- **Keep subjects short**: Max 50 characters in the subject line
- **Be specific**: Use the most appropriate emoji, not just a generic one
- **Combine with Conventional Commits**: Emoji + type + scope for maximum clarity
