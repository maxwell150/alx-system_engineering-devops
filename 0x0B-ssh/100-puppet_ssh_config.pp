# Sets up your client SSH configuration file so that you can connect to a server 
#without typing a password
include stdlib

file_line { 'USE private key':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'IdentityFile ~/.ssh/school'
}

file_line { 'TURN OFF Password Auth':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no'
}
