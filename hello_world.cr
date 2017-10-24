require "colorize"

str = "Hello, World!"
color_seq = [:black,:red,:green,:yellow,:blue,:magenta,:cyan,:light_gray,
             :dark_gray,:light_red,:light_green,:light_yellow,:light_blue,
             :light_magenta,:light_cyan,:white]


start = Time.new()
elapsed = 5
limit = 5

while elapsed > 0
  color_seq.each do |color|
    print "#{str} #{elapsed}".colorize(color)
    sleep 0.1.seconds
    print "\r"
    elapsed = limit - (start.second - Time.new().second).abs
  end
end
