<h1 class="gap">0x09. Web server</h1>


<h4 class="task">
    0. Transfer a file to your server
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that transfers a file from our client to a server:</p><p>Requirements:</p><ul>
<li>Accepts 4 parameters

<ol>
<li>The path to the file to be transferred</li>
<li>The IP of the server we want to transfer the file to</li>
<li>The username <code>scp</code> connects with</li>
<li>The path to the SSH private key that <code>scp</code> uses</li>
</ol></li>
<li>Display <code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 3 parameters passed</li>
<li><code>scp</code> must transfer the file to the user home directory <code>~/</code></li>
<li>Strict host key checking must be disabled when using <code>scp</code> </li>
</ul><p>Example:</p>


<h4 class="task">
    1. Install nginx web server
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Readme:</p><ul>
<li><a href="/rltoken/Tcbz_WMUUcFSZd0TjxHRLA" target="_blank" title="-y on apt-get command">-y on apt-get command</a></li>
</ul><p>Web servers are the piece of software generating and serving HTML pages, let’s install one!</p><p>Requirements:</p><ul>
<li>Install <code>nginx</code> on your <code>web-01</code> server</li>
<li>Nginx should be listening on port 80</li>
<li>When querying Nginx at its root <code>/</code> with a GET request (requesting a page)  using <code>curl</code>, it must return a page that contains the string <code>Holberton School</code></li>
<li>As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul><p>Example:</p>


<h4 class="task">
    2. Setup a domain name
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p><a href="/rltoken/hKxGLx11hbaww7MDmdxTBg" target="_blank" title="Gandi">Gandi</a> is one of the top 25 domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with Gandi so that you can learn about DNS.</p><p>Gandi worked with domain name registrars to give you access to a free domain name for a year. Please use the promo code <strong>THXBETTY</strong>. Feel free to drop a thank you tweet for <a href="/rltoken/u9yMc-L0d0tLdupPnsG01A" target="_blank" title="Gandi">Gandi</a>.</p><p>Using your Gandi account, acquire a domain name at this <a href="/rltoken/hKxGLx11hbaww7MDmdxTBg" target="_blank" title="address">address</a>, using one of these extensions: </p><ul>
<li><code>.website</code></li>
<li><code>.site</code></li>
<li><code>.space</code></li>
<li><code>.online</code></li>
</ul><p>Provide the domain name in your answer file.</p><p>Requirement:</p><ul>
<li>provide the domain name only (example: <code>foobar.online</code>), no subdomain (example: <code>www.foobar.online</code>)</li>
<li>configure your DNS records with an A entry so that your root domain points to your <code>web-01</code> IP address</li>
<li>go to <a href="/rltoken/fYvJr4-HV1WPnfB7HCue_Q" target="_blank" title="your profile">your profile</a> and enter your domain in the <code>Project website url</code> field</li>
</ul><p>Example:</p>


<h4 class="task">
    3. Redirection
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Readme:</p><ul>
<li><a href="/rltoken/VxTHgC6QPUnYqY808HLAbg" target="_blank" title="Replace a line with multiple lines with sed">Replace a line with multiple lines with sed</a></li>
</ul><p>Configure your Nginx server so that <code>/redirect_me</code> is redirecting to another page.</p><p>Requirements:</p><ul>
<li>The redirection must be a “301 Moved Permanently”</li>
<li>You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements</li>
<li>Using what you did with <code>1-install_nginx_web_server</code>, write <code>3-redirection</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul><p>Example:</p>


<h4 class="task">
    4. Not found page 404
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Configure your Nginx server to have a custom 404 page that contains the string <code>Ceci n'est pas une page</code>.</p><p>Requirements:</p><ul>
<li>The page must return an HTTP 404 error code</li>
<li>The page must contain the string <code>Ceci n'est pas une page</code></li>
<li>Using what you did with <code>3-redirection</code>, write <code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul><p>Example:</p>

