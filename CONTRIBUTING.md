# Contributing to URDU-OCR-CNN

Thank you for your interest in contributing to URDU-OCR-CNN! We welcome contributions from the community and are grateful for your support.

## 🎯 Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features or enhancements
- 📝 Improve documentation
- 🔧 Submit bug fixes
- ✨ Implement new features
- 🧪 Add or improve tests
- 🎨 Enhance UI/UX design

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher
- Node.js 18 or higher
- Git
- Docker (optional, for containerized development)

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/URDU-OCR-CNN.git
   cd URDU-OCR-CNN
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/H0NEYP0T-466/URDU-OCR-CNN.git
   ```

### Setup Development Environment

#### Backend Setup
```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

#### Frontend Setup
```bash
# From the root directory
npm install

# Copy environment file
cp .env.example .env
```

## 📋 Development Workflow

### 1. Create a Branch

Create a new branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - for new features
- `fix/` - for bug fixes
- `docs/` - for documentation changes
- `refactor/` - for code refactoring
- `test/` - for adding or updating tests
- `chore/` - for maintenance tasks

### 2. Make Your Changes

- Write clean, readable, and well-documented code
- Follow the existing code style and conventions
- Add comments where necessary
- Update documentation if needed

### 3. Test Your Changes

#### Backend Tests
```bash
cd backend
pytest tests/ -v
```

#### Frontend Tests
```bash
npm run test
```

#### Linting
```bash
# Backend
cd backend
# Add any linting commands here (e.g., flake8, black, pylint)

# Frontend
npm run lint
```

### 4. Commit Your Changes

Write clear and meaningful commit messages:
```bash
git add .
git commit -m "feat: add new feature description"
```

Commit message format:
- `feat:` - new feature
- `fix:` - bug fix
- `docs:` - documentation changes
- `style:` - formatting, missing semicolons, etc.
- `refactor:` - code refactoring
- `test:` - adding or updating tests
- `chore:` - maintenance tasks
- `perf:` - performance improvements

### 5. Keep Your Branch Updated

Regularly sync your branch with the upstream repository:
```bash
git fetch upstream
git rebase upstream/main
```

### 6. Push Your Changes

```bash
git push origin your-branch-name
```

### 7. Create a Pull Request

1. Go to the [URDU-OCR-CNN repository](https://github.com/H0NEYP0T-466/URDU-OCR-CNN)
2. Click on "Pull Requests" → "New Pull Request"
3. Select your branch
4. Fill out the pull request template with:
   - Clear description of changes
   - Related issue number (if applicable)
   - Screenshots (for UI changes)
   - Testing instructions
5. Submit the pull request

## 📝 Code Style Guidelines

### Python (Backend)

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where applicable
- Write docstrings for functions and classes
- Keep functions focused and concise
- Use meaningful variable and function names

Example:
```python
def predict_character(image: np.ndarray) -> Dict[str, Any]:
    """
    Predict Urdu character from image.
    
    Args:
        image: Input image as numpy array
        
    Returns:
        Dictionary containing prediction results
    """
    # Implementation
    pass
```

### TypeScript/React (Frontend)

- Follow React best practices
- Use functional components and hooks
- Write clean, readable JSX
- Use TypeScript for type safety
- Keep components small and focused
- Use meaningful component and variable names

Example:
```typescript
interface PredictionResultProps {
  predictions: Prediction[];
  loading: boolean;
}

const PredictionResult: React.FC<PredictionResultProps> = ({ 
  predictions, 
  loading 
}) => {
  // Implementation
};
```

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Clear title** - Brief description of the issue
2. **Description** - Detailed explanation of the problem
3. **Steps to reproduce** - How to recreate the bug
4. **Expected behavior** - What should happen
5. **Actual behavior** - What actually happens
6. **Environment** - OS, Python/Node version, browser
7. **Screenshots** - If applicable
8. **Error messages** - Full error logs

Use our [Bug Report Template](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/issues/new?template=bug_report.yml)

## 💡 Suggesting Features

When suggesting features, please include:

1. **Clear title** - Brief description of the feature
2. **Problem statement** - What problem does it solve?
3. **Proposed solution** - How should it work?
4. **Alternatives** - Other solutions considered
5. **Additional context** - Any other relevant information

Use our [Feature Request Template](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/issues/new?template=feature_request.yml)

## 📖 Documentation

- Update README.md if adding new features
- Add API documentation for new endpoints
- Include code comments for complex logic
- Update setup instructions if needed
- Add examples and usage guidelines

## ✅ Pull Request Checklist

Before submitting your PR, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added (if applicable)
- [ ] Documentation updated (if applicable)
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main
- [ ] No merge conflicts
- [ ] Screenshots included (for UI changes)
- [ ] Backward compatibility maintained (or breaking changes noted)

## 🔍 Code Review Process

1. A maintainer will review your pull request
2. They may request changes or ask questions
3. Make requested changes and push updates
4. Once approved, your PR will be merged
5. Your contribution will be credited

## 🎉 Recognition

Contributors are recognized in:
- GitHub contributors list
- Release notes (for significant contributions)
- Project acknowledgments

## ❓ Questions?

If you have questions:
- Check existing [issues](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/issues)
- Start a [discussion](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/discussions)
- Read the [documentation](docs/)

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to URDU-OCR-CNN! 🙏
