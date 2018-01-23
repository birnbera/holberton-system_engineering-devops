# 0x17. Web stack debugging #3

This project consists of writing a Puppet manifest to correct problems with an Apache2 server hosting Wordpress content.

### Requirements

- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint` without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4

### Deploying manifest

This project is based on the LAMP stack serving Wordpress and is deployed as a Docker container for our debugging project. In order to use the provided manifest, transfer the Puppet manifest to the container using `scp` and run the script with:
```
puppet apply 0-strace_is_your_friend.pp
```
### Tasks

#### 0. Strace is you friend

Use `strace` to find out why Apache is returning a 500 status code. Once the source of the problem is discovered, use Puppet to write a manifest that will correct the issue.
Use `tmux` to run `strace` in one window, while running `curl` in the another.

###### Requirements:

- `0-strace_is_your_friend.pp` must contain Puppet code
- Use any Puppet resource type for the fix
