# ⚡ ZORO Quick Start Guide

Get started with ZORO in 3 minutes!

## 🚀 Installation (1 minute)

```powershell
# 1. Navigate to ZORO
cd C:\Users\teama\projects\zoro

# 2. Install dependencies
pip install -r requirements.txt
```

## 🎯 First Scan (2 minutes)

```powershell
# Test with a legal target
python zoro.py testphp.vulnweb.com --quick
```

**What happens:**
- Reconnaissance phase runs
- Vulnerability scanning starts
- Reports are generated automatically

## 📊 View Results

Reports are saved in `reports/` directory:

```powershell
# List generated reports
ls reports/

# Open HTML report (example)
start reports/testphp.vulnweb.com_20251027_*/security_report.html
```

## 🔥 Common Commands

```powershell
# Full comprehensive scan
python zoro.py example.com

# Quick scan (faster, less thorough)
python zoro.py example.com --quick

# Only reconnaissance
python zoro.py example.com --recon-only

# Only vulnerability scanning
python zoro.py example.com --scan-only

# Verbose output
python zoro.py example.com --verbose

# JSON output only
python zoro.py example.com --output json
```

## 📋 What You Get

### Security Report (HTML)
- Professional design
- Color-coded severity levels
- Detailed vulnerability descriptions
- Remediation recommendations

### Executive Summary (TXT)
- High-level overview
- Risk score (0-100)
- Quick vulnerability counts
- Action items

### Raw Data (JSON)
- Machine-readable format
- Complete scan results
- Easy integration with other tools

## 🎓 Next Steps

1. **Read full docs**: Check `README.md`
2. **Customize config**: Create `config/custom.json`
3. **Advanced scanning**: Try different options
4. **Report analysis**: Review HTML reports

## ⚠️ Important Reminders

✅ **DO:**
- Only scan authorized targets
- Get written permission first
- Use on your own systems
- Report vulnerabilities responsibly

❌ **DON'T:**
- Scan without permission
- Use on production systems without approval
- Ignore legal boundaries
- Harm or damage systems

## 🐛 Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'requests'`  
**Solution**: Run `pip install -r requirements.txt`

**Problem**: Python not found  
**Solution**: Make sure Python is in your PATH

**Problem**: Permission errors  
**Solution**: Run PowerShell as Administrator

## 💡 Pro Tips

- Start with `--quick` to get fast results
- Use `--verbose` to see what's happening
- Check HTML reports for best presentation
- Use JSON reports for automation

## 🔗 Resources

- 📖 Full Documentation: `README.md`
- 🛠️ Installation Guide: `INSTALL.md`
- 💬 Get Help: Create an issue

---

**Ready to scan?** Run: `python zoro.py --help`
