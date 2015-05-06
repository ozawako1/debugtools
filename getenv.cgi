#!/usr/bin/env ruby
# encoding: utf-8

ARGV.each { |arg|
	case arg
	when "PROXY"
		use_proxy = 1
	when "DEBUG"
		use_debug = 1
	else
		puts("undefined arg. [" + arg + "]")
	end
}

envs = "<table>\r\n"
envs += "<tr><th align='left'>ENVS<td>" + ENV.length.to_s + "\r\n"
ENV.each do |k, v|
	envs += "<tr><th align='left'>" + k + "<td>" + v + "\r\n"
end
envs +="</table>\r\n"

print(<<"EOSTR")
Content-Type: text/html

<html>
<title>hello, ruby cgi.</title>
<body>
	#{envs}
</body>
</html>
EOSTR