<h1 class="gap">0x15. API</h1>


<h4 class="task">
    0. Gather data from an API
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that, using this <a href="/rltoken/0Ltm_dXy-m4E9jchBrKLVA" target="_blank" title="REST API">REST API</a>, for a given employee ID, returns information about his/her TODO list progress.</p><p>Requirements:</p><ul>
<li>You are free to use any native Python3 module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress in this exact format:

<ul>
<li>First line: <code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code>
<ul>
<li><code>EMPLOYEE_NAME</code>: name of the employee</li>
<li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li>
<li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li>
</ul></li>
<li>Second and N next lines display the title of completed tasks: Tab <code>TASK_TITLE</code></li>
</ul></li>
</ul><p>Example:</p>


<h4 class="task">
    1. Export to CSV
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p><p>Requirements:</p><ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"</code></li>
<li>File name must be: <code>USER_ID.csv</code></li>
</ul><p>Example:</p>


<h4 class="task">
    2. Export to JSON
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p><p>Requirements:</p><ul>
<li>Records all tasks that are owned by this employee</li>
<li>Formart must be: <code>{ "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}</code></li>
<li>File name must be: <code>USER_ID.json</code></li>
</ul><p>Example:</p>


<h4 class="task">
    3. Dictionary of list of dictionaries
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p><p>Requirements:</p><ul>
<li>Records all tasks from all employees</li>
<li>Formart must be: <code>{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}</code></li>
<li>File name must be: <code>todo_all_employees.json</code></li>
</ul><p>Example:</p>

