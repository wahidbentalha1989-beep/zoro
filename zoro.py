#!/usr/bin/env python3
"""
ZORO - Advanced Security Assessment Tool
Combines reconnaissance, vulnerability scanning, and professional reporting
Version: 1.0.0
"""

import asyncio
import argparse
import sys
import os
from pathlib import Path
from datetime import datetime
import json

# Add modules to path
sys.path.append(str(Path(__file__).parent))

from modules.recon.recon_engine import ReconEngine
from modules.scanner.vulnerability_scanner import VulnerabilityScanner
from modules.reporting.report_generator import ReportGenerator

class ZoroScanner:
    """Main Zoro Security Scanner"""
    
    def __init__(self, target, config=None):
        self.target = target
        self.config = config or {}
        self.results = {
            'metadata': {
                'tool': 'ZORO Security Scanner',
                'version': '1.0.0',
                'target': target,
                'timestamp': datetime.now().isoformat(),
                'scan_id': datetime.now().strftime('%Y%m%d_%H%M%S')
            },
            'reconnaissance': {},
            'vulnerabilities': [],
            'risk_assessment': {}
        }
        
        # Initialize modules
        self.recon = ReconEngine(target, config)
        self.scanner = VulnerabilityScanner(target, config)
        self.reporter = ReportGenerator(config)
    
    def banner(self):
        """Display Zoro banner"""
        banner = r"""
    ███████╗ ██████╗ ██████╗  ██████╗ 
    ╚══███╔╝██╔═══██╗██╔══██╗██╔═══██╗
      ███╔╝ ██║   ██║██████╔╝██║   ██║
     ███╔╝  ██║   ██║██╔══██╗██║   ██║
    ███████╗╚██████╔╝██║  ██║╚██████╔╝
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
    
    Advanced Security Assessment Framework
    Version 1.0.0 | Professional Grade
    """
        print(banner)
        print(f"[>] Target: {self.target}")
        print(f"[>] Scan ID: {self.results['metadata']['scan_id']}")
        print(f"[>] Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    async def run_reconnaissance(self):
        """Execute reconnaissance phase"""
        print("[*] Phase 1: RECONNAISSANCE")
        print("=" * 60)
        
        recon_data = await self.recon.run_full_recon()
        self.results['reconnaissance'] = recon_data
        
        print(f"✓ Subdomains found: {len(recon_data.get('subdomains', []))}")
        print(f"✓ Open ports: {len(recon_data.get('ports', []))}")
        print(f"✓ Technologies detected: {len(recon_data.get('technologies', []))}")
        print()
    
    async def run_vulnerability_scan(self):
        """Execute vulnerability scanning phase"""
        print("[*] Phase 2: VULNERABILITY SCANNING")
        print("=" * 60)
        
        vulns = await self.scanner.scan_all()
        self.results['vulnerabilities'] = vulns
        
        critical = len([v for v in vulns if v.get('severity') == 'CRITICAL'])
        high = len([v for v in vulns if v.get('severity') == 'HIGH'])
        medium = len([v for v in vulns if v.get('severity') == 'MEDIUM'])
        
        print(f"✓ Total vulnerabilities: {len(vulns)}")
        print(f"  - Critical: {critical}")
        print(f"  - High: {high}")
        print(f"  - Medium: {medium}")
        print()
    
    def calculate_risk_score(self):
        """Calculate overall risk assessment"""
        vulns = self.results['vulnerabilities']
        
        # Count by severity
        critical = len([v for v in vulns if v.get('severity') == 'CRITICAL'])
        high = len([v for v in vulns if v.get('severity') == 'HIGH'])
        medium = len([v for v in vulns if v.get('severity') == 'MEDIUM'])
        low = len([v for v in vulns if v.get('severity') == 'LOW'])
        
        # Calculate risk score (0-100)
        risk_score = min(100, critical * 25 + high * 10 + medium * 5 + low * 2)
        
        if risk_score >= 80:
            risk_level = 'CRITICAL'
        elif risk_score >= 60:
            risk_level = 'HIGH'
        elif risk_score >= 40:
            risk_level = 'MEDIUM'
        else:
            risk_level = 'LOW'
        
        self.results['risk_assessment'] = {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'critical_count': critical,
            'high_count': high,
            'medium_count': medium,
            'low_count': low,
            'total_vulnerabilities': len(vulns)
        }
    
    async def generate_reports(self):
        """Generate comprehensive reports"""
        print("[*] Phase 3: REPORT GENERATION")
        print("=" * 60)
        
        # Calculate risk before reporting
        self.calculate_risk_score()
        
        # Generate reports
        report_dir = Path(f"reports/{self.target}_{self.results['metadata']['scan_id']}")
        report_dir.mkdir(parents=True, exist_ok=True)
        
        # JSON report
        json_file = report_dir / "scan_results.json"
        with open(json_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"✓ JSON Report: {json_file}")
        
        # HTML report
        html_file = await self.reporter.generate_html_report(self.results, report_dir)
        print(f"✓ HTML Report: {html_file}")
        
        # Executive summary
        summary_file = await self.reporter.generate_executive_summary(self.results, report_dir)
        print(f"✓ Executive Summary: {summary_file}")
        print()
    
    def print_summary(self):
        """Print scan summary"""
        risk = self.results['risk_assessment']
        
        print("\n" + "=" * 60)
        print("SCAN COMPLETE - SUMMARY")
        print("=" * 60)
        print(f"Target: {self.target}")
        print(f"Risk Level: {risk['risk_level']} (Score: {risk['risk_score']}/100)")
        print(f"Total Vulnerabilities: {risk['total_vulnerabilities']}")
        print(f"  - Critical: {risk['critical_count']}")
        print(f"  - High: {risk['high_count']}")
        print(f"  - Medium: {risk['medium_count']}")
        print(f"  - Low: {risk['low_count']}")
        print(f"\nReports saved to: reports/{self.target}_{self.results['metadata']['scan_id']}/")
        print("=" * 60)
    
    async def run_full_scan(self):
        """Execute complete security assessment"""
        self.banner()
        
        try:
            # Phase 1: Reconnaissance
            await self.run_reconnaissance()
            
            # Phase 2: Vulnerability Scanning
            await self.run_vulnerability_scan()
            
            # Phase 3: Report Generation
            await self.generate_reports()
            
            # Print summary
            self.print_summary()
            
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n[!] Error during scan: {e}")
            sys.exit(1)


async def main():
    parser = argparse.ArgumentParser(
        description='ZORO - Advanced Security Assessment Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  zoro.py example.com                    # Full scan
  zoro.py example.com --quick            # Quick scan
  zoro.py example.com --recon-only       # Reconnaissance only
  zoro.py example.com --scan-only        # Vulnerability scan only
  zoro.py example.com --output json      # JSON output only
        """
    )
    
    parser.add_argument('target', help='Target domain or URL')
    parser.add_argument('--quick', action='store_true', help='Quick scan (limited scope)')
    parser.add_argument('--recon-only', action='store_true', help='Reconnaissance only')
    parser.add_argument('--scan-only', action='store_true', help='Vulnerability scanning only')
    parser.add_argument('--output', choices=['html', 'json', 'both'], default='both', help='Report format')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--config', help='Configuration file path')
    
    args = parser.parse_args()
    
    # Load configuration if provided
    config = {}
    if args.config and Path(args.config).exists():
        with open(args.config) as f:
            config = json.load(f)
    
    # Apply command-line options to config
    config['quick'] = args.quick
    config['verbose'] = args.verbose
    config['output_format'] = args.output
    
    # Initialize and run scanner
    scanner = ZoroScanner(args.target, config)
    
    if args.recon_only:
        scanner.banner()
        await scanner.run_reconnaissance()
    elif args.scan_only:
        scanner.banner()
        await scanner.run_vulnerability_scan()
    else:
        await scanner.run_full_scan()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        sys.exit(0)
