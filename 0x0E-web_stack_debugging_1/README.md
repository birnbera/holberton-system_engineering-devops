<h1 class="gap">0x0E. Web stack debugging #1</h1>


<h4 class="task">
    0. Nginx likes port 80
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port <code>80</code>. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.</p><p>Requirements:</p><ul>
<li>Nginx must be running, and listening on port <code>80</code> of all the server’s active IPv4 IPs </li>
<li>Write a Bash script that configures a server to the above requirements</li>
</ul><p>Container before debugging (I manually installed <code>curl</code> to show this example):</p>


<h4 class="task">
    1. Make it sweet and short
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Using what you did for task #0, make your fix short and sweet.</p><p>Requirements:</p><ul>
<li>Your Bash script must be 5 lines long or less</li>
<li>There must be a new line at the end of the file</li>
<li>You must respect usual Bash script requirements</li>
<li>You cannot use <code>;</code> </li>
<li>You cannot use <code>&amp;&amp;</code></li>
<li><code>service</code> (init) must say that <code>nginx</code> is not running</li>
</ul>

