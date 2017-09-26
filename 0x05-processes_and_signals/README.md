<h1 class="gap">0x05. Processes and signals</h1>
  <h4 class="task">
    0. What is my PID
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that displays its PID.</p>
  <h4 class="task">
    1. List your processes
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that displays a list of currently running processes.</p>

<p>Requirements:</p>

<ul>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display a user-oriented format</li>
<li>Show process hierarchy</li>
</ul>
  <h4 class="task">
    2. Show your Bash PID
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Using your previous exercise command, write a Bash script that displays line containing the <code>bash</code> word, this allowing you to easily get the PID of your Bash process</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>pgrep</code></li>
<li>The third line of your script must be <code># shellcheck disable=SC2009</code> (for more info about ignoring <code>shellcheck</code> error <a href="https://github.com/koalaman/shellcheck/wiki/Ignore">here</a>)</li>
</ul>
  <h4 class="task">
    3. Show your Bash PID made easy
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that displays the PID, along with the process name, of processes which name contains the word <code>bash</code>.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>ps</code></li>
</ul>
  <h4 class="task">
    4. To infinity and beyond
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>

<p>Requirements:</p>

<ul>
<li>In between each iteration of the loop, add a <code>sleep 2</code></li>
</ul>
  <h4 class="task">
    5. Kill me now
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>We killed our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>

<p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>kill</code></li>
</ul>
  <h4 class="task">
    6. Kill me now made easy
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
</ul>
  <h4 class="task">
    7. Highlander
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that displays: </p>

<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>

<p>Make a copy of your <code>6-kill_me_now_made_easy</code> script, name it <code>67-kill_me_now_made_easy</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>
  <h4 class="task">
    8. Beheaded process
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that kills the process <code>7-highlander</code>.</p>
  <h4 class="task">
    9. Process and PID file
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a Bash script that: </p>

<ul>
<li>Creates the file <code>/var/run/holbertonscript.pid</code> containing its PID</li>
<li>Displays <code>To infinity and beyond</code> indefinitely</li>
<li>Displays <code>I hate the kill command</code> when receiving a SIGTERM signal</li>
<li>Displays <code>Y U no love me?!</code> when receiving a SIGINT signal</li>
<li>Deletes the file <code>/var/run/holbertonscript.pid</code> and terminate itself when receiving a SIGQUIT or SIGTERM signal</li>
</ul>
  <h4 class="task">
    10. Manage my process
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p><img src="http://i.imgur.com/o9q0iPA.jpg" alt="Priest stopping data center with /etc/init.d/DEAMON STOP"></p>

<p>Read:</p>

<ul>
<li><a href="http://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html">&amp;</a></li>
<li><a href="http://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/">init.d</a></li>
<li><a href="https://en.wikipedia.org/wiki/Daemon_(computing)">Daemon</a></li>
<li><a href="http://wiki.bash-hackers.org/scripting/posparams">Positional parameters</a></li>
</ul>

<p>man: <code>sudo</code></p>

<p>Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: <code>start</code>, <code>restart</code> and <code>stop</code>. The most popular way of doing so on Unix system is to use the init scripts.</p>

<p>Write a <code>manage_my_process</code> Bash script that: </p>

<ul>
<li>Indefinitely writes <code>I am alive!</code> to the file <code>/tmp/my_process</code></li>
<li>In between every <code>I am alive!</code> message, the program should pause for 2 seconds</li>
</ul>

<p>Write Bash (init) script <code>101-manage_my_process</code> that manages <code>manage_my_process</code></p>

<p>Requirements:</p>

<ul>
<li>When passing the argument <code>start</code>:

<ul>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process started</code></li>
</ul></li>
<li>When passing the argument <code>stop</code>: 

<ul>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process stopped</code></li>
</ul></li>
<li>When passing the argument <code>restart</code>

<ul>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process restarted</code></li>
</ul></li>
<li>Displays <code>Usage: manage_my_process {start|stop|restart}</code> if any other argument or no argument is passed</li>
</ul>

<p>Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing <code>./101-manage_my_process start</code>, in our case it will simply create a new process instead of saying that it is already started.</p>
  <h4 class="task">
    11. Zombie
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p><a href="http://fineartamerica.com/featured/zombie-seahorse-lauren-b.html"><img src="http://i.imgur.com/C6mO7b3.jpg" alt="Zombie searhose"></a></p>

<p>Read <a href="https://zombieprocess.wordpress.com/what-is-a-zombie-process/">what a zombie process is</a>.</p>

<p>Write a C program that creates 5 zombie processes.</p>

<p>Requirements:</p>

<ul>
<li>For every zombie process created, it displays <code>Zombie process created, PID: ZOMBIE_PID</code></li>
<li>Your code should use the Betty style. It will be checked using <code>betty-style.pl</code> and <code>betty-doc.pl</code></li>
<li>When you code is done creating the parent process and the zombies, use the function bellow</li>
</ul>

<pre><code>int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
</code></pre>
