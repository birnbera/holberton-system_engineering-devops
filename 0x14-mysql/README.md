<h1 class="gap">0x14. Mysql</h1>


<h4 class="task">
    0. Setup a Primary-Replica infrastructure using MySQL
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p><img alt="Redundancy simply explained" src="http://i.imgur.com/FOeOLrP.gif"/></p><p>Install and configure MySQL  on<code>web-01</code> and <code>web-02</code> so that they for a primary/replica (master/slave) cluster.</p><p>Having a replica member on for your MySQL database has 2 advantages:</p><ul>
<li>Redundancy: if you lose one of the database servers, you will still have another working one and a copy of your data</li>
<li>Load distribution: you can split the read operations between the 2 servers, allowing to reduce the load on the primary member and improve query response speed</li>
</ul><p>Requirements:</p><ul>
<li>MySQL primary must be hosted on <code>web-01</code> - do no use the <code>bind-address</code>,  just comment this parameter</li>
<li>MySQL replica must be hosted on <code>web-02</code></li>
<li>Setup replication for the MySQL database named <code>holberton</code></li>
<li>Provide your MySQL primary configuration as answer file(<code>my.cnf</code>) with the name <code>0-mysql_configuration_primary</code></li>
<li>Provide your MySQL replica configuration as answer file with the name <code>0-mysql_configuration_replica</code></li>
<li>Create a MySQL user named <code>holberton</code>, password <code>projectcorrection280hbtn</code> with read access on replication status (the checker will use it to verify that replication is running fine)</li>
<li>Make sure that task <a href="/rltoken/wZyb9uhoQNOeFGabkDdO2g" target="_blank" title="#3 of your SSH project is completed">#3 of your SSH project is completed</a> for <code>web-01</code> and <code>web-02</code>, the checker will connect to your servers to check MySQL status</li>
</ul><p>Tips:</p><ul>
<li>Once MySQL is installed on <code>web-01</code>, create a database containing at least one table with one record (name and what type of fields does not matter)</li>
<li>Once MySQL replication is setup, add a new record in your table via MySQL on <code>web-01</code> and check if the record has been replicated in MySQL <code>web-02</code>. If you see it, it means your replication is working!</li>
</ul><p>Example:</p>


<h4 class="task">
    1. MySQL backup
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p><a href="https://www.youtube.com/watch?v=ANU-oSE5_hU" target="_blank"><img alt="Flooded datacenter" src="https://i.imgur.com/Bbpsgif.jpg"/></a></p><p>What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.</p><p>Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.</p><p>Requirements:</p><ul>
<li>The MySQL dump must contain all your MySQL databases</li>
<li> The MySQL dump must be named <code>backup.sql</code></li>
<li>The MySQL dump file has to be compressed to a <code>tar.gz</code> archive</li>
<li>This archive must have the following name format: <code>day-month-year.tar.gz</code></li>
<li>The user to connect to the MySQL database must be <code>root</code></li>
<li>The Bash script accepts one argument that is the password used to connect to the MySQL database</li>
</ul><p>Example:</p>

