![Screenshot 2024-10-29 082406](https://github.com/user-attachments/assets/8e48a7c2-6326-4c0d-a354-714dcb0cd789)# Cherlock

![images](https://github.com/user-attachments/assets/bbe6330a-9579-48a5-8602-b310d1355d43)

**Cherlock** is an advanced vulnerability detection and analysis tool designed to provide a comprehensive and proactive assessment of security vulnerabilities within information systems. It focuses on recognition and information collection with an emphasis on simplicity and performance.

## Features

### DNS Details
- **DNS Mapping**: DNS visualization via advanced techniques, including DNS dumpster.
- **WHOIS Information**: Complete recovery of WHOIS data for domains.

### TLS Security
- **Supported ciphers**: Identification of supported encryption algorithms.
- **TLS versions**: Detection of active TLS versions.
- **Certificate and SAN Details**: Extract certificate information, including Subject Alternative Names (SANs).

### Port Analysis
- **Port Scans**: Evaluation of open ports for detection of active services.
- **Services and Scripts Scan**: Use of specific scripts to obtain detailed information about online services.

### Fuzzing and Enumeration
- **URL Fuzzing and File/Dir Detection**: Search for hidden or sensitive files and directories.
- **Subdomain enumeration**: Includes Google Dorking, DNS, SAN discovery and bruteforce.

### Web Application Analysis
- **CMS detection**: Identification of the Content Management Systems used.
- **Web server and X-Powered-By**: Discovery of server technologies.
- **Robots.txt and sitemap extraction**: Access to robots.txt and sitemaps files.
- **Cookie inspection**: Detection and analysis of cookies.
- **Extracting fuzzable URLs and HTML forms**: Identification of interaction points.
- **Email address recovery**: Analysis and recovery of public email addresses.
- **Storage Scan**: Search for vulnerable S3 buckets and enumerate sensitive files.
- **WAF detection**: Identification of known application firewalls.

### Performance and Anonymity
- **Routing via Tor/Proxy**: Supports request anonymization.
- **Asyncio support**: Asynchronous execution of scans for optimal performance.
- **Advanced logging**: Saving output in files, by targets and modules.

---
### Port Analysis
- **Port Scans**: Evaluation of open ports for detection of active services.
- **Services and Scripts Scan**: Use of specific scripts to obtain detailed information about online services.

### Fuzzing and Enumeration
- **URL Fuzzing and File/Dir Detection**: Search for hidden or sensitive files and directories.
- **Subdomain enumeration**: Includes Google Dorking, DNS, SAN discovery and bruteforce.

### Web Application Analysis
- **CMS detection**: Identification of the Content Management Systems used.
- **Web server and X-Powered-By**: Discovery of server technologies.
- **Robots.txt and sitemap extraction**: Access to robots.txt and sitemaps files.
- **Cookie inspection**: Detection and analysis of cookies.
- **Extracting fuzzable URLs and HTML forms**: Identification of interaction points.
- **Email address recovery**: Analysis and recovery of public email addresses.
- **Storage Scan**: Search for vulnerable S3 buckets and enumerate sensitive files.
- **WAF detection**: Identification of known application firewalls.

### Performance and Anonymity
- **Routing via Tor/Proxy**: Supports request anonymization.
- **Asyncio support**: Asynchronous execution of scans for optimal performance.
- **Advanced logging**: Saving output in files, by targets and modules.

---### Port Analysis
- **Port Scans**: Evaluation of open ports for detection of active services.
- **Services and Scripts Scan**: Use of specific scripts to obtain detailed information about online services.

### Fuzzing and Enumeration
- **URL Fuzzing and File/Dir Detection**: Search for hidden or sensitive files and directories.
- **Subdomain enumeration**: Includes Google Dorking, DNS, SAN discovery and bruteforce.

### Web Application Analysis
- **CMS detection**: Identification of the Content Management Systems used.
- **Web server and X-Powered-By**: Discovery of server technologies.
- **Robots.txt and sitemap extraction**: Access to robots.txt and sitemaps files.
- **Cookie inspection**: Detection and analysis of cookies.
- **Extracting fuzzable URLs and HTML forms**: Identification of interaction points.
- **Email address recovery**: Analysis and recovery of public email addresses.
- **Storage Scan**: Search for vulnerable S3 buckets and enumerate sensitive files.
- **WAF detection**: Identification of known application firewalls.

### Performance and Anonymity
- **Routing via Tor/Proxy**: Supports request anonymization.
- **Asyncio support**: Asynchronous execution of scans for optimal performance.
- **Advanced logging**: Saving output in files, by targets and modules.

---
Clone the GitHub repository to benefit from recent features and updates:

```bash
git clone https://github.com/RhaB17369/cherlock.git
cd spynet
python setup.py install
```
### To execute code changes in real time, use:

``` bash
python setup.py develop
```

### macOS compatibility
On macOS, you will need the gtimeout tool:

```bash
brew install coreutils
```
### Docker
To run Spynet in a Docker container:

```bash
# Building the Docker image
docker build -t cherlock 
```
# Running a scan
```bash
docker run --name cherlock_container cherlock:latest example.com -o /home/cherlock
```
# Prerequisites
Nmap: Used for port scanning and running Nmap scripts.
OpenSSL: Needed for TLS/SSL scanning.
# Usage
Run spynet --help to see all available command options and their descriptions.

Examples of Orders
For a full scan with default options:

```bash
cherlock -d example.com
```
To specify a target with Tor/proxy enabled:

```bash
cherlock -d example.com --tor
```
To save the output in JSON format:

```bash
cherlock -d example.com --output-format json
```
# Screenshots 
![Screenshot 2024-10-29 082552](https://github.com/user-attachments/assets/a88cf618-4522-41dc-b2ab-8d988c97a6d6)
![Screenshot 2024-10-29 082406](https://github.com/user-attachments/assets/d512fdd8-5459-459d-93b2-129b4ddfba41)
![Screenshot 2024-10-29 082345](https://github.com/user-attachments/assets/cee7921f-023a-4d56-929c-c81b88b59ad7)
# Nmap vulners scan results:
![68747470733a2f2f696d6167652e6962622e636f2f69614f4d79552f6e6d61705f76756c6e6572735f706f632e706e67](https://github.com/user-attachments/assets/46643aab-58a6-4af4-8fd2-9e0c3a035392)
# HTB challenge example scan:
![68747470733a2f2f696d6167652e6962622e636f2f62474b5452792f626262626262622e706e67](https://github.com/user-attachments/assets/47fc53b5-6792-4384-a41f-ad9a9cbf10c9)

# About
cherlock is designed for IT security professionals looking to obtain an accurate and in-depth security assessment of information systems. Thanks to its flexibility and extensive configuration options, Spynet integrates seamlessly into security workflows, providing a comprehensive and technical view of the target infrastructure.

