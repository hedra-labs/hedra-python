# Hedra CLI

A comprehensive command-line interface for the Hedra API, providing unified video generation capabilities.

## Features

- **Unified Generate Command**: Complete end-to-end character video creation in a single command
- **Voice Resolution**: Use friendly voice names (Alice, Brian, etc.) instead of IDs  
- **Face Detection**: Automatic face detection and selection for multi-face images
- **Bounding Box Animation**: Precise face region targeting for animation
- **Rich Output**: Progress tracking and detailed feedback
- **Debug Tools**: API payload inspection and bounding box visualization

## Quick Start

```bash
# Basic usage
python -m hedra.lib.cli generate \
  --text "Hello world" \
  --voice-name "Alice" \
  --img "face.jpg"

# Advanced usage with animation
python -m hedra.lib.cli generate \
  --text "Welcome to AI news" \
  --voice-name "Alice" \
  --img "news-scene.png" \
  --bounding-box "0.243,0.277" \
  --aspect-ratio "16:9" \
  --animation-prompt "News anchor speaking confidently"
```

## Commands

- `generate` - Unified video generation workflow
- `voices` - List and preview available voices
- `projects` - Manage video generation projects
- `characters` - Character creation operations
- `portraits` - Image upload and management
- `audio` - Audio file operations
- `config` - CLI configuration management

## Architecture

```
cli/
├── commands/          # Individual CLI commands
│   ├── generate.py   # Unified generation workflow
│   ├── voices.py     # Voice management
│   └── ...
├── face/             # Face detection and processing
├── utils/            # Shared utilities
└── main.py           # CLI entry point
```

## Key Implementation Details

- **Correct Bounding Box Format**: Uses web app compatible `generated_video_inputs.bounding_box_target` structure
- **Asset Management**: Proper separation of avatar files vs source images for animation
- **Error Handling**: Comprehensive error reporting with helpful suggestions
- **Type Safety**: Full typing support with runtime validation

## Integration

This CLI is integrated into the main hedra package via pyproject.toml:

```toml
[project.scripts]
hedra = "hedra.lib.cli.main:cli"
```

Allows usage as: `hedra generate --text "Hello" --voice-name "Alice" --img "face.jpg"`