import os
import shutil
from platform import system
from collections import Counter
from subprocess import PIPE, check_call, CalledProcessError
from requests.exceptions import ConnectionError
from cherlock.utils.exceptions import cherlockException, ScannerException, RequestHandlerException
from cherlock.utils.request_handler import RequestHandler


class HelpUtilities:

    PATH = ""

    @classmethod
    def validate_target_is_up(cls, host):
        cmd = "ping -c 1 {}".format(host.target)
        try:
            check_call(cmd.split(), stdout=PIPE, stderr=PIPE)
            return
        except CalledProcessError:
            # If ICMP is blocked, try checking the web server
            try:
                url = "{}://{}".format(host.protocol, host.target) if host.port in {80, 443} else "{}://{}:{}".format(host.protocol, host.target, host.port)
                rh = RequestHandler()
                rh.send("GET", url=url, timeout=15)
                return
            except (ConnectionError, RequestHandlerException):
                raise cherlockException(f"Target {host} seems to be down (no response to ping or from a web server at port {host.port})."
                                       " Run with --skip-health-check to ignore hosts considered as down.")

    @classmethod
    def parse_cookie_arg(cls, cookie_arg):
        try:
            cookies = {c.split(":")[0]: c.split(":")[1] for c in cookie_arg.split(',')}
            return cookies
        except (IndexError, TypeError):
            raise cherlockException("Cookie parsing error occurred, likely due to invalid format. "
                                   "Cookie format should be comma-separated key:value pairs. Use --help for more info.")

    @classmethod
    def validate_wordlist_args(cls, proxy_list, wordlist, subdomain_list):
        for file_path in [proxy_list, wordlist, subdomain_list]:
            if file_path and not os.path.isfile(file_path):
                raise FileNotFoundError(f"Not a valid file path: {file_path}")

    @classmethod
    def validate_port_range(cls, port_range):
        """Validate port range for Nmap scan"""
        ports = port_range.split("-")
        if len(ports) == 2 and all(ports) and int(ports[1]) <= 65535:
            return True
        raise ScannerException(f"Invalid port range {port_range}")

    @classmethod
    def validate_proxy_args(cls, *args):
        """Only one of the following can be specified: tor_routing, proxy, proxy_list"""
        supplied_proxies = Counter((not arg for arg in args)).get(False)
        if supplied_proxies > 1:
            raise cherlockException("Must specify only one of the following: --tor-routing, --proxy-list, --proxy")

    @classmethod
    def determine_verbosity(cls, quiet):
        return "CRITICAL" if quiet else "INFO"

    @classmethod
    def find_nmap_executable(cls):
        return shutil.which("nmap")

    @classmethod
    def find_openssl_executable(cls):
        return shutil.which("openssl")

    @classmethod
    def find_mac_gtimeout_executable(cls):
        """For macOS support, coreutils package needs to be installed using Homebrew"""
        return shutil.which("gtimeout")

    @classmethod
    def validate_executables(cls):
        if not (cls.find_nmap_executable() and cls.find_openssl_executable()):
            raise cherlockException("Could not find Nmap or OpenSSL installed. Please install them and try again.")
        if system() == "Darwin" and not cls.find_mac_gtimeout_executable():
            raise cherlockException("To support macOS, 'gtimeout' must be installed.\n"
                                   "Install it with 'brew install coreutils'")
        return

    @classmethod
    def create_output_directory(cls, outdir):
        """Tries to create base output directory"""
        cls.PATH = outdir
        try:
            os.mkdir(outdir)
        except FileExistsError:
            pass

    @classmethod
    def get_output_path(cls, module_path):
        return f"{cls.PATH}/{module_path}"

    @classmethod
    def confirm_traffic_routs_through_tor(cls):
        rh = RequestHandler()
        try:
            page = rh.send("GET", url="https://check.torproject.org")
            if "Congratulations. This browser is configured to use Tor." in page.text:
                return
            elif "Sorry. You are not using Tor" in page.text:
                raise cherlockException("Traffic does not seem to be routed through Tor. Exiting.")
        except RequestHandlerException:
            raise cherlockException("Tor service seems to be down - unable to connect to 127.0.0.1:9050. Exiting.")

    @classmethod
    def query_dns_dumpster(cls, host):
        request_handler = RequestHandler()
        dnsdumpster_session = request_handler.get_new_session()
        url = "https://dnsdumpster.com"
        target = host.naked or host.target
        payload = {"targetip": target, "csrfmiddlewaretoken": None}
        try:
            dnsdumpster_session.get(url, timeout=10)
            jar = dnsdumpster_session.cookies
            for c in jar:
                if c.__dict__.get("name") == "csrftoken":
                    payload["csrfmiddlewaretoken"] = c.__dict__.get("value")
                    break
            dnsdumpster_session.post(url, data=payload, headers={"Referer": "https://dnsdumpster.com/"})
            return dnsdumpster_session.get(f"https://dnsdumpster.com/static/map/{target}.png")
        except ConnectionError:
            raise cherlockException

    @classmethod
    def extract_hosts_from_cidr(cls):
        pass

    @classmethod
    def extract_hosts_from_range(cls):
        pass
