<h1 class="gap">0x0F. Load balancer</h1>


<h4 class="task">
    0. Double the number of webservers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>In this first task you need to configure <code>web-02</code> to be identical to <code>web-01</code>. Fortunately, you built a Bash script during your <a href="/rltoken/8oRonOh-zV4e2bmsZ3sxEw" target="_blank" title="web server project">web server project</a>, and they’ll now come in handy to easily configure <code>web-02</code>. Remember, always try to automate your work!</p><p>Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</p><p>Requirements:</p><ul>
<li>Configure Nginx so that its HTTP response contains a custom header (on <code>web-01</code> and <code>web-02</code>)

<ul>
<li>The name of the custom HTTP header must be <code>X-Served-By</code></li>
<li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
</ul></li>
<li>Write <code>0-custom_http_response-header</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task

<ul>
<li><a href="/rltoken/3AOvROMUNUrzxEWhli4GTw" target="_blank" title="Ignore">Ignore</a> <a href="/rltoken/i5f8DYX_rRYFz4hfbG_GJg" target="_blank" title="SC2154">SC2154</a> for <code>shellcheck</code></li>
</ul></li>
</ul><p>Example:</p>


<h4 class="task">
    1. Install your load balancer
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Install and configure HAproxy on your <code>lb-01</code> server.</p><p>Requirements:</p><ul>
<li>Configure HAproxy with version equal or greater than 1.5 so that it send traffic to <code>web-01</code> and <code>web-02</code></li>
<li>Distribute requests using a roundrobin algorithm</li>
<li>Make sure that HAproxy can be managed via an init script</li>
<li>Make sure that your servers are configured with the right hostnames: <code>[STUDENT_ID]-web-01</code> and <code>[STUDENT_ID]-web-02</code>. If not, follow this <a href="/rltoken/P7nGAS_YjgHdjAt8KTgJbw" target="_blank" title="tutorial">tutorial</a>.</li>
<li>For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul><p>Example:</p>

