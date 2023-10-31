#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([a-zA-z0-9+]*)\] \[to:(.*?)\] \[flags:([0-9+-:]*)\]/).join
