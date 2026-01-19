#!/bin/bash
# Installation script for shared-orm package

set -e

echo "==================================="
echo "Installing shared-orm package"
echo "==================================="

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Install in development mode
echo "Installing in development mode..."
pip install -e "$SCRIPT_DIR"

echo ""
echo "==================================="
echo "Installation complete!"
echo "==================================="
echo ""
echo "To verify the installation, run:"
echo "  python -c 'from shared_orm import Base; print(Base)'"
echo ""
echo "To run tests:"
echo "  cd $SCRIPT_DIR && pytest tests/"
echo ""
echo "To install with dev dependencies:"
echo "  pip install -e '$SCRIPT_DIR[dev]'"

