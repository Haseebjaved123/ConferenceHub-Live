#!/usr/bin/env python3
"""
Simple test script to verify the conference update system works
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from update_conferences import main
    print("✅ Import successful")
    
    # Test with minimal data
    print("🔄 Testing conference update...")
    main()
    print("✅ Test completed successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages: pip install -r requirements.txt")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
