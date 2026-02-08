#!/usr/bin/env python3
"""
Gitmoji selector - Maps change types to appropriate gitmojis
Analyzes commit messages and suggests the best gitmoji
"""

import sys
import json
import re
from typing import Tuple, Optional

# Gitmoji mapping: (patterns, emoji, description)
# Order matters - more specific patterns first
GITMOJI_MAPPING = [
    # Security (check before bug fix)
    (
        r'\b(security|secure|vulnerability|cve|exploit|xss|csrf|patch)\b',
        '🔐',
        'lock - fix security vulnerability',
    ),
    
    # Documentation (check before general feature)
    (
        r'\b(doc|docs|documentation|readme|guide|comment)\b',
        '📝',
        'memo - documentation',
    ),
    
    # Testing
    (
        r'\b(test|tests|unit test|integration test)\b',
        '🧪',
        'test_tube - add/update tests',
    ),
    
    # Bug fixes
    (
        r'\b(fix|bug|bugfix|issue)\b',
        '🐛',
        'bug - bug fix',
    ),
    
    # Refactoring (check before add)
    (
        r'\b(refactor|refactoring|extract|clean|cleanup|reorgan)\b',
        '♻️',
        'recycle - refactor code',
    ),
    
    # Performance
    (
        r'\b(perf|performance|optimize|optimized|speed|faster|efficient)\b',
        '⚡',
        'zap - improve performance',
    ),
    
    # Styling/UI
    (
        r'\b(style|ui|css|design|theme|color|layout|component|visual)\b',
        '💄',
        'lipstick - add/update UI or styles',
    ),
    
    # Dependencies
    (
        r'\b(dependencies|depend|npm|package|upgrade|install|version)\b',
        '📦',
        'package - add/update dependencies',
    ),
    
    # Build/Config
    (
        r'\b(build|config|configuration|setup|webpack|babel|tsconfig|env)\b',
        '⚙️',
        'gear - configuration changes',
    ),
    
    # Major rewrite
    (
        r'\b(rewrite|major|breaking|redesign|rework)\b',
        '🔨',
        'hammer - major refactoring',
    ),
    
    # Cleanup
    (
        r'\b(remove|delete|unused|deprecated|cleanup)\b',
        '🗑️',
        'wastebasket - remove files/code',
    ),
    
    # Features (check last)
    (
        r'\b(feat|new|feature|add)\b',
        '✨',
        'sparkles - new feature',
    ),
]

def analyze_commit(commit_message: str) -> Tuple[str, str]:
    """
    Analyze commit message and suggest gitmoji
    
    Args:
        commit_message: Full commit message or diff summary
        
    Returns:
        Tuple of (emoji, description)
    """
    message_lower = commit_message.lower()
    
    # Try to find matching pattern
    for pattern, emoji, description in GITMOJI_MAPPING:
        if re.search(pattern, message_lower):
            return emoji, description
    
    # Default to sparkles for general features
    return '✨', 'sparkles - general change'

def extract_gitmoji_from_message(message: str) -> Optional[str]:
    """Check if message already has a gitmoji"""
    match = re.match(r'^[^\w\s]\s', message)
    return match.group(0)[0] if match else None

def suggest_with_conventional_commits(
    commit_type: str,
    scope: Optional[str],
    message: str,
) -> str:
    """
    Generate commit message with gitmoji + conventional commits
    
    Args:
        commit_type: Type of change (feat, fix, refactor, etc.)
        scope: Optional scope (auth, api, ui, etc.)
        message: Commit message
        
    Returns:
        Formatted commit message with gitmoji
    """
    emoji, _ = analyze_commit(commit_type + ' ' + message)
    
    scope_str = f'({scope})' if scope else ''
    return f'{emoji} {commit_type}{scope_str}: {message}'

def main():
    if len(sys.argv) < 2:
        print('Usage: gitmoji_selector.py <commit-message>')
        print('       gitmoji_selector.py --conventional <type> [scope] <message>')
        sys.exit(1)
    
    if sys.argv[1] == '--conventional' and len(sys.argv) >= 4:
        # Handle conventional commits format
        commit_type = sys.argv[2]
        if len(sys.argv) == 4:
            # No scope
            message = sys.argv[3]
            scope = None
        else:
            # Has scope
            scope = sys.argv[3]
            message = ' '.join(sys.argv[4:])
        
        result = suggest_with_conventional_commits(commit_type, scope, message)
        print(result)
    else:
        # Analyze full message
        message = ' '.join(sys.argv[1:])
        emoji, description = analyze_commit(message)
        print(json.dumps({
            'emoji': emoji,
            'description': description,
            'suggested_format': f'{emoji} {message}'
        }, indent=2))

if __name__ == '__main__':
    main()
