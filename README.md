DNS Resolver
This project is a Python application that performs DNS resolution operations. DNS resolution is used to resolve the IP address of a specific domain name.

Installation
 1.Download or clone the project:
 git clone https://github.com/Ecthelionn/DNS-Resolver
 2. Install the required library:
 pip install dnspython
Usage
 1.Navigate to the directory where the project is located in your terminal or command prompt:
 cd DNS-Resolver
 2.To start the DNS resolution process, run:
 python resolver.py
 3.The program will prompt you to enter the domain name and file path. Please enter this information in the correct format.
File Structure
The entries.txt file should contain a list of subdomains and paths to be scanned. For example:
subdomain1
subdomain2
/admin
/login
Required Libraries
DNSPython
<h1>DNS Resolver</h1>

<p>This project is a Python application that performs DNS resolution operations. DNS resolution is used to resolve the IP address of a specific domain name.</p>

<h2>Installation</h2>

<ol>
  <li>Download or clone the project:</li>
  <code>git clone https://github.com/username/DNS-Resolver.git</code>

  <li>Install the required library:</li>
  <code>pip install dnspython</code>
</ol>

<h2>Usage</h2>

<ol>
  <li>Navigate to the directory where the project is located in your terminal or command prompt:</li>
  <code>cd DNS-Resolver</code>

  <li>To start the DNS resolution process, run:</li>
  <code>python resolver.py</code>

  <li>The program will prompt you to enter the domain name and file path. Please enter this information in the correct format.</li>
</ol>

<h2>File Structure</h2>

<p>The <code>entries.txt</code> file should contain a list of subdomains and paths to be scanned. For example:</p>

<pre>
subdomain1
subdomain2
/admin
/login
</pre>

<h2>Required Libraries</h2>

<ul>
  <li><a href="https://pypi.org/project/dnspython/">DNSPython</a></li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.</p>
