
erl -eval '{ok, Version} = file:read_
file(filename:join([code:root_dir(),"release",
erlang:system_info(otp_release),"OTP_VERSION"])),
io:fwrite(Version),halt().'-noshell
