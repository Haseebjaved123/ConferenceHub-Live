#!/usr/bin/env python3
"""
Setup script for ConferenceHub-Live
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def test_system():
    """Test the conference update system"""
    try:
        # Import and test
        from update_conferences import load_csv_safe, parse_date, get_primary_deadline
        import pandas as pd
        
        # Test date parsing
        test_date = parse_date("2025-01-15")
        assert test_date is not None, "Date parsing failed"
        
        # Test CSV loading
        df = load_csv_safe("data/manual_seeds.csv")
        assert not df.empty, "CSV loading failed"
        
        print("✅ System tests passed")
        return True
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

def main():
    print("🚀 Setting up ConferenceHub-Live...")
    
    # Install requirements
    if not install_requirements():
        return False
    
    # Test system
    if not test_system():
        return False
    
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Run: python update_conferences.py")
    print("2. Check README.md for updated conference table")
    print("3. Push to GitHub to enable automated updates")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
