#!/bin/bash

################################################################################
# ZORO - Automated Setup Script for Kali Linux
# This script will install all dependencies and run a test scan automatically
################################################################################

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
cat << "EOF"
    ███████╗ ██████╗ ██████╗  ██████╗ 
    ╚══███╔╝██╔═══██╗██╔══██╗██╔═══██╗
      ███╔╝ ██║   ██║██████╔╝██║   ██║
     ███╔╝  ██║   ██║██╔══██╗██║   ██║
    ███████╗╚██████╔╝██║  ██║╚██████╔╝
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
    
    Automated Setup Script for Kali Linux
    Advanced Security Assessment Framework
EOF
echo -e "${NC}"

echo -e "${GREEN}[+] Starting ZORO installation...${NC}\n"

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo -e "${YELLOW}[!] Warning: Running as root. Consider running as normal user.${NC}"
fi

# Step 1: Update system packages
echo -e "${BLUE}[1/6] Updating system packages...${NC}"
sudo apt-get update -qq

# Step 2: Install Python3 and pip if not present
echo -e "${BLUE}[2/6] Checking Python3 installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}[!] Python3 not found. Installing...${NC}"
    sudo apt-get install -y python3 python3-pip
else
    echo -e "${GREEN}✓ Python3 already installed ($(python3 --version))${NC}"
fi

if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}[!] pip3 not found. Installing...${NC}"
    sudo apt-get install -y python3-pip
else
    echo -e "${GREEN}✓ pip3 already installed${NC}"
fi

# Step 3: Install system dependencies
echo -e "${BLUE}[3/6] Installing system dependencies...${NC}"
sudo apt-get install -y \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    dnsutils \
    git 2>/dev/null || echo -e "${YELLOW}[!] Some packages may already be installed${NC}"

# Step 4: Create virtual environment (optional but recommended)
echo -e "${BLUE}[4/6] Setting up Python virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
source venv/bin/activate

# Step 5: Install Python dependencies
echo -e "${BLUE}[5/6] Installing Python dependencies...${NC}"
pip3 install --upgrade pip -q
pip3 install -r requirements.txt -q

echo -e "${GREEN}✓ All dependencies installed successfully${NC}\n"

# Step 6: Verify installation
echo -e "${BLUE}[6/6] Verifying installation...${NC}"
python3 zoro.py --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ ZORO installed successfully!${NC}\n"
else
    echo -e "${RED}✗ Installation verification failed${NC}\n"
    exit 1
fi

# Display installation summary
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}           INSTALLATION COMPLETE!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}\n"

echo -e "${YELLOW}Quick Start Commands:${NC}"
echo -e "  ${BLUE}source venv/bin/activate${NC}          # Activate virtual environment"
echo -e "  ${BLUE}python3 zoro.py --help${NC}            # Show help"
echo -e "  ${BLUE}python3 zoro.py testphp.vulnweb.com --quick${NC}  # Run test scan\n"

# Ask if user wants to run a test scan
echo -e "${YELLOW}Would you like to run a test scan now? (y/n)${NC}"
read -r response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo -e "\n${GREEN}[+] Running test scan on testphp.vulnweb.com...${NC}\n"
    python3 zoro.py testphp.vulnweb.com --quick
    
    echo -e "\n${GREEN}════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}Test scan complete! Check the reports/ directory for results.${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}\n"
    
    # Show report location
    if [ -d "reports" ]; then
        latest_report=$(ls -td reports/*/ 2>/dev/null | head -1)
        if [ -n "$latest_report" ]; then
            echo -e "${YELLOW}Latest report location:${NC}"
            echo -e "  ${BLUE}${latest_report}${NC}\n"
            echo -e "${YELLOW}View reports:${NC}"
            echo -e "  ${BLUE}firefox ${latest_report}security_report.html &${NC}  # HTML report"
            echo -e "  ${BLUE}cat ${latest_report}executive_summary.txt${NC}     # Executive summary"
        fi
    fi
else
    echo -e "\n${GREEN}Setup complete! You can run ZORO anytime with:${NC}"
    echo -e "  ${BLUE}cd $(pwd)${NC}"
    echo -e "  ${BLUE}source venv/bin/activate${NC}"
    echo -e "  ${BLUE}python3 zoro.py <target> --quick${NC}\n"
fi

echo -e "${RED}⚠️  IMPORTANT LEGAL NOTICE:${NC}"
echo -e "${RED}Only scan systems you own or have explicit written authorization to test!${NC}"
echo -e "${RED}Unauthorized scanning is illegal and unethical.${NC}\n"

echo -e "${GREEN}For full documentation, see:${NC}"
echo -e "  ${BLUE}cat README.md${NC}"
echo -e "  ${BLUE}cat WARP.md${NC}\n"

# Deactivate virtual environment
deactivate 2>/dev/null || true

exit 0
