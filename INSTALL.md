# 🚀 ZORO Installation Guide

## Quick Install (Windows)

### Prerequisites
- Python 3.7+ installed ([Download Python](https://www.python.org/downloads/))
- pip package manager (included with Python)

### Installation Steps

1. **Navigate to ZORO directory**
   ```powershell
   cd C:\Users\teama\projects\zoro
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```powershell
   python zoro.py --help
   ```

### Expected Output
```
usage: zoro.py [-h] [--quick] [--recon-only] [--scan-only] 
               [--output {html,json,both}] [--verbose] [--config CONFIG]
               target

ZORO - Advanced Security Assessment Tool
```

## First Scan

Test ZORO with a legal testing target:

```powershell
python zoro.py testphp.vulnweb.com --quick
```

This will:
- Perform reconnaissance
- Scan for vulnerabilities
- Generate reports in `reports/` directory

## Troubleshooting

### Error: "No module named 'requests'"
**Solution**: Install dependencies
```powershell
pip install -r requirements.txt
```

### Error: "Python not found"
**Solution**: Add Python to PATH or use full path
```powershell
C:\Python311\python.exe zoro.py --help
```

### SSL Certificate Errors
ZORO disables SSL verification by default for testing. This is normal.

### Permission Errors
Run PowerShell as Administrator if you encounter permission issues.

## What's Next?

1. **Read the docs**: Check `README.md` for full documentation
2. **Run a full scan**: `python zoro.py example.com`
3. **View reports**: Open HTML reports in `reports/` directory
4. **Customize**: Create config files in `config/` directory

## Need Help?

- 📖 Full Documentation: `README.md`
- 🐛 Report Issues: Create an issue on GitHub
- 💬 Questions: Check documentation first

---

**⚠️ Remember**: Only scan authorized targets!
