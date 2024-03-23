#!/usr/bin/env bash
# Using puppet to change our configuration file

file { 'etc/ssh/ssh_cofig':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentification no
	",

}
