# 🗡️ ZORO - Advanced Security Assessment Tool

**Version 1.0.0** | Professional-Grade Security Scanner

ZORO is a comprehensive security assessment framework that combines the best features of multiple security tools into one unified, powerful solution. Named after the legendary swordsman, ZORO delivers precision, power, and professional results.

## 🌟 Features

### Reconnaissance
- **Subdomain Enumeration**: Multiple methods including DNS brute-force, certificate transparency logs
- **Port Scanning**: Fast, multi-threaded port scanning with service detection
- **Technology Detection**: Identify web frameworks, CMS, servers, and technologies
- **Directory Discovery**: Find hidden directories and sensitive files
- **Security Headers Analysis**: Comprehensive security posture assessment

### Vulnerability Scanning
- **SQL Injection Detection**: Advanced pattern matching and error-based detection
- **Cross-Site Scripting (XSS)**: Reflected and stored XSS testing
- **Open Redirect**: URL parameter manipulation testing
- **Sensitive File Exposure**: Detect exposed configuration files and backups
- **Security Misconfiguration**: Missing headers and insecure configurations

### Reporting
- **Professional HTML Reports**: Beautiful, comprehensive security reports
- **Executive Summaries**: High-level overviews for management
- **JSON Output**: Machine-readable results for automation
- **Risk Scoring**: Automated risk assessment (0-100 scale)

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection for scanning external targets

## 🚀 Installation

### Windows (PowerShell)

```powershell
# 1. Clone or download ZORO
cd ~\projects\zoro

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Verify installation
python zoro.py --help
```

### Linux/macOS

```bash
# 1. Navigate to ZORO directory
cd ~/projects/zoro

# 2. Install Python dependencies
pip3 install -r requirements.txt

# 3. Make executable (optional)
chmod +x zoro.py

# 4. Verify installation
python3 zoro.py --help
```

### Dependencies

The following Python packages will be installed:
- `requests` - HTTP library for web requests
- `dnspython` - DNS toolkit for subdomain enumeration
- `urllib3` - HTTP client library
- `beautifulsoup4` - HTML/XML parsing
- `lxml` - XML and HTML parser
- `colorama` - Cross-platform colored terminal text

## 📖 Usage

### Basic Usage

```bash
# Full security assessment
python zoro.py example.com

# Quick scan (reduced scope for faster results)
python zoro.py example.com --quick

# Reconnaissance only
python zoro.py example.com --recon-only

# Vulnerability scanning only
python zoro.py example.com --scan-only
```

### Advanced Options

```bash
# Verbose output
python zoro.py example.com --verbose

# JSON output only
python zoro.py example.com --output json

# HTML output only
python zoro.py example.com --output html

# Use custom configuration
python zoro.py example.com --config config/custom.json
```

### Examples

```bash
# Scan a website with full assessment
python zoro.py testphp.vulnweb.com

# Quick scan of a domain
python zoro.py example.com --quick

# Recon-only with verbose output
python zoro.py example.com --recon-only --verbose

# Full scan with JSON output
python zoro.py example.com --output json
```

## 📊 Output

ZORO generates multiple output formats:

### Reports Directory Structure
```
reports/
└── example.com_20251027_090530/
    ├── security_report.html      # Comprehensive HTML report
    ├── executive_summary.txt     # Executive summary
    └── scan_results.json         # Raw JSON data
```

### HTML Report
Professional, color-coded security report with:
- Risk score and severity breakdown
- Detailed vulnerability findings
- Reconnaissance results
- Technology stack information
- Remediation recommendations

### Executive Summary
Text-based summary perfect for:
- Quick review
- Management briefings
- Email sharing
- Terminal viewing

### JSON Output
Machine-readable format for:
- Automation and CI/CD integration
- Custom report generation
- Data analysis and trending
- Integration with other tools

## 🎯 Use Cases

### Penetration Testing
- Comprehensive security assessments
- Vulnerability identification
- Attack surface mapping
- Security posture evaluation

### Bug Bounty Hunting
- Quick reconnaissance
- Automated vulnerability discovery
- Multi-target scanning
- Professional reporting

### Security Audits
- Compliance checking
- Security header validation
- Configuration review
- Risk assessment

### DevSecOps
- CI/CD integration
- Continuous security testing
- Automated vulnerability tracking
- Security regression testing

## ⚠️ Legal Disclaimer

**IMPORTANT**: Only use ZORO on systems you own or have explicit authorization to test.

- Unauthorized access to computer systems is illegal
- Always obtain written permission before scanning
- Respect scope and boundaries set by target owners
- Follow responsible disclosure practices
- Comply with local laws and regulations

**The authors and contributors of ZORO are not responsible for any misuse or damage caused by this tool.**

## 🛡️ Features Comparison

### From "The Cave Ultimate"
✅ AI-powered vulnerability analysis patterns  
✅ Comprehensive reconnaissance engine  
✅ Professional HTML reporting  
✅ Risk assessment and scoring  

### From "DeepSeek Ninja"
✅ Multi-threaded scanning for performance  
✅ Screenshot capture capabilities (foundation)  
✅ Nuclei-style template system (architecture)  
✅ Executive summary generation  

### From "Dubai Cyber Sentinel"
✅ Dependency auto-installation  
✅ Cross-platform support  
✅ Modular architecture  
✅ Professional reporting templates  

## 📁 Project Structure

```
zoro/
├── zoro.py                          # Main entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── modules/
│   ├── recon/
│   │   ├── __init__.py
│   │   └── recon_engine.py         # Reconnaissance module
│   ├── scanner/
│   │   ├── __init__.py
│   │   └── vulnerability_scanner.py # Vulnerability scanner
│   ├── exploits/
│   │   └── __init__.py
│   └── reporting/
│       ├── __init__.py
│       └── report_generator.py      # Report generation
├── config/                          # Configuration files
├── reports/                         # Generated reports
├── wordlists/                       # Scanning wordlists
├── payloads/                        # Test payloads
└── logs/                            # Scan logs
```

## 🔧 Configuration

Create custom configurations in `config/custom.json`:

```json
{
  "quick": false,
  "verbose": true,
  "timeout": 10,
  "max_threads": 50,
  "output_format": "both"
}
```

## 🚧 Roadmap

### Version 1.1 (Planned)
- [ ] Screenshot capture with Selenium
- [ ] API security testing
- [ ] Authentication testing
- [ ] WordPress-specific scans

### Version 1.2 (Planned)
- [ ] Cloud security checks (AWS, Azure, GCP)
- [ ] SSL/TLS analysis
- [ ] Network scanning features
- [ ] Custom payload templates

### Version 2.0 (Future)
- [ ] GUI interface
- [ ] Plugin system
- [ ] Multi-target campaign management
- [ ] Continuous monitoring mode

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is released for educational and authorized security testing purposes only.

## 🙏 Acknowledgments

ZORO combines inspiration and techniques from:
- The Cave Ultimate
- DeepSeek Ninja
- Dubai Cyber Sentinel
- The security research community

## 📞 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Review documentation in `/docs`
- Check examples in `/examples`

## 🔍 Quick Start Example

```bash
# Install
cd ~/projects/zoro
pip install -r requirements.txt

# Test scan (use a legal testing target)
python zoro.py testphp.vulnweb.com

# View report
# Open: reports/testphp.vulnweb.com_*/security_report.html
```

---

**Remember**: With great power comes great responsibility. Use ZORO ethically and legally! 🗡️

**Version**: 1.0.0  
**Last Updated**: October 2025  
**Status**: Active Development
