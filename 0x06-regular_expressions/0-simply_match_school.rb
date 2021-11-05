#!/usr/bin/env ruby
# A ruby script that accepts one arg and pass it to a regular expression matching method

puts ARGV[0].scan(/School/).join
