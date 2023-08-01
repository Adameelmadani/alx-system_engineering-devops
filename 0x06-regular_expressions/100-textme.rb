#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from\:)(\w+|\+\d{1,})|(?<=to\:)(\w+|\+\d{1,})|((?<=flags\:).*?(?=\]))/).join(",")
