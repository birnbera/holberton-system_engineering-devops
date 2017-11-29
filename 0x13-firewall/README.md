<h1 class="gap">0x13. Firewall</h1>


<h4 class="task">
    0. Firewall ABC
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Pick one answer for every question.</p><p>What is a firewall?</p><ol>
<li>A hardware security system</li>
<li>A hardware or software security system</li>
<li>A software security system</li>
</ol><p>What are the 2 types of firewall:</p><ol>
<li>Soft and hard firewall</li>
<li>Incoming and outgoing firewall</li>
<li>Network and host-based firewall</li>
</ol><p>What is the main function of a firewall?</p><ol>
<li>To filter incoming and outgoing network traffic</li>
<li>To filter  incoming and outgoing TCP traffic</li>
<li>To  filter outgoing traffic</li>
</ol>


<h4 class="task">
    1. Block all incoming traffic but
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s install the <code>ufw</code> firewall and setup a few rules on <code>web-01</code>.</p><p>Requirements:</p><ul>
<li>The requirements below must be applied to <code>web-01</code> (feel free to do it on <code>lb-01</code> and <code>web-02</code>, but it won’t be checked)</li>
<li>Configure <code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:

<ul>
<li><code>22</code> (SSH)</li>
<li><code>443</code> (HTTPS SSL)</li>
<li><code>80</code> (HTTP)</li>
</ul></li>
<li>Share the <code>ufw</code> commands that you used in your answer file</li>
</ul>


<h4 class="task">
    2. Port forwarding
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Firewalls can not only filter requests, they can also forward them.</p><p>Requirements:</p><ul>
<li>Configure <code>web-01</code> so that its firewall redirects port <code>8080/TCP</code> to port <code>80/TCP</code>.</li>
<li>Your answer file should be a copy of the <code>ufw</code> configuration file that you modified to make this happen</li>
</ul><p>Terminal in <code>web-01</code>:</p>

